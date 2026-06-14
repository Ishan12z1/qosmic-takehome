import contextlib
import io
import json
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import Mock, patch

import evals.run_eval as eval_module
from evals.analyze_failures import build_candidates, unique_failures
from crawler.crawl_store import homepage_loaded_cleanly
from crawler.shopping_journey import _score_from_flags
from crawler.technical_checks import check_broken_links
from crawler.url_discovery import _is_valid_store_url, select_pages
from crawler.utils import detect_payment_methods, find_existing_run, normalize_host


class CrawlerRegressionTests(unittest.TestCase):
    def test_www_normalization_preserves_legitimate_w_prefixes(self):
        for host in ["warbyparker.com", "walmart.com", "woodlandfoods.com"]:
            self.assertEqual(normalize_host(host), host)
            self.assertTrue(_is_valid_store_url(f"https://{host}/", host))
            self.assertTrue(_is_valid_store_url(f"https://www.{host}/", host))

    def test_discovered_pages_outrank_guessed_standard_paths(self):
        base = "https://example.com"
        guessed = {
            f"{base}/pages/faq",
            f"{base}/pages/about",
        }
        urls = [
            f"{base}/",
            f"{base}/pages/faqs",
            f"{base}/pages/faq",
            f"{base}/pages/aboutus",
            f"{base}/pages/about",
        ]

        selected, _ = select_pages(urls, base, guessed_links=guessed)
        selected_urls = {entry["url"] for entry in selected}

        self.assertIn(f"{base}/pages/faqs", selected_urls)
        self.assertIn(f"{base}/pages/aboutus", selected_urls)
        self.assertNotIn(f"{base}/pages/faq", selected_urls)
        self.assertNotIn(f"{base}/pages/about", selected_urls)

    def test_existing_run_prefers_newest_usable_run_over_blocked_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime.now()
            self._make_run(root, "shop_healthy", "Healthy", now)
            self._make_run(root, "shop_degraded", "Degraded", now + timedelta(minutes=1))
            self._make_run(root, "shop_blocked", "Blocked", now + timedelta(minutes=2))

            self.assertEqual(find_existing_run("shop", root), "shop_degraded")

            self._make_run(root, "shop_newest", "Healthy", now + timedelta(minutes=3))
            self.assertEqual(find_existing_run("shop", root), "shop_newest")

    def test_existing_run_does_not_reuse_blocked_only_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            now = datetime.now()
            self._make_run(root, "shop_blocked_old", "Blocked", now)
            self._make_run(root, "shop_blocked_new", "Blocked", now + timedelta(minutes=1))

            self.assertIsNone(find_existing_run("shop", root))

    def test_blocked_homepage_disables_mobile_and_speed_measurement(self):
        self.assertFalse(homepage_loaded_cleanly([
            {"page_type": "homepage", "status": "blocked"},
            {"page_type": "product_page", "status": "ok"},
        ]))
        self.assertTrue(homepage_loaded_cleanly([
            {"page_type": "homepage", "status": "ok"},
        ]))

    def test_api_add_fallback_reduces_journey_score(self):
        self.assertLess(_score_from_flags(["api_add_to_cart_fallback"]), 5.0)

    def test_access_denied_links_are_not_reported_as_broken(self):
        response = Mock(status_code=403)
        with patch("crawler.technical_checks._SESSION.head", return_value=response):
            result = check_broken_links(["https://example.com/cart"])

        self.assertEqual(result["status"], "Warn")
        self.assertIn("could not be verified", result["detail"])

    def test_payment_detection_does_not_treat_discover_verb_as_card_brand(self):
        html = "<html><body><a href='/products'>Discover our products</a></body></html>"
        self.assertEqual(detect_payment_methods(html), [])

    @staticmethod
    def _make_run(root: Path, name: str, verdict: str, crawled_at: datetime):
        run = root / name
        (run / "pages").mkdir(parents=True)
        (run / "discovered_links.json").write_text(
            json.dumps({"crawled_at": crawled_at.isoformat()}), encoding="utf-8")
        (run / "technical_checks.json").write_text("{}", encoding="utf-8")
        (run / "summary.md").write_text(
            f"**Crawl health: {verdict}**", encoding="utf-8")
        (run / "pages" / "shopping_journey.json").write_text("{}", encoding="utf-8")


class EvalRegressionTests(unittest.TestCase):
    def test_completed_layer9_is_detected_for_preservation(self):
        text = (
            "# Eval\n\n## Layer 9: Quality Rubric\n\n"
            "| Dimension | Score |\n|---|---|\n| Quality | 5 |\n\n"
            "**Total: 50/50**"
        )
        self.assertIn("**Total: 50/50**", eval_module._completed_layer9(text))
        self.assertEqual(eval_module._completed_layer9("# Eval\n\n## Layer 9: Quality Rubric"), "")

    def test_failure_analysis_uses_unique_distinct_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "failures.jsonl"
            entries = [
                {"run_id": "a", "layer": 1, "failure_type": "missing_section", "detail": "x"},
                {"run_id": "a", "layer": 1, "failure_type": "missing_section", "detail": "x"},
                {"run_id": "b", "layer": 1, "failure_type": "missing_section", "detail": "y"},
            ]
            log.write_text(
                "\n".join(json.dumps(entry) for entry in entries), encoding="utf-8")

            failures = unique_failures(log)
            candidates = build_candidates(failures, min_runs=2)

        self.assertEqual(len(failures), 2)
        self.assertEqual(candidates[0]["distinct_runs"], 2)

    def test_zero_experiments_fail_field_validation(self):
        result = eval_module.layer4_experiment_fields("# Report", "run")
        self.assertFalse(result["passed"])

    def test_missing_technical_checks_fail(self):
        result = eval_module.layer7_technical_checks("## Technical Checks", None, "run")
        self.assertFalse(result["passed"])

    def test_technical_details_must_match_exactly(self):
        checks = {
            f"check_{index}": {
                "label": f"Check {index}",
                "status": "Pass",
                "detail": f"Detail {index}",
            }
            for index in range(17)
        }
        rows = "\n".join(
            f"| Check {index} | Pass | {'WRONG' if index == 3 else f'Detail {index}'} |"
            for index in range(17)
        )
        report = f"## Technical Checks\n\n| Check | Status | Detail |\n|---|---|---|\n{rows}"

        result = eval_module.layer7_technical_checks(report, checks, "run")
        self.assertFalse(result["passed"])
        self.assertIn("detail does not match", result["detail"])

    def test_failure_log_deduplicates_identical_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            previous = eval_module.FAILURE_LOG
            eval_module.FAILURE_LOG = Path(tmp) / "failures.jsonl"
            try:
                eval_module._log_failure("run", 1, "type", "detail")
                eval_module._log_failure("run", 1, "type", "detail")
                lines = eval_module.FAILURE_LOG.read_text(encoding="utf-8").splitlines()
            finally:
                eval_module.FAILURE_LOG = previous

        self.assertEqual(len(lines), 1)

    def test_blocked_uses_reduced_eval_but_degraded_uses_full_eval(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._configure_eval_roots(root)
            partial = (
                "# Partial Audit - Crawl Issues\n\n"
                "Blocked by bot protection. No full audit was produced."
            )

            blocked = self._make_eval_run(root, "blocked", "Blocked", partial)
            degraded = self._make_eval_run(root, "degraded", "Degraded", partial)

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(eval_module.run_eval(blocked), 0)
                self.assertEqual(eval_module.run_eval(degraded), 1)

    def test_failed_eval_returns_nonzero(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._configure_eval_roots(root)
            run_id = self._make_eval_run(root, "bad", "Healthy", "# Invalid report")

            with contextlib.redirect_stdout(io.StringIO()):
                result = eval_module.run_eval(run_id)

        self.assertEqual(result, 1)

    def test_read_health_verdict_supports_hyphenated_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            (run_dir / "summary.md").write_text(
                "**Crawl health: Non-ecommerce**", encoding="utf-8"
            )

            self.assertEqual(eval_module._read_health_verdict(run_dir), "Non-ecommerce")

    def setUp(self):
        self.previous_roots = (
            eval_module.ARTIFACTS_ROOT,
            eval_module.SAMPLE_OUTPUT_ROOT,
            eval_module.EVAL_RESULTS_ROOT,
            eval_module.FAILURE_LOG,
        )
        self.temp_log_dir = tempfile.TemporaryDirectory()
        eval_module.FAILURE_LOG = Path(self.temp_log_dir.name) / "failure_log.jsonl"

    def tearDown(self):
        (
            eval_module.ARTIFACTS_ROOT,
            eval_module.SAMPLE_OUTPUT_ROOT,
            eval_module.EVAL_RESULTS_ROOT,
            eval_module.FAILURE_LOG,
        ) = self.previous_roots
        self.temp_log_dir.cleanup()

    @staticmethod
    def _configure_eval_roots(root: Path):
        eval_module.ARTIFACTS_ROOT = root / "artifacts"
        eval_module.SAMPLE_OUTPUT_ROOT = root / "sample_output"
        eval_module.EVAL_RESULTS_ROOT = root / "eval_results"
        eval_module.FAILURE_LOG = root / "failure_log.jsonl"
        eval_module.ARTIFACTS_ROOT.mkdir()
        eval_module.SAMPLE_OUTPUT_ROOT.mkdir()

    @staticmethod
    def _make_eval_run(root: Path, run_id: str, verdict: str, report: str) -> str:
        run = root / "artifacts" / run_id
        run.mkdir(parents=True)
        (run / "summary.md").write_text(
            f"**Crawl health: {verdict}**\n\n## Issues a reader should know\n",
            encoding="utf-8",
        )
        (root / "sample_output" / f"{run_id}_audit.md").write_text(
            report, encoding="utf-8")
        return run_id


if __name__ == "__main__":
    unittest.main()
