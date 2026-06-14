(function(){let e=navigator,t=`prototype`,n=`sendBeacon`,r=e[n],i=fetch,a=XMLHttpRequest[t],{open:o,send:s}=a,c=`EventListener`,l=`add${c}`,u=`remove${c}`,d=EventTarget[t],f=d[l],p=d[u],m=e=>Error((e=document.currentScript)&&[e?.src,e?.id||e?.dataset?.sourceAttribution]),h=(e=[],t=0)=>(e.p=n=>e[t++%1e3]=n,[e,t=>(e.forEach(e.p=t),e.length=0)]),[g,\_]=h(),[v,y]=h(),b,x=new WeakMap,S=e=>e&&g.p([e,b||[m()]]);d[l]=function(e,t,n){let r=this,i=t?.handleEvent||t,a=x.get(t),o=m();i?.call&&!a&&x.set(t,a=function(e){b=[o,e.type];try{i.call(t==i?this:t,e)}finally{b=null}}),v.p([e,o,a,r?.tagName||r+``,r?.id]),f.call(r,e,a||t,n)},d[u]=function(e,t,n){p.call(this,e,x.get(t)||t,n)},a.open=function(e,t){x.set(this,[t+``,e]),o.apply(this,arguments)},a.send=function(e){S(x.get(this)),s.call(this,e)},fetch=(e,t)=>(S([(e?.url||e)+``,t?.method]),i(e,t)),e[n]=(t,n)=>(S([t+``,``]),r.call(e,t,n)),setTimeout(()=>import("//www.beardbrand.com/cdn/shopifycloud/storefront/assets/storefront/event\_observer\_reporter-de731130.js").then(e=>e.$(\_,y,f,i,`2090478`)))})();
//# sourceURL=event-observer-collector.js


Your Shopping Cart – Beardbrand















{
"@context": "https://schema.org",
"@type": "BreadcrumbList",
"itemListElement": [{
"@type": "ListItem",
"position": 1,
"name": "Home",
"item": "https://www.beardbrand.com"
}]
}
{
"@context": "https://schema.org",
"@type" : "Organization",
"name" : "Beardbrand",
"url" : "https://www.beardbrand.com",
"potentialAction": {
"@type": "SearchAction",
"target": "https://www.beardbrand.com/search?q={search\_term}",
"query-input": "required name=search\_term"
}
}









window.performance && window.performance.mark && window.performance.mark('shopify.content\_for\_header.start');









{"shopId":2090478,"countryCode":"US","currencyCode":"USD","merchantCapabilities":["supports3DS"],"merchantId":"gid:\/\/shopify\/Shop\/2090478","merchantName":"Beardbrand","requiredBillingContactFields":["postalAddress","email","phone"],"requiredShippingContactFields":["postalAddress","email","phone"],"shippingType":"shipping","supportedNetworks":["visa","masterCard","amex","discover","elo","jcb"],"total":{"type":"pending","label":"Beardbrand","amount":"1.00"},"shopifyPaymentsEnabled":true,"supportsSubscriptions":true}
{"accessToken":"fff70b01a4e85354a9671d0ccd9fe597","betas":["rich-media-storefront-analytics"],"domain":"www.beardbrand.com","predictiveSearch":true,"shopId":2090478,"locale":"en"}
var Shopify = Shopify || {};
Shopify.shop = "beardbrand.myshopify.com";
Shopify.locale = "en";
Shopify.currency = {"active":"USD","rate":"1.0"};
Shopify.country = "US";
Shopify.theme = {"name":"Split v1.0.3.6.7 [PDP vid section optz]","id":190866391410,"schema\_name":"Split","schema\_version":"3.1.0","theme\_store\_id":842,"role":"main"};
Shopify.theme.handle = "null";
Shopify.theme.style = {"id":null,"handle":null};
Shopify.cdnHost = "www.beardbrand.com/cdn";
Shopify.routes = Shopify.routes || {};
Shopify.routes.root = "/";
Shopify.shopJsCdnBaseUrl = "https://cdn.shopify.com/shopifycloud/shop-js";
Shopify.SignInWithShop = Shopify.SignInWithShop || {};
Shopify.SignInWithShop.User = Shopify.SignInWithShop.User || {};
Shopify.SignInWithShop.User.recognized = false;
!function(o){(o.Shopify=o.Shopify||{}).modules=!0}(window);
!function(o){function n(){var o=[];function n(){o.push(Array.prototype.slice.apply(arguments))}return n.q=o,n}var t=o.Shopify=o.Shopify||{};t.loadFeatures=n(),t.autoloadFeatures=n()}(window);

window.ShopifyPay = window.ShopifyPay || {};
window.ShopifyPay.apiHost = "shop.app\/pay";
window.ShopifyPay.redirectState = null;

window.Shopify = window.Shopify || {};
window.Shopify.SignInWithShop = window.Shopify.SignInWithShop || {};
window.Shopify.SignInWithShop.assetMetrics = { sampleRate: 0.01 };
window.Shopify.SignInWithShop.eligible = true;
{"pageType":"cart"}


await import("//www.beardbrand.com/cdn/shopifycloud/shop-js/modules/v2/loader.init-shop-cart-sync.en.esm.js");
window.Shopify.SignInWithShop?.initShopCartSync?.({"fedCMEnabled":true,"windoidEnabled":true,"transferSessionEnabled":true});

window.Shopify = window.Shopify || {};
if (!window.Shopify.featureAssets) window.Shopify.featureAssets = {};
window.Shopify.featureAssets['shop-js'] = {"shop-toast-manager":["modules/v2/loader.shop-toast-manager.en.esm.js"],"shop-button":["modules/v2/loader.shop-button.en.esm.js"],"shop-cash-offers":["modules/v2/loader.shop-cash-offers.en.esm.js"],"listener":["modules/v2/loader.listener.en.esm.js"],"shop-login-button":["modules/v2/loader.shop-login-button.en.esm.js"],"init-windoid":["modules/v2/loader.init-windoid.en.esm.js"],"avatar":["modules/v2/loader.avatar.en.esm.js"],"init-fed-cm":["modules/v2/loader.init-fed-cm.en.esm.js"],"init-shop-user-recognition":["modules/v2/loader.init-shop-user-recognition.en.esm.js"],"checkout-modal":["modules/v2/loader.checkout-modal.en.esm.js"],"init-shop-cart-sync":["modules/v2/loader.init-shop-cart-sync.en.esm.js"],"init-customer-accounts-sign-up":["modules/v2/loader.init-customer-accounts-sign-up.en.esm.js"],"init-shop-email-lookup-coordinator":["modules/v2/loader.init-shop-email-lookup-coordinator.en.esm.js"],"init-shop-for-new-customer-accounts":["modules/v2/loader.init-shop-for-new-customer-accounts.en.esm.js"],"pay-button":["modules/v2/loader.pay-button.en.esm.js"],"shop-cart-sync":["modules/v2/loader.shop-cart-sync.en.esm.js"],"shop-login":["modules/v2/loader.shop-login.en.esm.js"],"shop-user-recognition":["modules/v2/loader.shop-user-recognition.en.esm.js"],"shop-follow-button":["modules/v2/loader.shop-follow-button.en.esm.js"],"init-customer-accounts":["modules/v2/loader.init-customer-accounts.en.esm.js"],"lead-capture":["modules/v2/loader.lead-capture.en.esm.js"],"payment-terms":["modules/v2/loader.payment-terms.en.esm.js"]};
(function() {
var isLoaded = false;
function asyncLoad() {
if (isLoaded) return;
isLoaded = true;
var urls = ["https:\/\/app.electricsms.com\/cart-widget\/widget.min.js?shop=beardbrand.myshopify.com","https:\/\/static.rechargecdn.com\/assets\/js\/widget.min.js?shop=beardbrand.myshopify.com","https:\/\/cdn.richpanel.com\/js\/richpanel\_shopify\_script.js?appClientId=beardbrand8661\u0026tenantId=beardbrand866\u0026shop=beardbrand.myshopify.com\u0026shop=beardbrand.myshopify.com","\/\/backinstock.useamp.com\/widget\/35336\_1772124979.js?category=bis\u0026v=6\u0026shop=beardbrand.myshopify.com"];
for (var i = 0; i < urls.length; i++) {
var s = document.createElement('script');
s.type = 'text/javascript';
s.async = true;
s.src = urls[i];
var x = document.getElementsByTagName('script')[0];
x.parentNode.insertBefore(s, x);
}
};
if(window.attachEvent) {
window.attachEvent('onload', asyncLoad);
} else {
window.addEventListener('load', asyncLoad, false);
}
})();
var \_\_st={"a":2090478,"offset":-18000,"reqid":"d301d72c-6eec-44e1-903f-af721b86d8b6-1781460400","pageurl":"www.beardbrand.com\/cart","u":"1b9316e21df6","p":"cart"};
window.ShopifyPaypalV4VisibilityTracking = true;
!function(){'use strict';const t='contact',e='account',n='new\_comment',o=[[t,t],['blogs',n],['comments',n],[t,'customer']],c=[[e,'customer\_login'],[e,'guest\_login'],[e,'recover\_customer\_password'],[e,'create\_customer']],r=t=>t.map((([t,e])=>`form[action\*='/${t}']:not([data-nocaptcha='true']) input[name='form\_type'][value='${e}']`)).join(','),a=t=>()=>t?[...document.querySelectorAll(t)].map((t=>t.form)):[];function s(){const t=[...o],e=r(t);return a(e)}const i='password',u='form\_key',d=['recaptcha-v3-token','g-recaptcha-response','h-captcha-response',i],f=()=>{try{return window.sessionStorage}catch{return}},m='\_\_shopify\_v',\_=t=>t.elements[u];function p(t,e,n=!1){try{const o=window.sessionStorage,c=JSON.parse(o.getItem(e)),{data:r}=function(t){const{data:e,action:n}=t;return t[m]||n?{data:e,action:n}:{data:t,action:n}}(c);for(const[e,n]of Object.entries(r))t.elements[e]&&(t.elements[e].value=n);n&&o.removeItem(e)}catch(o){console.error('form repopulation failed',{error:o})}}const l='form\_type',E='cptcha';function T(t){t.dataset[E]=!0}const w=window,h=w.document,L='Shopify',v='ce\_forms',y='captcha';let A=!1;((t,e)=>{const n=(g='f06e6c50-85a8-45c8-87d0-21a2b65856fe',I='https://cdn.shopify.com/shopifycloud/storefront-forms-hcaptcha/ce\_storefront\_forms\_captcha\_hcaptcha.v1.5.2.iife.js',D={infoText:'Protected by hCaptcha',privacyText:'Privacy',termsText:'Terms'},(t,e,n)=>{const o=w[L][v],c=o.bindForm;if(c)return c(t,g,e,D).then(n);var r;o.q.push([[t,g,e,D],n]),r=I,A||(h.body.append(Object.assign(h.createElement('script'),{id:'captcha-provider',async:!0,src:r})),A=!0)});var g,I,D;w[L]=w[L]||{},w[L][v]=w[L][v]||{},w[L][v].q=[],w[L][y]=w[L][y]||{},w[L][y].protect=function(t,e){n(t,void 0,e),T(t)},Object.freeze(w[L][y]),function(t,e,n,w,h,L){const[v,y,A,g]=function(t,e,n){const i=e?o:[],u=t?c:[],d=[...i,...u],f=r(d),m=r(i),\_=r(d.filter((([t,e])=>n.includes(e))));return[a(f),a(m),a(\_),s()]}(w,h,L),I=t=>{const e=t.target;return e instanceof HTMLFormElement?e:e&&e.form},D=t=>v().includes(t);t.addEventListener('submit',(t=>{const e=I(t);if(!e)return;const n=D(e)&&!e.dataset.hcaptchaBound&&!e.dataset.recaptchaBound,o=\_(e),c=g().includes(e)&&(!o||!o.value);(n||c)&&t.preventDefault(),c&&!n&&(function(t){try{if(!f())return;!function(t){const e=f();if(!e)return;const n=\_(t);if(!n)return;const o=n.value;o&&e.removeItem(o)}(t);const e=Array.from(Array(32),(()=>Math.random().toString(36)[2])).join('');!function(t,e){\_(t)||t.append(Object.assign(document.createElement('input'),{type:'hidden',name:u})),t.elements[u].value=e}(t,e),function(t,e){const n=f();if(!n)return;const o=[...t.querySelectorAll(`input[type='${i}']`)].map((({name:t})=>t)),c=[...d,...o],r={};for(const[a,s]of new FormData(t).entries())c.includes(a)||(r[a]=s);n.setItem(e,JSON.stringify({[m]:1,action:t.action,data:r}))}(t,e)}catch(e){console.error('failed to persist form',e)}}(e),e.submit())}));const S=(t,e)=>{t&&!t.dataset[E]&&(n(t,e.some((e=>e===t))),T(t))};for(const o of['focusin','change'])t.addEventListener(o,(t=>{const e=I(t);D(e)&&S(e,y())}));const B=e.get('form\_key'),M=e.get(l),P=B&&M;t.addEventListener('DOMContentLoaded',(()=>{const t=y();if(P)for(const e of t)e.elements[l].value===M&&p(e,B);[...new Set([...A(),...v().filter((t=>'true'===t.dataset.shopifyCaptcha))])].forEach((e=>S(e,t)))}))}(h,new URLSearchParams(w.location.search),n,t,e,['guest\_login'])})(!0,!0)}();



var Shopify=Shopify||{};Shopify.PaymentButton=Shopify.PaymentButton||{isStorefrontPortableWallets:!0,init:function(){window.Shopify.PaymentButton.init=function(){};var t=document.createElement("script");t.src="https://www.beardbrand.com/cdn/shopifycloud/portable-wallets/latest/portable-wallets.en.js",t.type="module",document.head.appendChild(t)}};

function portableWalletsHideBuyerConsent(e){var t=document.getElementById("shopify-buyer-consent"),n=document.getElementById("shopify-subscription-policy-button");t&&n&&(t.classList.add("hidden"),t.setAttribute("aria-hidden","true"),n.removeEventListener("click",e))}function portableWalletsShowBuyerConsent(e){var t=document.getElementById("shopify-buyer-consent"),n=document.getElementById("shopify-subscription-policy-button");t&&n&&(t.classList.remove("hidden"),t.removeAttribute("aria-hidden"),n.addEventListener("click",e))}window.Shopify?.PaymentButton&&(window.Shopify.PaymentButton.hideBuyerConsent=portableWalletsHideBuyerConsent,window.Shopify.PaymentButton.showBuyerConsent=portableWalletsShowBuyerConsent);
document.addEventListener("DOMContentLoaded",(function(){function t(){return document.querySelector("shopify-accelerated-checkout-cart, shopify-accelerated-checkout")}if(t())Shopify.PaymentButton.init();else{new MutationObserver((function(e,n){t()&&(Shopify.PaymentButton.init(),n.disconnect())})).observe(document.body,{childList:!0,subtree:!0})}}));


#shopify-buyer-consent {
margin-top: 1em;
display: inline-block;
width: 100%;
}
#shopify-buyer-consent.hidden {
display: none;
}
#shopify-subscription-policy-button {
background: none;
border: none;
padding: 0;
text-decoration: underline;
font-size: inherit;
cursor: pointer;
}
#shopify-subscription-policy-button::before {
box-shadow: none;
}
window.performance && window.performance.mark && window.performance.mark('shopify.content\_for\_header.end');




const rbi = [];
const ribSetSize = (img) => {
if ( img.offsetWidth / img.dataset.ratio < img.offsetHeight ) {
img.setAttribute('sizes', `${Math.ceil(img.offsetHeight \* img.dataset.ratio)}px`);
} else {
img.setAttribute('sizes', `${Math.ceil(img.offsetWidth)}px`);
}
}
function debounce(fn, wait) {
let t;
return (...args) => {
clearTimeout(t);
t = setTimeout(() => fn.apply(this, args), wait);
};
}
window.addEventListener('resize', debounce(()=>{
for ( let img of rbi ) {
ribSetSize(img);
}
}, 250));

/\* HW Pano Bold - Headings \*/
@font-face {
font-family: 'HW\_Pano\_Bold';
src: url('https://cdn.shopify.com/s/files/1/0209/0478/files/HW\_Pano\_Bold.woff?v=1689187304') format('woff');
font-style: normal;
font-display: fallback;
}
/\* Space Grotesk — Regular (400) \*/
@font-face {
font-family: 'Space Grotesk';
src: url('https://cdn.shopify.com/s/files/1/0209/0478/files/SpaceGrotesk-Regular.woff2?v=1745862684') format('woff2');
font-weight: 400;
font-style: normal;
font-display: fallback;
}
/\* Space Grotesk — Medium (500)\*/
@font-face {
font-family: 'Space Grotesk';
src: url('https://cdn.shopify.com/s/files/1/0209/0478/files/SpaceGrotesk-Medium.woff2?v=1758576253') format('woff');
font-weight: 500;
font-style: normal;
font-display: fallback;
}
/\* Space Grotesk — Bold (700) \*/
@font-face {
font-family: 'Space Grotesk';
src: url('https://cdn.shopify.com/s/files/1/0209/0478/files/SpaceGrotesk-Bold.woff2?v=1745862684') format('woff2');
font-weight: 700;
font-style: normal;
font-display: fallback;
}

:root {
/\* Main color scheme \*/
--main-text: #101010;
--main-text-hover: rgba(16, 16, 16, 0.82);
--main-text-foreground: #fff;
--main-background: #f9f8f6;
--main-background-gradient: rgba(249, 248, 246, 0);
--main-background-secondary: rgba(16, 16, 16, 0.18);
--main-background-third: rgba(16, 16, 16, 0.03);
--main-borders: #101010;
/\* Header & sidebars color scheme \*/
--header-text: #101010;
--header-text-foreground: #fff;
--header-background: #f9f8f6;
--header-background-secondary: rgba(16, 16, 16, 0.18);
--header-borders: #101010;
/\* Footer color scheme \*/
--footer-text: ;
--footer-text-foreground: #fff;
--footer-background: ;
--footer-background-secondary: ;
--footer-borders: ;
/\* Buttons radius \*/
--buttons-radius: 0px;
/\* Font variables \*/
--font-stack-headings: "HW\_Pano\_Bold", Zurich Bold Extended, Verdana, Geneva, sans-serif;
--font-weight-headings: 400;
--font-style-headings: normal;
--font-stack-body: "Space Grotesk", mono;
--font-weight-body: 400; /\* restore body to regular weight \*/
--font-stack-body-bold: "Space Grotesk", mono; /\* simplify: use same family \*/
--font-weight-body-bold: 700; /\* true bold \*/
--font-style-body: normal;
--base-headings-size: 55;
--base-headings-line: 1.1;
--base-body-size: 19;
--base-body-line: 1.6;
}
select, .regular-select-cover {
background-image: url("data:image/svg+xml,%0A%3Csvg width='14' height='9' viewBox='0 0 14 9' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M8.42815 7.47604L7.01394 8.89025L0.528658 2.40497L1.94287 0.990753L8.42815 7.47604Z' fill='rgb(16, 16, 16)'/%3E%3Cpath d='M6.98591 8.89025L5.5717 7.47604L12.057 0.990755L13.4712 2.40497L6.98591 8.89025Z' fill='rgb(16, 16, 16)'/%3E%3C/svg%3E%0A");
}
sidebar-drawer .facets\_\_disclosure:after, sidebar-drawer select {
background-image: url("data:image/svg+xml,%0A%3Csvg width='14' height='9' viewBox='0 0 14 9' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M8.42815 7.47604L7.01394 8.89025L0.528658 2.40497L1.94287 0.990753L8.42815 7.47604Z' fill='rgb(16, 16, 16)'/%3E%3Cpath d='M6.98591 8.89025L5.5717 7.47604L12.057 0.990755L13.4712 2.40497L6.98591 8.89025Z' fill='rgb(16, 16, 16)'/%3E%3C/svg%3E%0A");
}
// This allows to expose several variables to the global scope, to be used in scripts
window.lazySizesConfig = {
loadHidden: false,
hFac: 0.5,
expFactor: 2,
ricTimeout: 150,
lazyClass: 'Image--lazyLoad',
loadingClass: 'Image--lazyLoading',
loadedClass: 'Image--lazyLoaded'
};
document.documentElement.className = document.documentElement.className.replace('no-js', 'js');
document.documentElement.style.setProperty('--window-height', window.innerHeight + 'px');
// We do a quick detection of some features (we could use Modernizr but for so little...)
(function() {
document.documentElement.className += ((window.CSS && window.CSS.supports('(position: sticky) or (position: -webkit-sticky)')) ? ' supports-sticky' : ' no-supports-sticky');
document.documentElement.className += (window.matchMedia('(-moz-touch-enabled: 1), (hover: none)')).matches ? ' no-supports-hover' : ' supports-hover';
}());





console.log('growi-embed.liquid');
console.log('🔵 [GROWI-EMBED] growi-embed.liquid inline script STARTED, v.1.8.0');
console.log('🔵 [GROWI-EMBED] Script execution timestamp:', new Date().toISOString());
console.log('🔵 [GROWI-EMBED] Document readyState:', document.readyState);
console.log('🔵 [GROWI-EMBED] window.growiCookieUtils exists?', typeof window.growiCookieUtils !== 'undefined');
if (typeof window.growiCookieUtils !== 'undefined') {
console.log('✅ [GROWI-EMBED] Cookie utils ALREADY available!', window.growiCookieUtils);
} else {
console.log('⏳ [GROWI-EMBED] Cookie utils NOT YET available, will wait...');
}
(function () {
// Default customization settings
const defaultCustomization = {
popup\_enabled: true,
heading\_text: null,
body\_text: null,
button\_text: null,
helper\_text: null,
background\_color: '#ffffff',
text\_color: '#000000',
button\_color: '#2c2c2c',
button\_text\_color: '#ffffff',
banner\_enabled: false,
banner\_top\_offset: 0,
emoji: '🎉',
};
// Fetch customization settings from API
async function fetchCustomization(affiliateTag) {
try {
const response = await fetch(
`https://api.growi.io/api/v1/campaigns/ambassador\_program\_customization?affiliate\_tag=${encodeURIComponent(
affiliateTag
)}&url=${encodeURIComponent(window.location.href)}`,
{
method: 'GET',
headers: {
'Content-Type': 'application/json',
},
}
);
if (!response.ok) {
console.warn('Customization API returned error, returning null');
return null;
}
const data = await response.json();
if (data.success && data.customization) {
console.log('✅ Loaded customization settings:', data.customization);
return data.customization;
} else {
console.log('ℹ️ No customization found, returning null');
return null;
}
} catch (error) {
console.error('Failed to fetch customization, returning null:', error);
return null;
}
}
function showDiscountModal(discountCode, affiliateName, discountValue, discountType, affiliateId) {
console.log('showDiscountModal', discountCode, affiliateName, discountValue, discountType, affiliateId);
if (
!discountValue ||
discountValue === '0' ||
discountValue === 0 ||
discountValue === null ||
discountValue === undefined ||
discountValue === 'null'
)
return;
// Prevent duplicate modals
if (document.getElementById('\_\_growi-modal-overlay')) return;
const overlay = document.createElement('div');
overlay.id = '\_\_growi-modal-overlay';
overlay.style.cssText = `
display:block;
position:fixed;
top:0; left:0;
width:100%; height:100%;
background-color:rgba(0,0,0,0.5);
z-index:9998;
`;
const modal = document.createElement('div');
modal.className = '\_\_growi\_modal\_content';
modal.style.cssText = `
display:block;
background-color:white;
z-index:9999;
border-top:10px solid #2C2C2C;
border-radius:10px;
text-align:center;
margin:auto;
min-height:400px;
height:auto;
position:fixed;
top:50%; left:50%;
transform:translate(-50%, -50%);
width:90%; max-width:500px;
`;
// Add mobile-specific styles
const mobileStyles = document.createElement('style');
mobileStyles.textContent = `
@media (max-width: 768px) {
.\_\_growi\_modal\_content {
top: calc(50% + 20px) !important;
}
}
@media (max-width: 480px) {
.\_\_growi\_modal\_content {
top: calc(50% + 30px) !important;
}
}
`;
document.head.appendChild(mobileStyles);
modal.innerHTML = `
<div class="\_\_growi-modal-inner" style="display:block;position:relative;width:100%;height:100%;padding:40px 40px 40px 40px;box-sizing:border-box;">
<button id="\_\_growi-close-modal" style="position:absolute;top:15px;right:15px;background-color:transparent;border:none;cursor:pointer;z-index:10000;padding:5px;">
<svg style="fill:#000000" height="20px" width="20px" viewBox="0 0 490 490" xmlns="http://www.w3.org/2000/svg">
<polygon points="456.851,0 245,212.564 33.149,0 0.708,32.337
212.669,245.004 0.708,457.678 33.149,490
245,277.443 456.851,490 489.292,457.678
277.331,245.004 489.292,32.337"/>
</svg>
</button>
<div style="text-align:center;width:100%;">
<p style="text-align:center;margin:0 0 20px 0;">
<img src="https://d2pnkb2a79l965.cloudfront.net/party-popper-emoji.png" style="width:80px;height:80px;display:inline-block;">
</p>
<h2 style="
text-align:center;
font-size:2.5em;
line-height:1em;
margin:0.5em 0;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
font-weight:bold;
color:#000000;
">
${affiliateName ? decodeURIComponent(affiliateName) : "We've"} sent you ${discountValue}${
discountType === 'percentage' ? '%' : '$'
} off!
</h2>
<h3 style="
text-align:center;
font-size:1.3em;
margin:0.8em 0;
color:#9aaab9;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
">
Click below to redeem your discount code
</h3>
<button id="\_\_growi-redeem-btn" style="
display:block;
margin:20px auto 0 auto;
padding:12px 20px;
width:230px;
background-color:#2c2c2c;
color:#ffffff;
border:1px solid #535459;
border-radius:5px;
font-size:1.2em;
cursor:pointer;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
">
Redeem Coupon
</button>
<div style="font-size:0.8em;color:#9aaab9;margin-top:10px;text-align:center;">
<em>Your discount will automatically be applied at checkout</em>
</div>
</div>
</div>
`;
overlay.appendChild(modal);
document.body.appendChild(overlay);
// Close handler
document.getElementById('\_\_growi-close-modal').onclick = () => {
window.growiCookieUtils.setCookie('discount\_seen', `${affiliateId.toLowerCase()}`, -1);
overlay.remove();
};
// Redeem handler
document.getElementById('\_\_growi-redeem-btn').onclick = () => {
const redeemBtn = document.getElementById('\_\_growi-redeem-btn');
// Set loading state
redeemBtn.disabled = true;
redeemBtn.style.cursor = 'not-allowed';
redeemBtn.innerHTML = `
<svg style="animation: spin 1s linear infinite; width: 20px; height: 20px; display: inline-block; margin-right: 8px;" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" stroke-dasharray="31.416" stroke-dashoffset="31.416" fill="none" stroke-linecap="round"/>
</svg>
Loading...
`;
// Add spinning animation
const style = document.createElement('style');
style.textContent = `
@keyframes spin {
0% { transform: rotate(0deg); }
100% { transform: rotate(360deg); }
}
`;
document.head.appendChild(style);
// Simulate loading delay then show discount code
setTimeout(() => {
// Replace button with discount code
redeemBtn.style.display = 'none';
// Create discount code container
const discountCodeDiv = document.createElement('div');
discountCodeDiv.id = '\_\_growi-discount-code';
discountCodeDiv.style.cssText = `
background-color:#ecf0ff;
display:block;
width:90%;
margin:20px auto 0 auto;
text-align:center;
color:#3860fb;
font-size:25px;
padding:8px;
cursor:pointer;
border-radius:5px;
font-weight:bold;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif;
`;
discountCodeDiv.innerHTML = `
${discountCode.toUpperCase()}
<img src="https://d2pnkb2a79l965.cloudfront.net/copy-blue-icon.png" style="width:22px;margin-bottom:-5px;display:inline;">
`;
// Add copy functionality
discountCodeDiv.onclick = () => {
navigator.clipboard
.writeText(discountCode.toUpperCase())
.then(() => {
// Show copied feedback under the code
let copiedText = document.getElementById('\_\_growi-copied-text');
if (!copiedText) {
copiedText = document.createElement('div');
copiedText.id = '\_\_growi-copied-text';
copiedText.style.cssText = `
font-size:0.9em;
color:#28a745;
margin-top:8px;
text-align:center;
`;
discountCodeDiv.parentNode.insertBefore(copiedText, discountCodeDiv.nextSibling);
}
copiedText.innerHTML = '✓ Discount applied!';
})
.catch(() => {
// Fallback for older browsers
const textArea = document.createElement('textarea');
textArea.value = discountCode.toUpperCase();
document.body.appendChild(textArea);
textArea.select();
document.execCommand('copy');
document.body.removeChild(textArea);
let copiedText = document.getElementById('\_\_growi-copied-text');
if (!copiedText) {
copiedText = document.createElement('div');
copiedText.id = '\_\_growi-copied-text';
copiedText.style.cssText = `
font-size:0.9em;
color:#28a745;
margin-top:8px;
text-align:center;
`;
discountCodeDiv.parentNode.insertBefore(copiedText, discountCodeDiv.nextSibling);
}
copiedText.innerHTML = '✓ Discount applied!';
});
};
// Insert the discount code div after the button
redeemBtn.parentNode.insertBefore(discountCodeDiv, redeemBtn.nextSibling);
}, 1500);
window.growiCookieUtils.setCookie('discount\_seen', `${affiliateId.toLowerCase()}`);
};
}
async function showDiscountModalV2(discountCode, affiliateName, discountValue, discountType, affiliateId) {
console.log('showDiscountModalV2', discountCode, affiliateName, discountValue, discountType, affiliateId);
if (
!discountValue ||
discountValue === '0' ||
discountValue === 0 ||
discountValue === null ||
discountValue === undefined ||
discountValue === 'null'
)
return;
// Fetch customization from API
const customization = await fetchCustomization(affiliateId);
// If no customization exists, fall back to the original showDiscountModal
if (!customization) {
console.log('ℹ️ No customization available, falling back to default modal');
showDiscountModal(discountCode, affiliateName, discountValue, discountType, affiliateId);
return;
}
// Prevent duplicate modals
if (document.getElementById('\_\_growi-modal-overlay')) return;
// Merge customization with defaults
const config = { ...defaultCustomization, ...customization };
// Check if popup is enabled
if (!config.popup\_enabled) {
console.log('ℹ️ Popup is disabled by customization settings');
if (config.banner\_enabled) {
window.growiCookieUtils.setCookie('discount\_seen', affiliateId.toLowerCase());
showBanner(affiliateId, discountCode, customization);
}
return;
}
const headingText =
config.heading\_text ||
`${affiliateName ? decodeURIComponent(affiliateName) : "We've"} sent you ${discountValue}${
discountType === 'percentage' ? '%' : '$'
} off!`;
const bodyText = config.body\_text || 'Click below to redeem your discount code';
const buttonText = config.button\_text || 'Redeem Coupon';
const helperText = config.helper\_text || 'Your discount will automatically be applied at checkout';
const buttonMarkup = config.hide\_button
? ''
: `<button id="\_\_growi-redeem-btn" style="
display:block;
margin:20px auto 0 auto;
padding:12px 20px;
width:230px;
background-color:${config.button\_color};
color:${config.button\_text\_color};
border:1px solid ${config.button\_color};
border-radius:5px;
font-size:1.2em;
cursor:pointer;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
">
${buttonText}
</button>`;
const helperMarkup = `
<div style="font-size:0.8em;color:${config.text\_color};opacity:0.7;margin-top:10px;text-align:center;">
<em>${helperText}</em>
</div>
`;
const overlay = document.createElement('div');
overlay.id = '\_\_growi-modal-overlay';
overlay.style.cssText = `
display:block;
position:fixed;
top:0; left:0;
width:100%; height:100%;
background-color:rgba(0,0,0,0.5);
z-index:9998;
`;
const modal = document.createElement('div');
modal.className = '\_\_growi\_modal\_content';
modal.style.cssText = `
display:block;
background-color:${config.background\_color};
z-index:9999;
border-top:10px solid #2C2C2C;
border-radius:10px;
text-align:center;
margin:auto;
min-height:400px;
height:auto;
position:fixed;
top:50%; left:50%;
transform:translate(-50%, -50%);
width:90%; max-width:500px;
`;
// Add mobile-specific styles
const mobileStyles = document.createElement('style');
mobileStyles.textContent = `
@media (max-width: 768px) {
.\_\_growi\_modal\_content {
top: calc(50% + 20px) !important;
}
}
@media (max-width: 480px) {
.\_\_growi\_modal\_content {
top: calc(50% + 30px) !important;
}
}
`;
document.head.appendChild(mobileStyles);
modal.innerHTML = `
<div class="\_\_growi-modal-inner" style="display:block;position:relative;width:100%;height:100%;padding:40px 40px 40px 40px;box-sizing:border-box;">
<button id="\_\_growi-close-modal" style="position:absolute;top:15px;right:15px;background-color:transparent;border:none;cursor:pointer;z-index:10000;padding:5px;">
<svg style="fill:${config.text\_color}" height="20px" width="20px" viewBox="0 0 490 490" xmlns="http://www.w3.org/2000/svg">
<polygon points="456.851,0 245,212.564 33.149,0 0.708,32.337
212.669,245.004 0.708,457.678 33.149,490
245,277.443 456.851,490 489.292,457.678
277.331,245.004 489.292,32.337"/>
</svg>
</button>
<div style="text-align:center;width:100%;">
<p style="text-align:center;margin:0 0 20px 0;">
<span style="font-size:80px;line-height:1;display:inline-block;">${config.emoji || '🎉'}</span>
</p>
<h2 style="
text-align:center;
font-size:2.5em;
line-height:1em;
margin:0.5em 0;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
font-weight:bold;
color:${config.text\_color};
">
${headingText}
</h2>
<h3 style="
text-align:center;
font-size:1.3em;
margin:0.8em 0;
color:${config.text\_color};
opacity:0.7;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji,
Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
">
${bodyText}
</h3>
${buttonMarkup}
${helperMarkup}
</div>
</div>
`;
overlay.appendChild(modal);
document.body.appendChild(overlay);
// Close handler
const closeButton = document.getElementById('\_\_growi-close-modal');
if (closeButton) {
closeButton.onclick = () => {
window.growiCookieUtils.setCookie('discount\_seen', affiliateId.toLowerCase(), -1);
overlay.remove();
};
}
// Redeem handler
const redeemBtn = document.getElementById('\_\_growi-redeem-btn');
if (redeemBtn) {
redeemBtn.onclick = () => {
// Set loading state (preserve custom button colors)
redeemBtn.disabled = true;
redeemBtn.style.cursor = 'not-allowed';
redeemBtn.style.backgroundColor = config.button\_color;
redeemBtn.style.color = config.button\_text\_color;
redeemBtn.innerHTML = `
<svg style="animation: spin 1s linear infinite; width: 20px; height: 20px; display: inline-block; margin-right: 8px;" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" stroke-dasharray="31.416" stroke-dashoffset="31.416" fill="none" stroke-linecap="round"/>
</svg>
Loading...
`;
// Add spinning animation
const style = document.createElement('style');
style.textContent = `
@keyframes spin {
0% { transform: rotate(0deg); }
100% { transform: rotate(360deg); }
}
`;
document.head.appendChild(style);
// Simulate loading delay then show discount code
setTimeout(() => {
// Replace button with discount code
redeemBtn.style.display = 'none';
// Create discount code container
const discountCodeDiv = document.createElement('div');
discountCodeDiv.id = '\_\_growi-discount-code';
discountCodeDiv.style.cssText = `
background-color:#ecf0ff;
display:block;
width:90%;
margin:20px auto 0 auto;
text-align:center;
color:#3860fb;
font-size:25px;
padding:8px;
cursor:pointer;
border-radius:5px;
font-weight:bold;
font-family:-apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif;
`;
discountCodeDiv.innerHTML = `
${discountCode.toUpperCase()}
<img src="https://d2pnkb2a79l965.cloudfront.net/copy-blue-icon.png" style="width:22px;margin-bottom:-5px;display:inline;">
`;
// Add copy functionality
discountCodeDiv.onclick = () => {
navigator.clipboard
.writeText(discountCode.toUpperCase())
.then(() => {
// Show copied feedback under the code
let copiedText = document.getElementById('\_\_growi-copied-text');
if (!copiedText) {
copiedText = document.createElement('div');
copiedText.id = '\_\_growi-copied-text';
copiedText.style.cssText = `
font-size:0.9em;
color:#28a745;
margin-top:8px;
text-align:center;
`;
discountCodeDiv.parentNode.insertBefore(copiedText, discountCodeDiv.nextSibling);
}
copiedText.innerHTML = '✓ Discount applied!';
})
.catch(() => {
// Fallback for older browsers
const textArea = document.createElement('textarea');
textArea.value = discountCode.toUpperCase();
document.body.appendChild(textArea);
textArea.select();
document.execCommand('copy');
document.body.removeChild(textArea);
let copiedText = document.getElementById('\_\_growi-copied-text');
if (!copiedText) {
copiedText = document.createElement('div');
copiedText.id = '\_\_growi-copied-text';
copiedText.style.cssText = `
font-size:0.9em;
color:#28a745;
margin-top:8px;
text-align:center;
`;
discountCodeDiv.parentNode.insertBefore(copiedText, discountCodeDiv.nextSibling);
}
copiedText.innerHTML = '✓ Discount applied!';
});
};
// Insert the discount code div after the button
redeemBtn.parentNode.insertBefore(discountCodeDiv, redeemBtn.nextSibling);
}, 1500);
window.growiCookieUtils.setCookie('discount\_seen', affiliateId.toLowerCase());
};
}
}
async function showBanner(affiliateId, discountCode, customizationData = null) {
// Prevent duplicate banners
if (document.getElementById('\_\_growi-banner')) return;
// Fetch customization from API if not provided
const customization = customizationData || (await fetchCustomization(affiliateId));
// If no customization exists or banner not enabled, return
if (!customization || !customization.banner\_enabled) {
console.log('ℹ️ Banner is disabled or no customization available');
return;
}
// Merge customization with defaults
const config = { ...defaultCustomization, ...customization };
const affiliateName = window.growiCookieUtils.getCookie('affiliate\_name');
const discountValue = window.growiCookieUtils.getCookie('discount\_value');
const discountType = window.growiCookieUtils.getCookie('discount\_type');
const bannerHeading =
config.heading\_text ||
`${affiliateName ? decodeURIComponent(affiliateName) : 'We'} sent you ${discountValue}${
discountType === 'percentage' ? '%' : '$'
} off!`;
const bannerSubtext = config.body\_text || `Click below to redeem your discount code`;
const bannerButtonText = config.button\_text || 'Redeem Coupon';
const bannerButtonMarkup = config.hide\_button
? ''
: `<button id="\_\_growi-banner-btn" style="
padding: 14px 24px;
background-color: ${config.button\_color};
color: ${config.button\_text\_color};
border: none;
border-radius: 6px;
font-size: 16px;
font-weight: 600;
cursor: pointer;
white-space: nowrap;
flex-shrink: 0;
font-family: -apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif;
transition: opacity 0.2s;
">
${bannerButtonText}
</button>`;
// Create banner element
const banner = document.createElement('div');
banner.id = '\_\_growi-banner';
banner.style.cssText = `
display: flex;
align-items: center;
justify-content: space-between;
padding: 16px 20px;
background-color: ${config.background\_color};
color: ${config.text\_color};
position: fixed;
top: 0;
left: 0;
right: 0;
width: 100%;
z-index: 9997;
box-shadow: 0 2px 8px rgba(0,0,0,0.1);
border-bottom: 1px solid rgba(0,0,0,0.08);
font-family: -apple-system, Inter, BlinkMacSystemFont, Segoe UI, Roboto,
Helvetica Neue, Arial, Noto Sans, sans-serif;
gap: 20px;
box-sizing: border-box;
`;
banner.innerHTML = `
<div style="display: flex; align-items: center; gap: 15px; flex: 1;">
<div style="font-size: 40px; line-height: 1; flex-shrink: 0;">
${config.emoji || '🎉'}
</div>
<div style="flex: 1; min-width: 0;">
<div style="font-size: 18px; font-weight: 700; color: ${config.text\_color}; margin-bottom: 4px; line-height: 1.3;">
${bannerHeading}
</div>
<div style="font-size: 14px; color: ${config.text\_color}; opacity: 0.7; line-height: 1.4;">
${bannerSubtext}
</div>
</div>
</div>
${bannerButtonMarkup}
<button id="\_\_growi-banner-close" style="
background: transparent;
border: none;
color: ${config.text\_color};
cursor: pointer;
padding: 8px;
display: flex;
align-items: center;
flex-shrink: 0;
opacity: 0.6;
transition: opacity 0.2s;
">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
</svg>
</button>
`;
// Add responsive styles and hover effects
const bannerStyles = document.createElement('style');
bannerStyles.textContent = `
#\_\_growi-banner-btn:hover {
opacity: 0.9;
}
#\_\_growi-banner-close:hover {
opacity: 1;
}
@media (max-width: 768px) {
#\_\_growi-banner {
flex-direction: column;
align-items: stretch !important;
padding: 16px;
width: 100%;
}
#\_\_growi-banner > div:first-child {
margin-bottom: 12px;
}
#\_\_growi-banner-btn {
width: 100%;
}
#\_\_growi-banner-close {
position: absolute;
top: 16px;
right: 16px;
}
}
`;
document.head.appendChild(bannerStyles);
// Append to body
document.body.appendChild(banner);
// Add body padding to prevent content from being hidden behind banner
const originalPaddingTop = document.body.style.paddingTop;
// Wait for banner to render to get actual height
setTimeout(() => {
const bannerBottom = banner.getBoundingClientRect().bottom;
document.body.style.paddingTop = `${bannerBottom}px`;
// Push down any existing sticky announcement bars so they appear below our banner
const stickyAnnouncementBars = document.querySelectorAll(
'[class\*="announcement-bar"], [class\*="announcement\_bar"], [id\*="announcement-bar"]'
);
stickyAnnouncementBars.forEach((el) => {
const style = getComputedStyle(el);
if (style.position === 'sticky') {
el.style.top = `${bannerBottom}px`;
}
});
}, 0);
// Store original padding for cleanup
banner.dataset.originalPadding = originalPaddingTop;
// Button click handler - always copy code to clipboard, and optionally open modal
const bannerBtn = document.getElementById('\_\_growi-banner-btn');
if (bannerBtn) {
bannerBtn.onclick = () => {
const discountCode = window.growiCookieUtils.getCookie('discount\_code');
const affiliateName = window.growiCookieUtils.getCookie('affiliate\_name');
const discountType = window.growiCookieUtils.getCookie('discount\_type');
const discountValue = window.growiCookieUtils.getCookie('discount\_value');
if (discountCode && discountValue) {
// Always copy discount code to clipboard
const originalText = bannerBtn.innerHTML;
navigator.clipboard
.writeText(discountCode.toUpperCase())
.then(() => {
bannerBtn.innerHTML = '✓ Discount applied!';
bannerBtn.style.backgroundColor = '#28a745';
setTimeout(() => {
bannerBtn.innerHTML = originalText;
bannerBtn.style.backgroundColor = config.button\_color;
}, 2000);
})
.catch(() => {
// Fallback for older browsers
const textArea = document.createElement('textarea');
textArea.value = discountCode.toUpperCase();
textArea.style.position = 'fixed';
textArea.style.opacity = '0';
document.body.appendChild(textArea);
textArea.select();
document.execCommand('copy');
document.body.removeChild(textArea);
bannerBtn.innerHTML = '✓ Discount applied!';
bannerBtn.style.backgroundColor = '#28a745';
setTimeout(() => {
bannerBtn.innerHTML = originalText;
bannerBtn.style.backgroundColor = config.button\_color;
}, 2000);
});
// Additionally show modal if enabled
if (config.popup\_enabled) {
showDiscountModalV2(discountCode, affiliateName, discountValue, discountType, affiliateId);
}
}
};
}
// Close button handler
document.getElementById('\_\_growi-banner-close').onclick = () => {
// Restore original padding
const originalPadding = banner.dataset.originalPadding || '';
document.body.style.paddingTop = originalPadding;
banner.remove();
// Store in cookie that banner was dismissed
window.growiCookieUtils.setCookie('banner\_dismissed', affiliateId.toLowerCase(), 1); // 1 day
};
}
// ---- PAGE VIEW (exact referrer only) ----
function hasFiredPageView(visitorUid) {
const key = `growi\_pv\_sent::${visitorUid || 'anon'}::${location.pathname}`;
try {
if (sessionStorage.getItem(key)) return true;
} catch {}
if (window.growiCookieUtils) {
const ck = window.growiCookieUtils.getCookie(encodeURIComponent(key));
if (ck === '1') return true;
}
return false;
}
function markFiredPageView(visitorUid) {
const key = `growi\_pv\_sent::${visitorUid || 'anon'}::${location.pathname}`;
try {
sessionStorage.setItem(key, '1');
} catch {}
// ~30 minutes lock across tabs
window.growiCookieUtils && window.growiCookieUtils.setCookie(encodeURIComponent(key), '1', 0.02);
}
async function sendOneTimePageView(externalId) {
console.log('sendOneTimePageView', externalId);
if (!window.growiCookieUtils) return;
console.log('sendOneTimePageView1', externalId);
if (!externalId) return;
const affiliateId = window.growiCookieUtils.getCookie('growi\_affiliate\_id');
const visitorUid = window.growiCookieUtils.getCookie('growi\_visitor\_uid');
if (!affiliateId || affiliateId === 'null') return; // keep your current rule
console.log('sendOneTimePageView2', affiliateId);
if (hasFiredPageView(visitorUid)) return;
console.log('sendOneTimePageView3', visitorUid);
markFiredPageView(visitorUid);
// EXACT referrer only
const referrerRaw = document.referrer || null;
let referrerHost = null;
try {
referrerHost = referrerRaw ? new URL(referrerRaw).host : null;
} catch {}
// Referrer captured at script-execute time, before any same-host nav
// could blank document.referrer. Survives pushState / SPA-style nav
// inside in-app browsers.
const referrerInitialRaw =
(typeof window !== 'undefined' && typeof window.\_\_growi\_initial\_referrer !== 'undefined'
? window.\_\_growi\_initial\_referrer
: null) || null;
let referrerInitialHost = null;
try {
referrerInitialHost = referrerInitialRaw ? new URL(referrerInitialRaw).host : null;
} catch {}
// Get UTM parameters for Meta/Facebook ad tracking
const utmParams = window.growiCookieUtils.getUtmParams ? window.growiCookieUtils.getUtmParams() : {};
// Check if traffic is from Facebook/Meta based on utm\_source
const isFacebookSource = utmParams.utm\_source &&
['fb', 'facebook', 'meta'].includes(utmParams.utm\_source.toLowerCase());
// Click IDs + first-touch snapshot for paid-search fraud detection
const clickIds = window.growiCookieUtils.getClickIds ? window.growiCookieUtils.getClickIds() : {};
const firstTouch = window.growiCookieUtils.getFirstTouch ? window.growiCookieUtils.getFirstTouch() : null;
// In-app-browser / platform inference from UA. Always safe to call —
// returns { platform: 'browser', in\_app\_browser: false, ... } when
// nothing matches.
const clientPlatform = window.growiCookieUtils.detectClientPlatform
? window.growiCookieUtils.detectClientPlatform()
: { platform: 'browser', in\_app\_browser: false, user\_agent: '', is\_mobile: false };
// Prefer the value stamped onto first\_touch (computed when the affiliate
// cookie was set / backfilled — most accurate). Fall back to recomputing
// live so payloads without a first\_touch still carry signal.
let inferredSource = (firstTouch && firstTouch.inferred\_source) || null;
if (!inferredSource) {
if (clientPlatform && clientPlatform.platform && clientPlatform.platform !== 'browser') {
inferredSource = clientPlatform.platform;
} else if (referrerHost) {
inferredSource = referrerHost;
} else if (clickIds.gclid) {
inferredSource = 'google\_ads';
} else if (clickIds.msclkid) {
inferredSource = 'bing\_ads';
} else if (clickIds.fbclid) {
inferredSource = 'facebook';
} else if (clickIds.ttclid) {
inferredSource = 'tiktok';
} else {
inferredSource = 'direct';
}
}
const event = {
name: 'page\_viewed',
id: (crypto.randomUUID && crypto.randomUUID()) || `${Date.now()}-${Math.random().toString(16).slice(2)}`,
timestamp: new Date().toISOString(),
data: {
title: document.title || null,
path: location.pathname,
url: location.href,
referrer\_raw: referrerRaw,
referrer\_host: referrerHost,
referrer\_initial\_raw: referrerInitialRaw,
referrer\_initial\_host: referrerInitialHost,
utm\_source: utmParams.utm\_source || null,
utm\_medium: utmParams.utm\_medium || null,
utm\_campaign: utmParams.utm\_campaign || null,
utm\_content: utmParams.utm\_content || null,
utm\_term: utmParams.utm\_term || null,
utm\_id: utmParams.utm\_id || null,
// Meta Ad ID (only set if utm\_source is fb/facebook/meta)
meta\_ad\_id: isFacebookSource ? (utmParams.utm\_content || null) : null,
click\_ids: clickIds,
first\_touch: firstTouch,
inferred\_source: inferredSource,
client\_platform: clientPlatform,
},
clientId: visitorUid,
};
const body = {
tracking\_event: {
event\_name: event.name,
occurred\_at: event.timestamp,
visitor\_uid: visitorUid,
event\_data: {
pageEventId: event.id,
timeStamp: event.timestamp,
data: { ...event.data, clientId: event.clientId },
},
},
campaign\_affiliate\_id: affiliateId,
external\_id: `gid://shopify/Shop/${externalId}`,
conversion\_platform: 'shopify',
};
// Optional server dedupe
const idempKey = `${visitorUid || 'anon'}::${location.pathname}::${Math.floor(Date.now() / 60000)}`;
try {
await fetch('https://api.growi.io/api/v1/tracking\_events', {
method: 'POST',
headers: {
'Content-Type': 'application/json',
'Idempotency-Key': idempKey,
},
body: JSON.stringify(body),
});
} catch (err) {
console.warn('page\_viewed send failed', err);
}
}
function waitForUrlParams(retries = 10, delay = 200) {
// Check if URL has any parameters yet
const hasParams = window.location.search.length > 0;
const affiliateParam =
new URLSearchParams(window.location.search).get('a') ||
new URLSearchParams(window.location.search).get('snowball') ||
new URLSearchParams(window.location.search).get('growi');
// If we found affiliate params or exhausted retries, proceed
if (affiliateParam || retries <= 0 || hasParams) {
console.log(`✅ URL stabilized after ${10 - retries} attempts. Affiliate param:`, affiliateParam);
initializeAffiliate();
return;
}
// Wait and retry - Instagram WebView needs time to stabilize
console.log(`⏳ Waiting for URL params to stabilize... (${retries} retries left)`);
setTimeout(() => waitForUrlParams(retries - 1, delay), delay);
}
function waitForUtils(retries = 5) {
console.log(`🔍 [WAIT-FOR-UTILS] Attempt ${6 - retries}/5 - Checking for window.growiCookieUtils...`);
console.log(
`🔍 [WAIT-FOR-UTILS] window.growiCookieUtils exists?`,
typeof window.growiCookieUtils !== 'undefined'
);
console.log(`🔍 [WAIT-FOR-UTILS] Document readyState:`, document.readyState);
console.log(`🔍 [WAIT-FOR-UTILS] Timestamp:`, new Date().toISOString());
if (window.growiCookieUtils) {
console.log('✅ [WAIT-FOR-UTILS] Cookie utils found! Available methods:', Object.keys(window.growiCookieUtils));
// Don't immediately read params - wait for URL to stabilize first
waitForUrlParams();
} else if (retries > 0) {
console.log(`⏳ [WAIT-FOR-UTILS] Not found yet, retrying in 100ms... (${retries} retries left)`);
setTimeout(() => waitForUtils(retries - 1), 100);
} else {
console.error('❌ [WAIT-FOR-UTILS] Growi cookie utilities not loaded after 5 retries (500ms total)');
console.error('❌ [WAIT-FOR-UTILS] All window properties:', Object.keys(window));
console.error('❌ [WAIT-FOR-UTILS] Check if cookie-utils.js is loading correctly');
}
}
function initializeAffiliate() {
console.log('🎯 [INIT-AFFILIATE] initializeAffiliate() called');
console.log(
'🎯 [INIT-AFFILIATE] window.growiCookieUtils exists?',
typeof window.growiCookieUtils !== 'undefined'
);
if (!window.growiCookieUtils) {
console.error('❌ [INIT-AFFILIATE] Cookie utils not available - CANNOT PROCEED');
console.error('❌ [INIT-AFFILIATE] This usually means cookie-utils.js failed to load or execute');
return;
}
console.log('✅ [INIT-AFFILIATE] Cookie utils available, proceeding...');
// Now read affiliate params after URL has stabilized
const urlAffiliateId =
new URLSearchParams(window.location.search).get('a') ||
new URLSearchParams(window.location.search).get('snowball') ||
new URLSearchParams(window.location.search).get('growi');
// Get affiliate info from cookies
const cookieInfo = window.growiCookieUtils.manageAffiliateCookies();
// Determine which affiliate ID to use (URL param takes precedence)
const affiliateId = urlAffiliateId || cookieInfo.affiliateId;
const visitorUid = cookieInfo.visitorUid;
console.log('🔍 Final affiliate detection:', {
urlAffiliateId,
cookieAffiliateId: cookieInfo.affiliateId,
finalAffiliateId: affiliateId,
});
// If we have affiliate data from either source, update the cart
if (affiliateId && visitorUid) {
// Get UTM parameters to pass to order
const utmParams = window.growiCookieUtils.getUtmParams ? window.growiCookieUtils.getUtmParams() : {};
// Check if traffic is from Facebook/Meta based on utm\_source
const isFacebookSource = utmParams.utm\_source &&
['fb', 'facebook', 'meta'].includes(utmParams.utm\_source.toLowerCase());
// Build cart attributes
const cartAttributes = {
\_\_growi\_affiliate\_id: affiliateId,
\_\_growi\_visitor\_uid: visitorUid,
};
if (utmParams.utm\_source) cartAttributes.\_\_growi\_utm\_source = utmParams.utm\_source;
if (utmParams.utm\_medium) cartAttributes.\_\_growi\_utm\_medium = utmParams.utm\_medium;
if (utmParams.utm\_campaign) cartAttributes.\_\_growi\_utm\_campaign = utmParams.utm\_campaign;
if (utmParams.utm\_content) cartAttributes.\_\_growi\_utm\_content = utmParams.utm\_content;
if (utmParams.utm\_term) cartAttributes.\_\_growi\_utm\_term = utmParams.utm\_term;
if (utmParams.utm\_id) cartAttributes.\_\_growi\_utm\_id = utmParams.utm\_id;
if (utmParams.campaign\_id) cartAttributes.\_\_growi\_campaign\_id = utmParams.campaign\_id;
if (utmParams.user\_id) cartAttributes.\_\_growi\_user\_id = utmParams.user\_id;
if (utmParams.campaign\_affiliate\_id) cartAttributes.\_\_growi\_campaign\_affiliate\_id = utmParams.campaign\_affiliate\_id;
if (utmParams.asset\_id) cartAttributes.\_\_growi\_asset\_id = utmParams.asset\_id;
if (isFacebookSource && utmParams.utm\_content) {
cartAttributes.\_\_growi\_meta\_ad\_id = utmParams.utm\_content;
}
fetch('/cart/update.js', {
method: 'POST',
headers: {
'Content-Type': 'application/json',
},
body: JSON.stringify({
attributes: cartAttributes,
}),
})
.then((res) => {
// Extract x-shopid from response headers
const externalId = res.headers.get('x-shopid');
console.log('🏪 Shop ID extracted from headers:', externalId);
return res.json().then((data) => ({ data, externalId }));
})
.then(({ data, externalId }) => {
console.log('✅ Cart attributes updated with affiliate & visitor ID', data);
// --- Discount code logic start ---
// Only fetch if we have an affiliateId and no discount\_code cookie
// Only fetch if we have an affiliateId and no discount\_code cookie
const discountCode = window.growiCookieUtils.getCookie('discount\_code');
const affiliateName = window.growiCookieUtils.getCookie('affiliate\_name');
const discountType = window.growiCookieUtils.getCookie('discount\_type');
const discountValue = window.growiCookieUtils.getCookie('discount\_value');
const campaignType = window.growiCookieUtils.getCookie('campaign\_type');
const discountSeen = window.growiCookieUtils.getCookie('discount\_seen');
const isDiscountSeen = discountSeen && discountSeen === `${affiliateId}`.toLowerCase();
console.log('Test', affiliateId, discountCode, affiliateId !== 'null', externalId);
if (affiliateId && !!discountCode && affiliateId !== 'null' && isDiscountSeen) {
const bannerDismissed = window.growiCookieUtils.getCookie('banner\_dismissed');
const isBannerDismissed = bannerDismissed && bannerDismissed === `${affiliateId}`.toLowerCase();
if (!isBannerDismissed) {
// Check if banner is enabled before showing
fetchCustomization(affiliateId).then((customization) => {
if (customization && customization.banner\_enabled) {
showBanner(affiliateId, discountCode, customization);
}
});
}
sendOneTimePageView(externalId);
} else if (
affiliateId &&
(!discountCode || (!!discountCode && !isDiscountSeen)) &&
affiliateId !== 'null'
) {
const currentUrl = window.location.href;
fetch(
`https://api.growi.io/api/v1/campaign\_affiliates/${encodeURIComponent(
affiliateId
)}/discount\_code?url=${encodeURIComponent(currentUrl)}`,
{
method: 'GET',
headers: {
'Content-Type': 'application/json',
},
}
)
.then((response) => {
if (!response.ok) throw new Error('Network response was not ok');
return response.json();
})
.then((data) => {
if (data.success) {
cookieDuration = data.cookie\_duration;
if (!!cookieDuration) {
updateAffiliateCookieDuration(cookieDuration);
console.log('✅ Affiliate cookie duration updated:', cookieDuration);
}
}
if (data.success && data.discount\_code) {
// Set discount\_code cookie for 30 days
window.growiCookieUtils.setCookie('discount\_code', data.discount\_code, 30);
// Set new response format cookies
if (data.affiliate\_name) {
window.growiCookieUtils.setCookie('affiliate\_name', data.affiliate\_name, 30);
}
if (data.discount\_type) {
window.growiCookieUtils.setCookie('discount\_type', data.discount\_type, 30);
}
if (data.discount\_value) {
window.growiCookieUtils.setCookie('discount\_value', data.discount\_value, 30);
}
if (data.campaign\_type) {
window.growiCookieUtils.setCookie('campaign\_type', data.campaign\_type, 30);
}
console.log('✅ Discount code cookies set:', data.discount\_code);
// Show discount modal only for ambassador programs and if not seen yet
const discountSeen = window.growiCookieUtils.getCookie('discount\_seen');
const isDiscountSeen = discountSeen && discountSeen === `${affiliateId}`.toLowerCase();
if (!isDiscountSeen) {
if (data.is\_v2) {
showDiscountModalV2(
data.discount\_code,
data.affiliate\_name,
data.discount\_value,
data.discount\_type,
affiliateId
);
} else {
showDiscountModal(
data.discount\_code,
data.affiliate\_name,
data.discount\_value,
data.discount\_type,
affiliateId
);
}
} else {
// If modal was already seen, show banner instead (if not dismissed)
const bannerDismissed = window.growiCookieUtils.getCookie('banner\_dismissed');
const isBannerDismissed = bannerDismissed && bannerDismissed === `${affiliateId}`.toLowerCase();
if (!isBannerDismissed) {
// Check if banner is enabled before showing
fetchCustomization(affiliateId).then((customization) => {
if (customization && customization.banner\_enabled) {
showBanner(affiliateId, data.discount\_code, customization);
}
});
}
}
}
})
.catch((error) => {
console.error('There has been a problem with your fetch operation:', error);
});
}
// --- Discount code logic end ---
sendOneTimePageView(externalId);
})
.catch((err) => {
console.error('❌ Failed to update cart attributes', err);
});
} else {
console.log('ℹ️ No affiliate data to process');
}
}
// Start the process - wait for utils first, then URL stability
console.log('🚀 [GROWI-EMBED] Starting waitForUtils() immediately...');
console.log('🚀 [GROWI-EMBED] Current timestamp:', new Date().toISOString());
waitForUtils();
// Also try on window.load as a fallback for very slow WebViews
window.addEventListener('load', () => {
setTimeout(() => {
console.log('🔄 [WINDOW-LOAD] Window load backup trigger fired (500ms after window.load)');
console.log('🔄 [WINDOW-LOAD] window.growiCookieUtils exists?', typeof window.growiCookieUtils !== 'undefined');
initializeAffiliate();
}, 500);
});
})();


!function(){if(!window.klaviyo){window.\_klOnsite=window.\_klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window.\_klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window.\_klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window.\_klOnsite).push.apply(n,arguments)}}}}();

window.klaviyoReviewsProductDesignMode = false


{
const getPage = () => "cart";
const getSearchTerms = () => "";
const getCart = () => ({"note":null,"attributes":{},"original\_total\_price":0,"total\_price":0,"total\_discount":0,"total\_weight":0.0,"item\_count":0,"items":[],"requires\_shipping":false,"currency":"USD","items\_subtotal\_price":0,"cart\_level\_discount\_applications":[],"checkout\_charge\_amount":0});
const getCollection = () => ({
list\_id: "",
category: null || null,
currency: "USD",
});
const getCustomer = () => ({
name: [null, null].filter(Boolean).join(" ") || null,
externalCustomerId: "",
email: "",
phone: "",
firstName: null,
lastName: null,
lifetimeValue: null,
orderCount: null,
address: {
street: null,
city: null,
state: null,
stateCode: null,
postalCode: "",
country: "",
province: "",
countryCode: "",
}
});
const getProduct = () => ({
productId: "",
variant: "",
variantId: "",
variantName: null,
sku: null,
brand: null,
category: null || null,
name: null,
price: 0.0,
url: "",
currency: "USD",
collections: [],
tags: null
});
const getProducts = () => {
var cartItemsJson = [];
return cartItemsJson.map((item, index) => {
return {
productId: item.id.toString(),
sku: item.sku,
quantity: item.quantity,
variant: item.variant\_id.toString(),
variantId: item.variant\_id.toString(),
variantName: item.variant\_title,
name: item.title,
price: item.final\_price / 100,
brand: item.vendor,
position: index + 1,
url: item.url,
imageUrl: item.image,
}
});
};
window.addEventListener('fueled-load', () => {
window.Fueled.setDataLayerItem('page', getPage());
window.Fueled.setDataLayerItem('cart', getCart());
window.Fueled.setDataLayerItem('products', getProducts());
});
}





window.jdgmSettings={"pagination":5,"disable\_web\_reviews":false,"coupon\_receiving\_condition":"","coupon\_value\_type":"percentage","coupon\_value\_percentage":10,"coupon\_value\_fixed\_amount":0,"coupon\_discount\_type":"single","coupon\_tier\_text\_enabled":false,"coupon\_tier\_text\_percentage":10,"coupon\_tier\_text\_fixed\_amount":0,"coupon\_tier\_photo\_enabled":false,"coupon\_tier\_photo\_percentage":10,"coupon\_tier\_photo\_fixed\_amount":0,"coupon\_tier\_video\_enabled":false,"coupon\_tier\_video\_percentage":10,"coupon\_tier\_video\_fixed\_amount":0,"enable\_coupons":false,"badge\_no\_review\_text":"No reviews","badge\_n\_reviews\_text":"({{ n }} reviews)","badge\_star\_color":"#101010","hide\_badge\_preview\_if\_no\_reviews":true,"badge\_hide\_text":false,"enforce\_center\_preview\_badge":false,"widget\_title":"{{ product\_name }} Reviews","widget\_open\_form\_text":"Write a review","widget\_close\_form\_text":"Cancel review","widget\_refresh\_page\_text":"Refresh page","widget\_summary\_text":"Based on {{ number\_of\_reviews }} customer review/reviews","widget\_no\_review\_text":"Be the first to write a review","widget\_name\_field\_text":"Display name","widget\_verified\_name\_field\_text":"Verified Name (public)","widget\_name\_placeholder\_text":"Display name","widget\_required\_field\_error\_text":"This field is required.","widget\_email\_field\_text":"Email address","widget\_verified\_email\_field\_text":"Verified Email (private, can not be edited)","widget\_email\_placeholder\_text":"Your email address","widget\_email\_field\_error\_text":"Please enter a valid email address.","widget\_rating\_field\_text":"Choose your star rating below:","widget\_review\_title\_field\_text":"Review Title","widget\_review\_title\_placeholder\_text":"Give your review a title","widget\_review\_body\_field\_text":"Review content","widget\_review\_body\_placeholder\_text":"Start writing here...","widget\_pictures\_field\_text":"Picture/Video (optional)","widget\_submit\_review\_text":"SUBMIT REVIEW","widget\_submit\_verified\_review\_text":"SUBMIT REVIEW","widget\_submit\_success\_msg\_with\_auto\_publish":"Thank you! Please refresh the page in a few moments to see your review. You can remove or edit your review by logging into \u003ca href='https://judge.me/login' target='\_blank' rel='nofollow noopener'\u003eJudge.me\u003c/a\u003e","widget\_submit\_success\_msg\_no\_auto\_publish":"Thank you! Your review will be published as soon as it is approved by the shop admin. You can remove or edit your review by logging into \u003ca href='https://judge.me/login' target='\_blank' rel='nofollow noopener'\u003eJudge.me\u003c/a\u003e","widget\_show\_default\_reviews\_out\_of\_total\_text":"Showing {{ n\_reviews\_shown }} out of {{ n\_reviews }} reviews.","widget\_show\_all\_link\_text":"Show all","widget\_show\_less\_link\_text":"Show less","widget\_author\_said\_text":"{{ reviewer\_name }} said:","widget\_days\_text":"{{ n }} days ago","widget\_weeks\_text":"{{ n }} week/weeks ago","widget\_months\_text":"{{ n }} month/months ago","widget\_years\_text":"{{ n }} year/years ago","widget\_yesterday\_text":"Yesterday","widget\_today\_text":"Today","widget\_replied\_text":"\u003e\u003e {{ shop\_name }}:","widget\_read\_more\_text":"Read more","widget\_reviewer\_name\_as\_initial":"last\_initial","widget\_rating\_filter\_color":"#101010","widget\_rating\_filter\_see\_all\_text":"See all reviews","widget\_sorting\_most\_recent\_text":"Most Recent","widget\_sorting\_highest\_rating\_text":"Highest Rating","widget\_sorting\_lowest\_rating\_text":"Lowest Rating","widget\_sorting\_with\_pictures\_text":"Only Pictures","widget\_sorting\_most\_helpful\_text":"Most Helpful","widget\_open\_question\_form\_text":"Ask a question","widget\_reviews\_subtab\_text":"Reviews","widget\_questions\_subtab\_text":"Questions","widget\_question\_label\_text":"Question","widget\_answer\_label\_text":"Answer","widget\_question\_placeholder\_text":"Write your question here","widget\_submit\_question\_text":"Submit Question","widget\_question\_submit\_success\_text":"Thank you for your question! We will notify you once it gets answered.","widget\_star\_color":"#101010","verified\_badge\_text":"Verified","verified\_badge\_bg\_color":"#101010","verified\_badge\_text\_color":"#F9F8F6","verified\_badge\_placement":"left-of-reviewer-name","widget\_review\_max\_height":"","widget\_hide\_border":true,"widget\_social\_share":false,"widget\_thumb":true,"widget\_review\_location\_show":true,"widget\_location\_format":"country\_iso\_code","all\_reviews\_include\_out\_of\_store\_products":true,"all\_reviews\_out\_of\_store\_text":"(out of store)","all\_reviews\_pagination":100,"all\_reviews\_product\_name\_prefix\_text":"about","enable\_review\_pictures":true,"enable\_question\_anwser":true,"widget\_theme":"","review\_date\_format":"mm/dd/yy","default\_sort\_method":"highest-rating","widget\_product\_reviews\_subtab\_text":"Product Reviews","widget\_shop\_reviews\_subtab\_text":"Shop Reviews","widget\_other\_products\_reviews\_text":"Reviews for other products","widget\_store\_reviews\_subtab\_text":"Store reviews","widget\_product\_variant\_reference\_text":"Review for","widget\_no\_store\_reviews\_text":"This store hasn't received any reviews yet","widget\_web\_restriction\_product\_reviews\_text":"This product hasn't received any reviews yet","widget\_no\_items\_text":"No items found","widget\_show\_more\_text":"Show more","widget\_write\_a\_store\_review\_text":"Write a Store Review","widget\_product\_and\_store\_reviews\_text":"Product and store reviews","widget\_reviews\_in\_collection\_text":"Reviews in this collection","widget\_other\_languages\_heading":"Reviews in Other Languages","widget\_translate\_review\_text":"Translate review to {{ language }}","widget\_translating\_review\_text":"Translating...","widget\_show\_original\_translation\_text":"Show original ({{ language }})","widget\_translate\_review\_failed\_text":"Review couldn't be translated.","widget\_translate\_review\_retry\_text":"Retry","widget\_translate\_review\_try\_again\_later\_text":"Try again later","show\_product\_url\_for\_grouped\_product":false,"widget\_sorting\_pictures\_first\_text":"Pictures First","show\_pictures\_on\_all\_rev\_page\_mobile":false,"show\_pictures\_on\_all\_rev\_page\_desktop":false,"floating\_tab\_hide\_mobile\_install\_preference":false,"floating\_tab\_button\_name":"★ Reviews","floating\_tab\_title":"Let customers speak for us","floating\_tab\_button\_color":"","floating\_tab\_button\_background\_color":"","floating\_tab\_url":"","floating\_tab\_url\_enabled":false,"floating\_tab\_tab\_style":"text","all\_reviews\_text\_badge\_text":"Customers rate us {{ shop.metafields.judgeme.all\_reviews\_rating | round: 1 }}/5 based on {{ shop.metafields.judgeme.all\_reviews\_count }} reviews.","all\_reviews\_text\_badge\_text\_branded\_style":"{{ shop.metafields.judgeme.all\_reviews\_rating | round: 1 }} out of 5 stars based on {{ shop.metafields.judgeme.all\_reviews\_count }} reviews","is\_all\_reviews\_text\_badge\_a\_link":false,"show\_stars\_for\_all\_reviews\_text\_badge":true,"all\_reviews\_text\_badge\_url":"","all\_reviews\_text\_style":"text","all\_reviews\_text\_color\_style":"judgeme\_brand\_color","all\_reviews\_text\_color":"#108474","all\_reviews\_text\_show\_jm\_brand":true,"featured\_carousel\_show\_header":true,"featured\_carousel\_title":"Let customers speak for us","testimonials\_carousel\_title":"Customers are saying","videos\_carousel\_title":"Real customer stories","cards\_carousel\_title":"Customers are saying","featured\_carousel\_count\_text":"from {{ n }} reviews","featured\_carousel\_add\_link\_to\_all\_reviews\_page":false,"featured\_carousel\_url":"","featured\_carousel\_show\_images":true,"featured\_carousel\_autoslide\_interval":5,"featured\_carousel\_arrows\_on\_the\_sides":false,"featured\_carousel\_height":250,"featured\_carousel\_width":80,"featured\_carousel\_image\_size":0,"featured\_carousel\_image\_height":250,"featured\_carousel\_arrow\_color":"#eeeeee","verified\_count\_badge\_style":"vintage","verified\_count\_badge\_orientation":"horizontal","verified\_count\_badge\_color\_style":"judgeme\_brand\_color","verified\_count\_badge\_color":"#108474","is\_verified\_count\_badge\_a\_link":false,"verified\_count\_badge\_url":"","verified\_count\_badge\_show\_jm\_brand":true,"widget\_rating\_preset\_default":5,"widget\_first\_sub\_tab":"product-reviews","widget\_show\_histogram":true,"widget\_histogram\_use\_custom\_color":true,"widget\_pagination\_use\_custom\_color":true,"widget\_star\_use\_custom\_color":true,"widget\_verified\_badge\_use\_custom\_color":false,"widget\_write\_review\_use\_custom\_color":false,"picture\_reminder\_submit\_button":"Upload Pictures","enable\_review\_videos":true,"mute\_video\_by\_default":false,"widget\_sorting\_videos\_first\_text":"Videos First","widget\_review\_pending\_text":"Pending","featured\_carousel\_items\_for\_large\_screen":3,"social\_share\_options\_order":"Facebook,Twitter","remove\_microdata\_snippet":true,"disable\_json\_ld":false,"enable\_json\_ld\_products":false,"preview\_badge\_show\_question\_text":false,"preview\_badge\_no\_question\_text":"No questions","preview\_badge\_n\_question\_text":"{{ number\_of\_questions }} question/questions","qa\_badge\_show\_icon":false,"qa\_badge\_position":"same-row","remove\_judgeme\_branding":true,"widget\_add\_search\_bar":true,"widget\_search\_bar\_placeholder":"Search","widget\_sorting\_verified\_only\_text":"Verified only","featured\_carousel\_theme":"default","featured\_carousel\_show\_rating":true,"featured\_carousel\_show\_title":true,"featured\_carousel\_show\_body":true,"featured\_carousel\_show\_date":false,"featured\_carousel\_show\_reviewer":true,"featured\_carousel\_show\_product":false,"featured\_carousel\_header\_background\_color":"#108474","featured\_carousel\_header\_text\_color":"#ffffff","featured\_carousel\_name\_product\_separator":"reviewed","featured\_carousel\_full\_star\_background":"#108474","featured\_carousel\_empty\_star\_background":"#dadada","featured\_carousel\_vertical\_theme\_background":"#f9fafb","featured\_carousel\_verified\_badge\_enable":false,"featured\_carousel\_verified\_badge\_color":"#108474","featured\_carousel\_border\_style":"round","featured\_carousel\_review\_line\_length\_limit":3,"featured\_carousel\_more\_reviews\_button\_text":"Read more reviews","featured\_carousel\_view\_product\_button\_text":"View product","all\_reviews\_page\_load\_reviews\_on":"button\_click","all\_reviews\_page\_load\_more\_text":"Load More Reviews","disable\_fb\_tab\_reviews":false,"enable\_ajax\_cdn\_cache":false,"widget\_public\_name\_text":"ie.","default\_reviewer\_name":"John Smith","default\_reviewer\_name\_has\_non\_latin":true,"widget\_reviewer\_anonymous":"Anonymous","medals\_widget\_title":"Judge.me Review Medals","medals\_widget\_background\_color":"#f9fafb","medals\_widget\_position":"footer\_all\_pages","medals\_widget\_border\_color":"#f9fafb","medals\_widget\_verified\_text\_position":"left","medals\_widget\_use\_monochromatic\_version":false,"medals\_widget\_elements\_color":"#108474","show\_reviewer\_avatar":false,"widget\_invalid\_yt\_video\_url\_error\_text":"Not a YouTube video URL","widget\_max\_length\_field\_error\_text":"Please enter no more than {0} characters.","widget\_show\_country\_flag":false,"widget\_show\_collected\_via\_shop\_app":true,"widget\_verified\_by\_shop\_badge\_style":"light","widget\_verified\_by\_shop\_text":"Verified by Shop","widget\_show\_photo\_gallery":true,"widget\_load\_with\_code\_splitting":true,"widget\_ugc\_install\_preference":false,"widget\_ugc\_title":"Made by us, Shared by you","widget\_ugc\_subtitle":"Tag us to see your picture featured in our page","widget\_ugc\_arrows\_color":"#ffffff","widget\_ugc\_primary\_button\_text":"Buy Now","widget\_ugc\_primary\_button\_background\_color":"#108474","widget\_ugc\_primary\_button\_text\_color":"#ffffff","widget\_ugc\_primary\_button\_border\_width":"0","widget\_ugc\_primary\_button\_border\_style":"none","widget\_ugc\_primary\_button\_border\_color":"#108474","widget\_ugc\_primary\_button\_border\_radius":"25","widget\_ugc\_secondary\_button\_text":"Load More","widget\_ugc\_secondary\_button\_background\_color":"#ffffff","widget\_ugc\_secondary\_button\_text\_color":"#108474","widget\_ugc\_secondary\_button\_border\_width":"2","widget\_ugc\_secondary\_button\_border\_style":"solid","widget\_ugc\_secondary\_button\_border\_color":"#108474","widget\_ugc\_secondary\_button\_border\_radius":"25","widget\_ugc\_reviews\_button\_text":"View Reviews","widget\_ugc\_reviews\_button\_background\_color":"#ffffff","widget\_ugc\_reviews\_button\_text\_color":"#108474","widget\_ugc\_reviews\_button\_border\_width":"2","widget\_ugc\_reviews\_button\_border\_style":"solid","widget\_ugc\_reviews\_button\_border\_color":"#108474","widget\_ugc\_reviews\_button\_border\_radius":"25","widget\_ugc\_reviews\_button\_link\_to":"judgeme-reviews-page","widget\_ugc\_show\_post\_date":true,"widget\_ugc\_max\_width":"800","widget\_rating\_metafield\_value\_type":true,"widget\_primary\_color":"#101010","widget\_enable\_secondary\_color":true,"widget\_secondary\_color":"#F9F8F6","widget\_summary\_average\_rating\_text":"{{ average\_rating }} out of 5","widget\_media\_grid\_title":"Photos \u0026 Videos","widget\_media\_grid\_see\_more\_text":"See more","widget\_round\_style":false,"widget\_show\_product\_medals":false,"widget\_verified\_by\_judgeme\_text":"Verified by Judge.me","widget\_show\_store\_medals":true,"widget\_verified\_by\_judgeme\_text\_in\_store\_medals":"Verified by Judge.me","widget\_media\_field\_exceed\_quantity\_message":"Sorry, we can only accept {{ max\_media }} for one review.","widget\_media\_field\_exceed\_limit\_message":"{{ file\_name }} is too large, please select a {{ media\_type }} less than {{ size\_limit }}MB.","widget\_review\_submitted\_text":"Review Submitted!","widget\_question\_submitted\_text":"Question Submitted!","widget\_close\_form\_text\_question":"Cancel","widget\_write\_your\_answer\_here\_text":"Write your answer here","widget\_enabled\_branded\_link":true,"widget\_show\_collected\_by\_judgeme":true,"widget\_reviewer\_name\_color":"#101010","widget\_write\_review\_text\_color":"#F9F8F6","widget\_write\_review\_bg\_color":"#101010","widget\_collected\_by\_judgeme\_text":"collected by Judge.me","widget\_pagination\_type":"load\_more","widget\_load\_more\_text":"Load More","widget\_load\_more\_color":"#101010","widget\_full\_review\_text":"Full Review","widget\_read\_more\_reviews\_text":"Read More Reviews","widget\_read\_questions\_text":"Read Questions","widget\_questions\_and\_answers\_text":"Questions \u0026 Answers","widget\_verified\_by\_text":"Verified by","widget\_verified\_text":"Verified","widget\_number\_of\_reviews\_text":"{{ number\_of\_reviews }} reviews","widget\_back\_button\_text":"Back","widget\_next\_button\_text":"Next","widget\_custom\_forms\_filter\_button":"Filters","custom\_forms\_style":"vertical","widget\_show\_review\_information":false,"how\_reviews\_are\_collected":"How reviews are collected?","widget\_show\_review\_keywords":false,"widget\_gdpr\_statement":"How we use your data: We'll only contact you about the review you left, and only if necessary. By submitting your review, you agree to Judge.me's \u003ca href='https://judge.me/terms' target='\_blank' rel='nofollow noopener'\u003eterms\u003c/a\u003e, \u003ca href='https://judge.me/privacy' target='\_blank' rel='nofollow noopener'\u003eprivacy\u003c/a\u003e and \u003ca href='https://judge.me/content-policy' target='\_blank' rel='nofollow noopener'\u003econtent\u003c/a\u003e policies.","widget\_multilingual\_sorting\_enabled":false,"widget\_translate\_review\_content\_enabled":false,"widget\_translate\_review\_content\_method":"manual","popup\_widget\_review\_selection":"automatically\_with\_pictures","popup\_widget\_round\_border\_style":true,"popup\_widget\_show\_title":true,"popup\_widget\_show\_body":true,"popup\_widget\_show\_reviewer":false,"popup\_widget\_show\_product":true,"popup\_widget\_show\_pictures":true,"popup\_widget\_use\_review\_picture":true,"popup\_widget\_show\_on\_home\_page":true,"popup\_widget\_show\_on\_product\_page":true,"popup\_widget\_show\_on\_collection\_page":true,"popup\_widget\_show\_on\_cart\_page":true,"popup\_widget\_position":"bottom\_left","popup\_widget\_first\_review\_delay":5,"popup\_widget\_duration":5,"popup\_widget\_interval":5,"popup\_widget\_review\_count":5,"popup\_widget\_hide\_on\_mobile":true,"review\_snippet\_widget\_round\_border\_style":true,"review\_snippet\_widget\_card\_color":"#FFFFFF","review\_snippet\_widget\_text\_color":"#000000","review\_snippet\_widget\_lighter\_text\_color":"#7B7B7B","review\_snippet\_widget\_slider\_arrows\_background\_color":"#FFFFFF","review\_snippet\_widget\_slider\_arrows\_color":"#000000","review\_snippet\_widget\_star\_color":"#101010","show\_product\_variant":true,"all\_reviews\_product\_variant\_label\_text":"Variant: ","widget\_show\_verified\_branding":false,"widget\_ai\_summary\_title":"Customers say","widget\_ai\_summary\_disclaimer":"AI-powered review summary based on recent customer reviews","widget\_show\_ai\_summary":false,"widget\_show\_ai\_summary\_bg":false,"write\_review\_button\_visibility":"everyone","store\_summary\_widget\_heading":"Customers rate this store","store\_summary\_widget\_button\_text":"View customer reviews","store\_summary\_widget\_button\_theme\_text":"See AI reviews summary","widget\_show\_review\_title\_input":true,"redirect\_reviewers\_invited\_via\_email":"review\_widget","request\_store\_review\_after\_product\_review":false,"request\_review\_other\_products\_in\_order":false,"review\_form\_color\_scheme":"default","review\_form\_corner\_style":"square","review\_form\_star\_color":"#101010","review\_form\_text\_color":"#333333","review\_form\_background\_color":"#ffffff","review\_form\_field\_background\_color":"#fafafa","review\_form\_button\_color":"#101010","review\_form\_button\_text\_color":"#ffffff","review\_form\_modal\_overlay\_color":"#000000","review\_form\_theme":"multi\_step","review\_form\_location":"in\_store\_popup","review\_form\_external\_page\_background\_color":"#C5F7F0","review\_content\_screen\_title\_text":"How would you rate this product?","review\_content\_introduction\_text":"We would love it if you would share a bit about your experience.","store\_review\_form\_title\_text":"How would you rate this store?","store\_review\_form\_introduction\_text":"We would love it if you would share a bit about your experience.","show\_review\_guidance\_text":true,"one\_star\_review\_guidance\_text":"Poor","five\_star\_review\_guidance\_text":"Great","customer\_information\_screen\_title\_text":"About you","customer\_information\_introduction\_text":"Please tell us more about you.","custom\_questions\_screen\_title\_text":"Your experience in more detail","custom\_questions\_introduction\_text":"Here are a few questions to help us understand more about your experience.","review\_submitted\_screen\_title\_text":"Thanks for your review!","review\_submitted\_screen\_thank\_you\_text":"We are processing it and it will appear on the store soon.","review\_submitted\_screen\_email\_verification\_text":"Please confirm your email by clicking the link we just sent you. This helps us keep reviews authentic.","confirm\_email\_screen\_title\_text":"Confirm your email","confirm\_email\_screen\_message\_text":"To help keep reviews authentic, we'll send you a secure link to continue writing your review. It only takes a moment.","check\_email\_screen\_title\_text":"Check your email","check\_email\_screen\_message\_text":"We sent you an email to {{ email }}. Click the button on the email to continue.","check\_email\_screen\_resend\_message\_text":"Email resent!","check\_email\_resend\_hint\_text":"Didn't get the email? Check your spam folder or [resend the email].","verification\_email\_rate\_limit\_error\_text":"You've reached the limit for review attempts on this product. Please check your inbox or try again later.","review\_submitted\_request\_store\_review\_text":"Would you like to share your experience of shopping with us?","review\_submitted\_review\_other\_products\_text":"Would you like to review these products?","store\_review\_screen\_title\_text":"Would you like to share your experience of shopping with us?","store\_review\_introduction\_text":"We value your feedback and use it to improve. Please share any thoughts or suggestions you have.","reviewer\_media\_screen\_title\_picture\_text":"Share a picture","reviewer\_media\_introduction\_picture\_text":"Upload a photo to support your review.","reviewer\_media\_screen\_title\_video\_text":"Share a video","reviewer\_media\_introduction\_video\_text":"Upload a video to support your review.","reviewer\_media\_screen\_title\_picture\_or\_video\_text":"Share a picture or video","reviewer\_media\_introduction\_picture\_or\_video\_text":"Upload a photo or video to support your review.","reviewer\_media\_youtube\_url\_text":"Paste your Youtube URL here","advanced\_settings\_next\_step\_button\_text":"Next","advanced\_settings\_close\_review\_button\_text":"Close","modal\_write\_review\_flow":true,"write\_review\_flow\_required\_text":"Required","write\_review\_flow\_privacy\_message\_text":"We respect your privacy.","write\_review\_flow\_anonymous\_text":"Post review as anonymous","write\_review\_flow\_visibility\_text":"This won't be visible to other customers.","write\_review\_flow\_multiple\_selection\_help\_text":"Select as many as you like","write\_review\_flow\_single\_selection\_help\_text":"Select one option","write\_review\_flow\_required\_field\_error\_text":"This field is required","write\_review\_flow\_invalid\_email\_error\_text":"Please enter a valid email address","write\_review\_flow\_max\_length\_error\_text":"Max. {{ max\_length }} characters.","write\_review\_flow\_media\_upload\_text":"\u003cb\u003eClick to upload\u003c/b\u003e or drag and drop","write\_review\_flow\_gdpr\_statement":"We'll only contact you about your review if necessary. By submitting your review, you agree to our \u003ca href='https://judge.me/terms' target='\_blank' rel='nofollow noopener'\u003eterms and conditions\u003c/a\u003e and \u003ca href='https://judge.me/privacy' target='\_blank' rel='nofollow noopener'\u003eprivacy policy\u003c/a\u003e.","rating\_only\_reviews\_enabled":false,"show\_negative\_reviews\_help\_screen":false,"new\_review\_flow\_help\_screen\_rating\_threshold":3,"negative\_review\_resolution\_screen\_title\_text":"Tell us more","negative\_review\_resolution\_text":"Your experience matters to us. If there were issues with your purchase, we're here to help. Feel free to reach out to us, we'd love the opportunity to make things right.","negative\_review\_resolution\_button\_text":"Contact us","negative\_review\_resolution\_proceed\_with\_review\_text":"Leave a review","negative\_review\_resolution\_subject":"Issue with purchase from {{ shop\_name }}.{{ order\_name }}","coupon\_promo\_intro\_any\_review\_text":"Write a review and get a coupon for {{ amount }} off your next purchase","coupon\_promo\_intro\_with\_photo\_text":"Write a review and add a photo or video to get a coupon for {{ amount }} off your next purchase","coupon\_promo\_intro\_with\_video\_text":"Write a review and add a video to get a coupon for {{ amount }} off your next purchase","coupon\_promo\_intro\_up\_to\_any\_review\_text":"Write a review and get a coupon for up to {{ amount }} off your next purchase","coupon\_promo\_intro\_up\_to\_with\_photo\_text":"Write a review and add a photo or video to get a coupon for up to {{ amount }} off your next purchase","coupon\_promo\_intro\_external\_text":"Write a review and get a reward for your next purchase","coupon\_promo\_intro\_external\_with\_photo\_text":"Write a review and add a photo or video to get a reward for your next purchase","coupon\_promo\_intro\_external\_with\_video\_text":"Write a review and add a video to get a reward for your next purchase","coupon\_promo\_media\_photo\_text":"Add a photo or video and get a coupon for {{ amount }} off your next purchase","coupon\_promo\_media\_photo\_only\_text":"Add a photo and get a coupon for {{ amount }} off your next purchase","coupon\_promo\_media\_video\_text":"Add a video and get a coupon for {{ amount }} off your next purchase","coupon\_promo\_media\_external\_photo\_text":"Add a photo or video and get a reward for your next purchase","coupon\_promo\_media\_external\_photo\_only\_text":"Add a photo and get a reward for your next purchase","coupon\_promo\_media\_external\_video\_text":"Add a video and get a reward for your next purchase","coupon\_promo\_success\_text":"You've got a coupon for your next purchase at {{ shop\_name }}!","coupon\_promo\_success\_subtext":"You'll receive your coupon email within the hour.","preview\_badge\_collection\_page\_install\_status":false,"widget\_review\_custom\_css":"","preview\_badge\_custom\_css":"","preview\_badge\_stars\_count":"5-stars","featured\_carousel\_custom\_css":"","floating\_tab\_custom\_css":"","all\_reviews\_widget\_custom\_css":"","medals\_widget\_custom\_css":"","verified\_badge\_custom\_css":"","all\_reviews\_text\_custom\_css":"","transparency\_badges\_collected\_via\_store\_invite":false,"transparency\_badges\_from\_another\_provider":false,"transparency\_badges\_collected\_from\_store\_visitor":false,"transparency\_badges\_collected\_by\_verified\_review\_provider":false,"transparency\_badges\_earned\_reward":false,"transparency\_badges\_collected\_via\_store\_invite\_text":"Review collected via store invitation","transparency\_badges\_from\_another\_provider\_text":"Review collected from another provider","transparency\_badges\_collected\_from\_store\_visitor\_text":"Review collected from a store visitor","transparency\_badges\_written\_in\_google\_text":"Review written in Google","transparency\_badges\_written\_in\_etsy\_text":"Review written in Etsy","transparency\_badges\_written\_in\_shop\_app\_text":"Review written in Shop App","transparency\_badges\_earned\_reward\_text":"Review earned a reward for future purchase","product\_review\_widget\_per\_page":7,"widget\_store\_review\_label\_text":"Review about the store","checkout\_comment\_extension\_title\_on\_product\_page":"Customer Comments","checkout\_comment\_extension\_num\_latest\_comment\_show":5,"checkout\_comment\_extension\_format":"name\_and\_timestamp","checkout\_comment\_customer\_name":"last\_initial","checkout\_comment\_comment\_notification":true,"preview\_badge\_collection\_page\_install\_preference":true,"preview\_badge\_home\_page\_install\_preference":false,"preview\_badge\_product\_page\_install\_preference":true,"review\_widget\_install\_preference":"","review\_carousel\_install\_preference":false,"floating\_reviews\_tab\_install\_preference":"none","verified\_reviews\_count\_badge\_install\_preference":false,"all\_reviews\_text\_install\_preference":false,"review\_widget\_best\_location":true,"judgeme\_medals\_install\_preference":false,"review\_widget\_revamp\_enabled":false,"review\_widget\_qna\_enabled":false,"review\_widget\_revamp\_dual\_publish\_end\_date":"2026-04-24T17:01:44.000+00:00","review\_widget\_header\_theme":"minimal","review\_widget\_widget\_title\_enabled":true,"review\_widget\_header\_text\_size":"medium","review\_widget\_header\_text\_weight":"regular","review\_widget\_average\_rating\_style":"compact","review\_widget\_bar\_chart\_enabled":true,"review\_widget\_bar\_chart\_type":"numbers","review\_widget\_bar\_chart\_style":"standard","review\_widget\_expanded\_media\_gallery\_enabled":false,"review\_widget\_show\_review\_highlights":false,"review\_widget\_show\_review\_keywords\_in\_gray":false,"review\_widget\_reviews\_section\_theme":"standard","review\_widget\_image\_style":"thumbnails","review\_widget\_review\_image\_ratio":"square","review\_widget\_stars\_size":"medium","review\_widget\_verified\_badge":"standard\_text","review\_widget\_review\_title\_text\_size":"medium","review\_widget\_review\_text\_size":"medium","review\_widget\_review\_text\_length":"medium","review\_widget\_number\_of\_columns\_desktop":3,"review\_widget\_carousel\_transition\_speed":5,"review\_widget\_custom\_questions\_answers\_display":"always","review\_widget\_card\_section\_size":"small","review\_widget\_button\_text\_color":"#FFFFFF","review\_widget\_text\_color":"#000000","review\_widget\_lighter\_text\_color":"#7B7B7B","review\_widget\_corner\_styling":"soft","review\_widget\_review\_word\_singular":"review","review\_widget\_review\_word\_plural":"reviews","review\_widget\_voting\_label":"Helpful?","review\_widget\_shop\_reply\_label":"Reply from {{ shop\_name }}:","review\_widget\_filters\_title":"Filters","review\_widget\_filter\_rating\_title":"Rating","review\_widget\_filter\_keyword\_title":"Keyword","review\_widget\_clear\_filters\_text":"Clear filters","review\_widget\_expand\_more\_text":"More","review\_widget\_review\_highlights\_title":"Review highlights","qna\_widget\_question\_word\_singular":"Question","qna\_widget\_question\_word\_plural":"Questions","qna\_widget\_answer\_reply\_label":"Answer from {{ answerer\_name }}:","qna\_content\_screen\_title\_text":"Ask a question about this product","qna\_widget\_question\_required\_field\_error\_text":"Please enter your question.","qna\_widget\_flow\_gdpr\_statement":"We'll only contact you about your question if necessary. By submitting your question, you agree to our \u003ca href='https://judge.me/terms' target='\_blank' rel='nofollow noopener'\u003eterms and conditions\u003c/a\u003e and \u003ca href='https://judge.me/privacy' target='\_blank' rel='nofollow noopener'\u003eprivacy policy\u003c/a\u003e.","qna\_widget\_question\_submitted\_text":"Thanks for your question!","qna\_widget\_close\_form\_text\_question":"Close","qna\_widget\_question\_submit\_success\_text":"We’ll notify you by email when your question is answered.","all\_reviews\_widget\_v2025\_enabled":false,"all\_reviews\_widget\_v2025\_header\_theme":"default","all\_reviews\_widget\_v2025\_widget\_title\_enabled":true,"all\_reviews\_widget\_v2025\_header\_text\_size":"medium","all\_reviews\_widget\_v2025\_header\_text\_weight":"regular","all\_reviews\_widget\_v2025\_average\_rating\_style":"compact","all\_reviews\_widget\_v2025\_bar\_chart\_enabled":true,"all\_reviews\_widget\_v2025\_bar\_chart\_type":"numbers","all\_reviews\_widget\_v2025\_bar\_chart\_style":"standard","all\_reviews\_widget\_v2025\_expanded\_media\_gallery\_enabled":false,"all\_reviews\_widget\_v2025\_show\_store\_medals":true,"all\_reviews\_widget\_v2025\_show\_photo\_gallery":true,"all\_reviews\_widget\_v2025\_show\_review\_keywords":false,"all\_reviews\_widget\_v2025\_show\_ai\_summary":false,"all\_reviews\_widget\_v2025\_show\_ai\_summary\_bg":false,"all\_reviews\_widget\_v2025\_show\_review\_highlights":false,"all\_reviews\_widget\_v2025\_show\_review\_keywords\_in\_gray":false,"all\_reviews\_widget\_v2025\_add\_search\_bar":false,"all\_reviews\_widget\_v2025\_default\_sort\_method":"most-recent","all\_reviews\_widget\_v2025\_reviews\_per\_page":10,"all\_reviews\_widget\_v2025\_reviews\_section\_theme":"default","all\_reviews\_widget\_v2025\_image\_style":"thumbnails","all\_reviews\_widget\_v2025\_review\_image\_ratio":"square","all\_reviews\_widget\_v2025\_stars\_size":"medium","all\_reviews\_widget\_v2025\_verified\_badge":"standard\_text","all\_reviews\_widget\_v2025\_review\_title\_text\_size":"medium","all\_reviews\_widget\_v2025\_review\_text\_size":"medium","all\_reviews\_widget\_v2025\_review\_text\_length":"medium","all\_reviews\_widget\_v2025\_number\_of\_columns\_desktop":3,"all\_reviews\_widget\_v2025\_carousel\_transition\_speed":5,"all\_reviews\_widget\_v2025\_custom\_questions\_answers\_display":"always","all\_reviews\_widget\_v2025\_review\_dates":false,"all\_reviews\_widget\_v2025\_card\_section\_size":"small","all\_reviews\_widget\_v2025\_show\_product\_variant":false,"all\_reviews\_widget\_v2025\_show\_reviewer\_avatar":true,"all\_reviews\_widget\_v2025\_reviewer\_name\_as\_initial":"","all\_reviews\_widget\_v2025\_review\_location\_show":false,"all\_reviews\_widget\_v2025\_location\_format":"","all\_reviews\_widget\_v2025\_show\_country\_flag":false,"all\_reviews\_widget\_v2025\_widget\_thumb":false,"all\_reviews\_widget\_v2025\_verified\_by\_shop\_badge\_style":"light","all\_reviews\_widget\_v2025\_social\_share":false,"all\_reviews\_widget\_v2025\_social\_share\_options\_order":"Facebook,Twitter,LinkedIn,Pinterest","all\_reviews\_widget\_v2025\_pagination\_type":"standard","all\_reviews\_widget\_v2025\_button\_text\_color":"#FFFFFF","all\_reviews\_widget\_v2025\_text\_color":"#000000","all\_reviews\_widget\_v2025\_lighter\_text\_color":"#7B7B7B","all\_reviews\_widget\_v2025\_corner\_styling":"soft","all\_reviews\_widget\_v2025\_title":"Customer reviews","all\_reviews\_widget\_v2025\_ai\_summary\_title":"Customers say about this store","all\_reviews\_widget\_v2025\_no\_review\_text":"Be the first to write a review","all\_reviews\_widget\_v2025\_review\_highlights\_title":"Review highlights","reviews\_grid\_widget\_show\_sample\_reviews":false,"reviews\_grid\_widget\_review\_selection":"all","reviews\_grid\_widget\_select\_products":[],"reviews\_grid\_widget\_show\_media\_only":false,"reviews\_grid\_widget\_display\_order":"media\_first","reviews\_grid\_widget\_card\_grouping":"per\_media","reviews\_grid\_widget\_columns\_desktop":3,"reviews\_grid\_widget\_rows\_desktop":3,"reviews\_grid\_widget\_columns\_mobile":2,"reviews\_grid\_widget\_rows\_mobile":6,"reviews\_grid\_widget\_show\_stars":true,"reviews\_grid\_widget\_show\_reviewer\_name":true,"reviews\_grid\_widget\_show\_review\_title\_on\_hover\_desktop":true,"reviews\_grid\_widget\_corner\_styling":"soft","reviews\_grid\_widget\_card\_spacing":"medium","reviews\_grid\_widget\_header\_text\_color":"#000000","reviews\_grid\_widget\_star\_and\_reviewer\_name\_color":"#F9F9F9","reviews\_grid\_widget\_overlay\_and\_background\_color":"#000000","reviews\_grid\_widget\_content\_color":"#F9F9F9","reviews\_grid\_widget\_header\_text":"From our customers","reviews\_grid\_widget\_show\_average\_rating":true,"trust\_badge\_enabled":false,"trust\_badge\_structure":"outline","trust\_badge\_color":"black","trust\_badge\_star":"black","trust\_badge\_rating\_display\_default":"show\_avg\_text","platform":"shopify","branding\_url":"https://app.judge.me/reviews/stores/beardbrand.com","branding\_text":"Powered by Judge.me","locale":"en","reply\_name":"Beardbrand","shop\_currency":"USD","widget\_version":"3.0","footer":true,"autopublish":true,"review\_dates":true,"enable\_custom\_form":false,"shop\_use\_review\_site":true,"shop\_locale":"en","enable\_multi\_locales\_translations":false,"show\_review\_title\_input":true,"review\_verification\_email\_status":"always","require\_verification\_before\_submit":false,"customer\_account\_validation\_enabled":true,"coupon\_promo\_invited\_eligible":true,"coupon\_promo\_web\_eligible":false,"uses\_coupon\_integration":false,"uses\_external\_coupon":false,"can\_be\_branded":true,"reply\_name\_text":"Beardbrand Team"}; .jdgm-xx{left:0}:root{--jdgm-primary-color: #101010;--jdgm-secondary-color: #F9F8F6;--jdgm-star-color: #101010;--jdgm-write-review-text-color: #F9F8F6;--jdgm-write-review-bg-color: #101010;--jdgm-paginate-color: #101010;--jdgm-border-radius: 0;--jdgm-reviewer-name-color: #101010}.jdgm-histogram\_\_bar-content{background-color:#101010}.jdgm-rev[data-verified-buyer=true] .jdgm-rev\_\_icon.jdgm-rev\_\_icon:after,.jdgm-rev\_\_buyer-badge.jdgm-rev\_\_buyer-badge{color:#F9F8F6;background-color:#101010}.jdgm-review-widget--small .jdgm-gallery.jdgm-gallery .jdgm-gallery\_\_thumbnail-link:nth-child(8) .jdgm-gallery\_\_thumbnail-wrapper.jdgm-gallery\_\_thumbnail-wrapper:before{content:"See more"}@media only screen and (min-width: 768px){.jdgm-gallery.jdgm-gallery .jdgm-gallery\_\_thumbnail-link:nth-child(8) .jdgm-gallery\_\_thumbnail-wrapper.jdgm-gallery\_\_thumbnail-wrapper:before{content:"See more"}}.jdgm-rev\_\_thumb-btn{color:#101010}.jdgm-rev\_\_thumb-btn:hover{opacity:0.8}.jdgm-rev\_\_thumb-btn:not([disabled]):hover,.jdgm-rev\_\_thumb-btn:hover,.jdgm-rev\_\_thumb-btn:active,.jdgm-rev\_\_thumb-btn:visited{color:#101010}.jdgm-preview-badge .jdgm-star.jdgm-star{color:#101010}.jdgm-prev-badge[data-average-rating='0.00']{display:none !important}.jdgm-rev .jdgm-rev\_\_icon{display:none !important}.jdgm-widget.jdgm-all-reviews-widget,.jdgm-widget .jdgm-rev-widg{border:none;padding:0}.jdgm-author-fullname{display:none !important}.jdgm-author-all-initials{display:none !important}.jdgm-rev-widg\_\_title{visibility:hidden}.jdgm-rev-widg\_\_summary-text{visibility:hidden}.jdgm-prev-badge\_\_text{visibility:hidden}.jdgm-rev\_\_prod-link-prefix:before{content:'about'}.jdgm-rev\_\_variant-label:before{content:'Variant: '}.jdgm-rev\_\_out-of-store-text:before{content:'(out of store)'}@media only screen and (min-width: 768px){.jdgm-rev\_\_pics .jdgm-rev\_all-rev-page-picture-separator,.jdgm-rev\_\_pics .jdgm-rev\_\_product-picture{display:none}}@media only screen and (max-width: 768px){.jdgm-rev\_\_pics .jdgm-rev\_all-rev-page-picture-separator,.jdgm-rev\_\_pics .jdgm-rev\_\_product-picture{display:none}}.jdgm-preview-badge[data-template="index"]{display:none !important}.jdgm-verified-count-badget[data-from-snippet="true"]{display:none !important}.jdgm-carousel-wrapper[data-from-snippet="true"]{display:none !important}.jdgm-all-reviews-text[data-from-snippet="true"]{display:none !important}.jdgm-medals-section[data-from-snippet="true"]{display:none !important}.jdgm-ugc-media-wrapper[data-from-snippet="true"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_collected\_via\_store\_invitation"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_collected\_from\_another\_provider"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_collected\_from\_store\_visitor"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_written\_in\_etsy"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_written\_in\_google\_business"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_written\_in\_shop\_app"]{display:none !important}.jdgm-rev\_\_transparency-badge[data-badge-type="review\_earned\_for\_future\_purchase"]{display:none !important}.jdgm-review-snippet-widget{--jdgm-snippet-card-color: #fff;--jdgm-snippet-text-color: #000;--jdgm-snippet-lighter-text-color: #7B7B7B;--jdgm-snippet-star-color: #101010;--jdgm-snippet-border-radius: 8px;--jdgm-snippet-arrows-bg-color: #fff;--jdgm-snippet-arrows-color: #000}.jdgm-review-snippet-widget .jdgm-rev-snippet-widget\_\_cards-container .jdgm-rev-snippet-card{border-radius:8px;background:#fff}.jdgm-review-snippet-widget .jdgm-rev-snippet-widget\_\_cards-container .jdgm-rev-snippet-card\_\_rev-rating .jdgm-star{color:#101010}.jdgm-review-snippet-widget .jdgm-rev-snippet-widget\_\_prev-btn,.jdgm-review-snippet-widget .jdgm-rev-snippet-widget\_\_next-btn{border-radius:50%;background:#fff}.jdgm-review-snippet-widget .jdgm-rev-snippet-widget\_\_prev-btn>svg,.jdgm-review-snippet-widget .jdgm-rev-snippet-widget\_\_next-btn>svg{fill:#000}.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jm-mfp-content,.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev\_\_icon,.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev\_\_pic-img,.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev\_\_reply{border-radius:8px}.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev[data-verified-buyer="true"] .jdgm-full-rev\_\_icon::after{border-radius:8px}.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev .jdgm-rev\_\_buyer-badge{border-radius:calc( 8px / 2 )}.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev .jdgm-full-rev\_\_replier::before{content:'Beardbrand'}.jdgm-full-rev-modal.rev-snippet-widget .jm-mfp-container .jdgm-full-rev .jdgm-full-rev\_\_product-button{border-radius:calc( 8px \* 6 )}
 

@-webkit-keyframes jdgm-spin{0%{-webkit-transform:rotate(0deg);-ms-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);-ms-transform:rotate(359deg);transform:rotate(359deg)}}@keyframes jdgm-spin{0%{-webkit-transform:rotate(0deg);-ms-transform:rotate(0deg);transform:rotate(0deg)}100%{-webkit-transform:rotate(359deg);-ms-transform:rotate(359deg);transform:rotate(359deg)}}@font-face{font-family:'JudgemeStar';src:url("data:application/x-font-woff;charset=utf-8;base64,d09GRgABAAAAAAScAA0AAAAABrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAAEgAAAABoAAAAcbyQ+3kdERUYAAARgAAAAHgAAACAAMwAGT1MvMgAAAZgAAABGAAAAVi+vS9xjbWFwAAAB8AAAAEAAAAFKwBMjvmdhc3AAAARYAAAACAAAAAj//wADZ2x5ZgAAAkAAAAEJAAABdH33LXtoZWFkAAABMAAAAC0AAAA2BroQKWhoZWEAAAFgAAAAHAAAACQD5QHQaG10eAAAAeAAAAAPAAAAFAYAAABsb2NhAAACMAAAAA4AAAAOAO4AeG1heHAAAAF8AAAAHAAAACAASgAvbmFtZQAAA0wAAADeAAABkorWfVZwb3N0AAAELAAAACkAAABEp3ubLXgBY2BkYADhPPP4OfH8Nl8ZuJkYQODS2fRrCPr/aSYGxq1ALgcDWBoAO60LkwAAAHgBY2BkYGDc+v80gx4TAwgASaAICmABAFB+Arl4AWNgZGBgYGPQYWBiAAIwyQgWc2AAAwAHVQB6eAFjYGRiYJzAwMrAwejDmMbAwOAOpb8ySDK0MDAwMbByMsCBAAMCBKS5pjA4PGB4wMR44P8BBj3GrQymQGFGkBwAjtgK/gAAeAFjYoAAEA1jAwAAZAAHAHgB3crBCcAwDEPRZydkih567CDdf4ZskmLwFBV8xBfCaC4BXkOUmx4sU0h2ngNb9V0vQCxaRKIAevT7fGWuBrEAAAAAAAAAAAA0AHgAugAAeAF9z79Kw1AUx/FzTm7un6QmJtwmQ5Bg1abgEGr/BAqlU6Gju+Cgg1MkQ/sA7Vj7BOnmO/gUvo2Lo14NqIO6/IazfD8HEODtmQCfoANwNsyp2/GJt3WKQrd1NLiYYWx2PBqOsmJMEOznPOTzfSCrhAtbbLdmeFLJV9eKd63WLrZcIcuaEVdssWCKM6pLCfTVOYbz/0pNSMSZKLIZpvh78sAUH6PlMrreTCabP9r+Z/puPZ2ur/RqpQHgh+MIegCnXeM4MRAPjYN//5tj4ZtTjkFqEdmeMShlEJ7tVAly2TAkx6R68Fl4E/aVvn8JqHFQ4JS1434gXKcuL31dDhzs3YbsEOAd/IU88gAAAHgBfY4xTgMxEEVfkk0AgRCioKFxQYd2ZRtpixxgRU2RfhU5q5VWseQ4JdfgAJyBlmNwAM7ABRhZQ0ORwp7nr+eZAa54YwYg9zm3ynPOeFRe8MCrciXOh/KSS76UV5L/iDmrLiS5AeU519wrL3jmSbkS5115yR2fyivJv9kx0ZMZ2RLZw27q87iNQi8EBo5FSPIMw3HqBboi5lKTGAGDp8FKXWP+t9TU01Lj5His1Ba6uM9dTEMwvrFmbf5GC/q2drW3ruXUhhsCiQOjznFlCzYhHUZp4xp76vsvQh89CQAAeAFjYGJABowM6IANLMrEyMTIzMjCXpyRWJBqZshWXJJYBKOMAFHFBucAAAAAAAAB//8AAngBY2BkYGDgA2IJBhBgAvKZGViBJAuYxwAABJsAOgAAeAFjYGBgZACCk535hiD60tn0azAaAEqpB6wAAA==") format("woff");font-weight:normal;font-style:normal}.jdgm-star{font-family:'JudgemeStar';display:inline !important;text-decoration:none !important;padding:0 4px 0 0 !important;margin:0 !important;font-weight:bold;opacity:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.jdgm-star:hover{opacity:1}.jdgm-star:last-of-type{padding:0 !important}.jdgm-star.jdgm--on:before{content:"\e000"}.jdgm-star.jdgm--off:before{content:"\e001"}.jdgm-star.jdgm--half:before{content:"\e002"}.jdgm-widget \*{margin:0;line-height:1.4;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;-webkit-overflow-scrolling:touch}.jdgm-hidden{display:none !important;visibility:hidden !important}.jdgm-temp-hidden{display:none}.jdgm-spinner{width:40px;height:40px;margin:auto;border-radius:50%;border-top:2px solid #eee;border-right:2px solid #eee;border-bottom:2px solid #eee;border-left:2px solid #ccc;-webkit-animation:jdgm-spin 0.8s infinite linear;animation:jdgm-spin 0.8s infinite linear}.jdgm-prev-badge{display:block !important}

!function(e){window.jdgm=window.jdgm||{},jdgm.CDN\_HOST="https://cdnwidget.judge.me/",jdgm.CDN\_HOST\_ALT="https://cdn2.judge.me/cdn/widget\_frontend/",jdgm.API\_HOST="https://api.judge.me/",jdgm.CDN\_BASE\_URL="https://cdn.shopify.com/extensions/019eb5d5-15a2-7881-a1c0-2c193621a131/judgeme-569/assets/",jdgm.CDN\_API\_HOST="https://cdn.judge.me/",
jdgm.docReady=function(d){(e.attachEvent?"complete"===e.readyState:"loading"!==e.readyState)?
setTimeout(d,0):e.addEventListener("DOMContentLoaded",d)},jdgm.loadCSS=function(d,t,o,a){
!o&&jdgm.loadCSS.requestedUrls.indexOf(d)>=0||(jdgm.loadCSS.requestedUrls.push(d),
(a=e.createElement("link")).rel="stylesheet",a.class="jdgm-stylesheet",a.media="nope!",
a.href=d,a.onload=function(){this.media="all",t&&setTimeout(t)},e.body.appendChild(a))},
jdgm.loadCSS.requestedUrls=[],jdgm.loadJS=function(e,d){var t=new XMLHttpRequest;
t.onreadystatechange=function(){4===t.readyState&&(Function(t.response)(),d&&d(t.response))},
t.open("GET",e),t.onerror=function(){if(e.indexOf(jdgm.CDN\_HOST)===0&&jdgm.CDN\_HOST\_ALT!==jdgm.CDN\_HOST){var f=e.replace(jdgm.CDN\_HOST,jdgm.CDN\_HOST\_ALT);jdgm.loadJS(f,d)}},t.send()},jdgm.docReady((function(){(window.jdgmLoadCSS||e.querySelectorAll(
".jdgm-widget, .jdgm-all-reviews-page").length>0)&&(jdgmSettings.widget\_load\_with\_code\_splitting?
parseFloat(jdgmSettings.widget\_version)>=3?jdgm.loadCSS(jdgm.CDN\_BASE\_URL+"widget\_v3\_base.css"):
jdgm.loadCSS(jdgm.CDN\_BASE\_URL+"widget\_base.css"):jdgm.loadCSS(jdgm.CDN\_BASE\_URL+"shopify\_v2.css")
)}))}(document);


(function() {
var jdgmThemeFixes = {"129032912979":{"html":"","css":"","js":"\ndocument.addEventListener('DOMContentLoaded', function() {\n function updateElementTag(selector, newTag) {\n document.querySelectorAll(selector).forEach(el =\u003e {\n el.outerHTML = `\u003c${newTag} class=\"${el.className}\"\u003e${el.innerHTML}\u003c\/${newTag}\u003e`;\n });\n }\n updateElementTag('.jdgm-rev\_\_prod-link', 'span');\n});\n"}};
if (!jdgmThemeFixes) return;
var thisThemeFix = jdgmThemeFixes[Shopify.theme.id];
if (!thisThemeFix) return;
if (thisThemeFix.html) {
document.addEventListener("DOMContentLoaded", function() {
var htmlDiv = document.createElement('div');
htmlDiv.classList.add('jdgm-theme-fix-html');
htmlDiv.innerHTML = thisThemeFix.html;
document.body.append(htmlDiv);
});
};
if (thisThemeFix.css) {
var styleTag = document.createElement('style');
styleTag.classList.add('jdgm-theme-fix-style');
styleTag.innerHTML = thisThemeFix.css;
document.head.append(styleTag);
};
if (thisThemeFix.js) {
var scriptTag = document.createElement('script');
scriptTag.classList.add('jdgm-theme-fix-script');
scriptTag.innerHTML = thisThemeFix.js;
document.head.append(scriptTag);
};
})();




!function(s) {
let o = s.createElement('script'), u = s.getElementsByTagName('script')[0];
o.src = 'https://cdn.aggle.net/oir/oir.min.js';
o.async = !0, o.setAttribute('oirtyp', '48b1feaa'), o.setAttribute('oirid', 'P965372B3');
u.parentNode.insertBefore(o, u);
}(document);

{
const cleanObj = (value) => {
if (Array.isArray(value)) {
const cleanedArray = value.map(cleanObj).filter((v) => v !== undefined);
return cleanedArray.length ? cleanedArray : undefined;
}
if (value && typeof value === "object") {
const cleanedObject = Object.entries(value).reduce((acc, [key, val]) => {
const cleanedValue = cleanObj(val);
if (cleanedValue !== undefined && cleanedValue !== null && cleanedValue !== "") {
acc[key] = cleanedValue;
}
return acc;
}, {});
return Object.keys(cleanedObject).length ? cleanedObject : undefined;
}
if (value === null || value === undefined || value === "") {
return undefined;
}
return value;
};
const getCustomer = () => ({
shopifyCustomerId: "",
email: "",
phone: "",
first\_name: null,
last\_name: null,
lifetime\_value: null,
order\_count: null,
address: {
street: null,
city: null,
state: null,
stateCode: null,
postalCode: "",
country: "",
province: "",
countryCode: "",
}
});
}



(function(){if ("sendBeacon" in navigator && "performance" in window) {try {var session\_token\_from\_headers = performance.getEntriesByType('navigation')[0].serverTiming.find(x => x.name == '\_s').description;} catch {var session\_token\_from\_headers = undefined;}var session\_cookie\_matches = document.cookie.match(/\_shopify\_s=([^;]\*)/);var session\_token\_from\_cookie = session\_cookie\_matches && session\_cookie\_matches.length === 2 ? session\_cookie\_matches[1] : "";var session\_token = session\_token\_from\_headers || session\_token\_from\_cookie || "";function handle\_abandonment\_event(e) {var entries = performance.getEntries().filter(function(entry) {return /monorail-edge.shopifysvc.com/.test(entry.name);});if (!window.abandonment\_tracked && entries.length === 0) {window.abandonment\_tracked = true;var currentMs = Date.now();var navigation\_start = performance.timing.navigationStart;var payload = {shop\_id: 2090478,url: window.location.href,navigation\_start,duration: currentMs - navigation\_start,session\_token,page\_type: "cart"};window.navigator.sendBeacon("https://monorail-edge.shopifysvc.com/v1/produce", JSON.stringify({schema\_id: "online\_store\_buyer\_site\_abandonment/1.1",payload: payload,metadata: {event\_created\_at\_ms: currentMs,event\_sent\_at\_ms: currentMs}}));}}window.addEventListener('pagehide', handle\_abandonment\_event);}}());

window.\_\_TREKKIE\_SHIM\_QUEUE = window.\_\_TREKKIE\_SHIM\_QUEUE || [];
(function(){var wpmLoader=function(){"use strict";return function(e,d,r,n){var o=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{};if(!Boolean(null==(i=null==(a=window.Shopify)?void 0:a.analytics)?void 0:i.replayQueue)){var a,i;window.Shopify=window.Shopify||{};var t=window.Shopify;t.analytics=t.analytics||{};var s=t.analytics;s.replayQueue=[],s.publish=function(e,d,r){return s.replayQueue.push([e,d,r]),!0};try{self.performance.mark("wpm:start")}catch(e){}var l,u,c,m,p,f,h,g,y,w,v,b,S,P=(u=(l={modern:/Edge?\/(1{2}[4-9]|1[2-9]\d|[2-9]\d{2}|\d{4,})\.\d+(\.\d+|)|Firefox\/(1{2}[4-9]|1[2-9]\d|[2-9]\d{2}|\d{4,})\.\d+(\.\d+|)|Chrom(ium|e)\/(9{2}|\d{3,})\.\d+(\.\d+|)|(Maci|X1{2}).+ Version\/(15\.\d+|(1[6-9]|[2-9]\d|\d{3,})\.\d+)([,.]\d+|)( \(\w+\)|)( Mobile\/\w+|) Safari\/|Chrome.+OPR\/(9{2}|\d{3,})\.\d+\.\d+|(CPU[ +]OS|iPhone[ +]OS|CPU[ +]iPhone|CPU IPhone OS|CPU iPad OS)[ +]+(15[.\_]\d+|(1[6-9]|[2-9]\d|\d{3,})[.\_]\d+)([.\_]\d+|)|Android:?[ /-](13[3-9]|1[4-9]\d|[2-9]\d{2}|\d{4,})(\.\d+|)(\.\d+|)|Android.+Firefox\/(13[5-9]|1[4-9]\d|[2-9]\d{2}|\d{4,})\.\d+(\.\d+|)|Android.+Chrom(ium|e)\/(13[3-9]|1[4-9]\d|[2-9]\d{2}|\d{4,})\.\d+(\.\d+|)|SamsungBrowser\/([2-9]\d|\d{3,})\.\d+/,legacy:/Edge?\/(1[6-9]|[2-9]\d|\d{3,})\.\d+(\.\d+|)|Firefox\/(5[4-9]|[6-9]\d|\d{3,})\.\d+(\.\d+|)|Chrom(ium|e)\/(5[1-9]|[6-9]\d|\d{3,})\.\d+(\.\d+|)([\d.]+$|.\*Safari\/(?![\d.]+ Edge\/[\d.]+$))|(Maci|X1{2}).+ Version\/(10\.\d+|(1[1-9]|[2-9]\d|\d{3,})\.\d+)([,.]\d+|)( \(\w+\)|)( Mobile\/\w+|) Safari\/|Chrome.+OPR\/(3[89]|[4-9]\d|\d{3,})\.\d+\.\d+|(CPU[ +]OS|iPhone[ +]OS|CPU[ +]iPhone|CPU IPhone OS|CPU iPad OS)[ +]+(10[.\_]\d+|(1[1-9]|[2-9]\d|\d{3,})[.\_]\d+)([.\_]\d+|)|Android:?[ /-](13[3-9]|1[4-9]\d|[2-9]\d{2}|\d{4,})(\.\d+|)(\.\d+|)|Mobile Safari.+OPR\/([89]\d|\d{3,})\.\d+\.\d+|Android.+Firefox\/(13[5-9]|1[4-9]\d|[2-9]\d{2}|\d{4,})\.\d+(\.\d+|)|Android.+Chrom(ium|e)\/(13[3-9]|1[4-9]\d|[2-9]\d{2}|\d{4,})\.\d+(\.\d+|)|Android.+(UC? ?Browser|UCWEB|U3)[ /]?(15\.([5-9]|\d{2,})|(1[6-9]|[2-9]\d|\d{3,})\.\d+)\.\d+|SamsungBrowser\/(5\.\d+|([6-9]|\d{2,})\.\d+)|Android.+MQ{2}Browser\/(14(\.(9|\d{2,})|)|(1[5-9]|[2-9]\d|\d{3,})(\.\d+|))(\.\d+|)|K[Aa][Ii]OS\/(3\.\d+|([4-9]|\d{2,})\.\d+)(\.\d+|)/}).modern,c=l.legacy,(m=navigator.userAgent).match(u)?"modern":m.match(c)?"legacy":"unknown"),C="modern"===P?"modern":"legacy",\_=(null!=n?n:{modern:"",legacy:""})[C],O=[(p={baseUrl:d,hashVersion:r,buildTarget:C}).baseUrl,"/wpm","/b",p.hashVersion,"modern"===p.buildTarget?"m":"l",".js"].join(""),U=(f={version:r,bundleTarget:P,surface:e.surface,pageUrl:self.location.href,monorailEndpoint:e.monorailEndpoint},h=f.version,g=f.bundleTarget,y=f.surface,w=f.pageUrl,v=f.monorailEndpoint,{emit:function(e){var d=e.status,r=e.errorMsg,n=(new Date).getTime(),o=JSON.stringify({metadata:{event\_sent\_at\_ms:n},events:[{schema\_id:"web\_pixels\_manager\_load/3.1",payload:{version:h,bundle\_target:g,page\_url:w,status:d,surface:y,error\_msg:r},metadata:{event\_created\_at\_ms:n}}]});if(!v)return console&&console.warn&&console.warn("[Web Pixels Manager] No Monorail endpoint provided, skipping logging."),!1;try{return self.navigator.sendBeacon.bind(self.navigator)(v,o)}catch(e){}var a=new XMLHttpRequest;try{return a.open("POST",v,!0),a.setRequestHeader("Content-Type","text/plain"),a.send(o),!0}catch(e){return console&&console.warn&&console.warn("[Web Pixels Manager] Got an unhandled error while logging to Monorail."),!1}}});try{o.browserTarget=P,function(e){var d=e.src,r=e.async,n=void 0===r||r,o=e.onload,a=e.onerror,i=e.sri,t=e.scriptDataAttributes,s=void 0===t?{}:t,l=document.createElement("script"),u=document.querySelector("head"),c=document.querySelector("body");if(l.async=n,l.src=d,i&&(l.integrity=i,l.crossOrigin="anonymous"),s)for(var m in s)if(Object.prototype.hasOwnProperty.call(s,m))try{l.dataset[m]=s[m]}catch(e){}if(o&&l.addEventListener("load",o),a&&l.addEventListener("error",a),u)u.appendChild(l);else{if(!c)throw new Error("Did not find a head or body element to append the script");c.appendChild(l)}}({src:O,async:!0,onload:function(){if(!function(){var e,d;return Boolean(null==(d=null==(e=window.Shopify)?void 0:e.analytics)?void 0:d.initialized)}()){var d=window.webPixelsManager.init(e)||void 0;if(d){var r=window.Shopify.analytics;r.replayQueue.forEach(function(e){var r=e[0],n=e[1],o=e[2];d.publishCustomEvent(r,n,o)}),r.replayQueue=[],r.publish=d.publishCustomEvent,r.visitor=d.visitor,r.initialized=!0}}},onerror:function(){return U.emit({status:"failed",errorMsg:"".concat(O," has failed to load")})},sri:(b=\_,S=/^sha384-[A-Za-z0-9+/=]+$/,"string"==typeof b&&S.test(b)?\_:""),scriptDataAttributes:o}),U.emit({status:"loading"})}catch(e){U.emit({status:"failed",errorMsg:(null==e?void 0:e.message)||"Unknown error"})}}}}();wpmLoader({shopId: 2090478,storefrontBaseUrl: "https://www.beardbrand.com",extensionsBaseUrl: "https://extensions.shopifycdn.com/cdn/shopifycloud/web-pixels-manager",monorailEndpoint: "https://monorail-edge.shopifysvc.com/unstable/produce\_batch",surface: "storefront-renderer",enabledBetaFlags: ["d5bdd5d0","f36ec97b","2b8f910e"],webPixelsConfigList: [{"id":"2250408306","configuration":"{\"pixelId\":\"e2a22d9d-5ef2-4406-96be-96d8f3b6c5cd\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"c119f01612c13b62ab52809eb08154bb","type":"APP","apiClientId":2556259,"privacyPurposes":["ANALYTICS","MARKETING","SALE\_OF\_DATA"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_address","read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data","read\_customer\_phone"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"2243985778","configuration":"{\"companyID\":\"gid:\/\/shopify\/Shop\/2090478\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"53a564b8574378237642302dbd2cb842","type":"APP","apiClientId":91426783233,"privacyPurposes":["ANALYTICS","MARKETING","SALE\_OF\_DATA"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"1580302706","configuration":"{\"pixelCode\":\"C6JTOBQEOTD2SO8H3300\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"22e92c2ad45662f435e4801458fb78cc","type":"APP","apiClientId":4383523,"privacyPurposes":["ANALYTICS","MARKETING","SALE\_OF\_DATA"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_address","read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data","read\_customer\_phone"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"1498153330","configuration":"{\"accountID\":\"hFArAj\",\"webPixelConfig\":\"eyJlbmFibGVBZGRlZFRvQ2FydEV2ZW50cyI6IHRydWV9\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"524f6c1ee37bacdca7657a665bdca589","type":"APP","apiClientId":123074,"privacyPurposes":["ANALYTICS","MARKETING"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_address","read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data","read\_customer\_phone"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted","enabledFlags":["9a3ed68a"]},{"id":"1477280114","configuration":"{\"storeHandle\":\"beardbrand.myshopify.com\", \"publisherId\": \"P965372B3\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"94a881e8d211e628cef2d7cbc6e68cf4","type":"APP","apiClientId":281572343809,"privacyPurposes":["ANALYTICS","MARKETING","SALE\_OF\_DATA"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_address","read\_customer\_email","read\_customer\_name","read\_customer\_phone","read\_customer\_personal\_data"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"1099268466","configuration":"{\"webPixelName\":\"Judge.me\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"34ad157958823915625854214640f0bf","type":"APP","apiClientId":683015,"privacyPurposes":["ANALYTICS"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data","read\_customer\_phone"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"898597234","configuration":"{\"store\_id\":\"433\",\"environment\":\"prod\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"c8753c9f7c80c1a1c22d49b41efcf0a4","type":"APP","apiClientId":294517,"privacyPurposes":["ANALYTICS"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_address","read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data","read\_customer\_phone"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"887456114","configuration":"{\"merchantId\":\"1022949\", \"url\":\"https:\/\/classic.avantlink.com\", \"shopName\":\"beardbrand\"}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"26843be7e7f0ff401f557cffac6b5a49","type":"APP","apiClientId":125215244289,"privacyPurposes":["ANALYTICS","SALE\_OF\_DATA"],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_personal\_data"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted"},{"id":"423264339","configuration":"{\"config\":\"{\\\"google\_tag\_ids\\\":[\\\"AW-990174919\\\",\\\"GT-PHXR7JPZ\\\",\\\"GT-MQ76SPS\\\"],\\\"target\_country\\\":\\\"US\\\",\\\"gtag\_events\\\":[{\\\"type\\\":\\\"begin\_checkout\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/DtgnCMKgiYAcEMe9k9gD\\\",\\\"MC-KTVSQG7PBN\\\"]},{\\\"type\\\":\\\"search\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/dx5SCJ-GkYAcEMe9k9gD\\\",\\\"MC-KTVSQG7PBN\\\"]},{\\\"type\\\":\\\"view\_item\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/i-MnCJyGkYAcEMe9k9gD\\\",\\\"MC-XC4FV1G8TM\\\",\\\"MC-ZZXJ707RZ7\\\",\\\"MC-KTVSQG7PBN\\\"]},{\\\"type\\\":\\\"purchase\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/Oib\_CL-giYAcEMe9k9gD\\\",\\\"MC-XC4FV1G8TM\\\",\\\"MC-ZZXJ707RZ7\\\",\\\"MC-KTVSQG7PBN\\\"]},{\\\"type\\\":\\\"page\_view\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/U3y-CJmGkYAcEMe9k9gD\\\",\\\"MC-XC4FV1G8TM\\\",\\\"MC-ZZXJ707RZ7\\\",\\\"MC-KTVSQG7PBN\\\"]},{\\\"type\\\":\\\"add\_payment\_info\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/WxwnCKKGkYAcEMe9k9gD\\\",\\\"MC-KTVSQG7PBN\\\"]},{\\\"type\\\":\\\"add\_to\_cart\\\",\\\"action\_label\\\":[\\\"AW-990174919\\\/jk80CMWgiYAcEMe9k9gD\\\",\\\"MC-KTVSQG7PBN\\\"]}],\\\"enable\_monitoring\_mode\\\":false}\"}","eventPayloadVersion":"v1","runtimeContext":"OPEN","scriptVersion":"ed24a66cfc901e9f66a77fcd7f6b6205","type":"APP","apiClientId":1780363,"privacyPurposes":[],"dataSharingAdjustments":{"protectedCustomerApprovalScopes":["read\_customer\_address","read\_customer\_email","read\_customer\_name","read\_customer\_personal\_data","read\_customer\_phone"],"dataSharingControls":["share\_all\_events"]},"dataSharingState":"unrestricted","enabledFlags":["9a3ed68a"]},{"id":"164856178","eventPayloadVersion":"1","runtimeContext":"LAX","scriptVersion":"1","type":"CUSTOM","privacyPurposes":["ANALYTICS","MARKETING","SALE\_OF\_DATA"],"name":"Fueled - Pixel 2.0"},{"id":"shopify-app-pixel","configuration":"{}","eventPayloadVersion":"v1","runtimeContext":"STRICT","scriptVersion":"0460","apiClientId":"shopify-pixel","type":"APP","privacyPurposes":["ANALYTICS","MARKETING"]},{"id":"shopify-custom-pixel","eventPayloadVersion":"v1","runtimeContext":"LAX","scriptVersion":"0460","apiClientId":"shopify-pixel","type":"CUSTOM","privacyPurposes":["ANALYTICS","MARKETING"]}],isMerchantRequest: false,initData: {"shop":{"name":"Beardbrand","paymentSettings":{"currencyCode":"USD"},"myshopifyDomain":"beardbrand.myshopify.com","countryCode":"US","storefrontUrl":"https:\/\/www.beardbrand.com"},"customer":null,"cart":null,"checkout":null,"productVariants":[],"products":[{"id":"15015071285618","handle":"custom-mens-cologne-set","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61705930080626","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"4348228567123","handle":"beard-combs","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"60677800886642","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"4348241477715","handle":"beard-brush","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"31154464063571","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"6587291336787","handle":"tweezers","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"39396765859923","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"4348902506579","handle":"trimming-scissors","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"31550479695955","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14842545471858","handle":"temple-smoke-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61488701210994","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14843422966130","handle":"norse-winter-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61488418324850","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"15012645896562","handle":"black-sails-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61694826250610","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14842236240242","handle":"bold-fortune-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61488433463666","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14842523713906","handle":"old-money-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61488592191858","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938225344882","handle":"old-money-beard-oil","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510413943154","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14937464897906","handle":"bold-fortune-beard-oil","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61502826840434","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"1353927262291","handle":"alliance-membership","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"27845715066963","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938229637490","handle":"temple-smoke-beard-oil","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510425739634","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14935756931442","handle":"norse-winter-beard-oil","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61499057078642","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957581304178","handle":"old-money-utility-beard-softener","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540782506354","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958603567474","handle":"old-money-beard-balm","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544569733490","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938239566194","handle":"old-money-utility-beard-wash","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510455296370","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958600061298","handle":"bold-fortune-beard-balm","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544561344882","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"15012641833330","handle":"ghost-tracer-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61694807867762","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938227933554","handle":"tree-ranger-beard-oil","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510423347570","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938236354930","handle":"bold-fortune-utility-beard-wash","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510447432050","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"7432276279379","handle":"utility-beard-trimmer","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"42135547969619","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958586593650","handle":"norse-winter-beard-balm","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544521630066","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"15012632330610","handle":"desert-road-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61694775624050","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957586907506","handle":"temple-smoke-utility-beard-softener","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540809998706","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"4357382733907","handle":"book-of-reminders","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"31224674713683","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957582025074","handle":"tree-ranger-utility-beard-softener","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540786667890","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958675427698","handle":"temple-smoke-beard-balm","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544675672434","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938234225010","handle":"old-money-styling-paste","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510438125938","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"15012593303922","handle":"four-vices-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61694720115058","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957597163890","handle":"old-money-sea-salt-spray","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540857577842","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938231079282","handle":"bold-fortune-styling-paste","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510429081970","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958726414706","handle":"bold-fortune-aluminum-free-deodorant","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544772567410","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938239861106","handle":"tree-ranger-utility-beard-wash","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510464405874","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957593264498","handle":"bold-fortune-sea-salt-spray","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540845879666","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938244710770","handle":"bold-fortune-utility-beard-softener","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510470205810","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958612709746","handle":"tree-ranger-beard-balm","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544655782258","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958729888114","handle":"old-money-aluminum-free-deodorant","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544777941362","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957600833906","handle":"temple-smoke-sea-salt-spray","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540892934514","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958730936690","handle":"temple-smoke-aluminum-free-deodorant","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544784200050","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938241958258","handle":"temple-smoke-utility-beard-wash","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510464831858","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958687519090","handle":"old-money-mustache-wax","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544696283506","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957599195506","handle":"tree-ranger-sea-salt-spray","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61540864622962","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14938235044210","handle":"tree-ranger-styling-paste","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61510439403890","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958560051570","handle":"old-money-utility-bar-soap-3-pack","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544438825330","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958730445170","handle":"tree-ranger-aluminum-free-deodorant","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544778760562","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958724907378","handle":"temple-smoke-mustache-wax","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544753725810","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14957693927794","handle":"bold-fortune-utility-bar-soap-3-pack","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61541212553586","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"15037603283314","handle":"short-game-mens-cologne","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61813947826546","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]},{"id":"14958723662194","handle":"tree-ranger-mustache-wax","title":"","vendor":"","type":null,"untranslatedTitle":null,"url":null,"remoteShopId":null,"variants":[{"id":"61544749138290","price":{"amount":0.0,"currencyCode":"USD"},"image":null,"sku":null,"title":null,"untranslatedTitle":null}]}],"purchasingCompany":null,"page":{"pageType":"cart","resourceId":null}},},"https://www.beardbrand.com/cdn","032da393w19368061p0cc732e2m671615c3",{"modern":"","legacy":""},{"trekkieShim":true,"apiClientId":"580111","pageType":"cart","shopId":"2090478","storefrontBaseUrl":"https:\/\/www.beardbrand.com","extensionBaseUrl":"https:\/\/extensions.shopifycdn.com\/cdn\/shopifycloud\/web-pixels-manager","surface":"storefront-renderer","enabledBetaFlags":"[\"d5bdd5d0\", \"f36ec97b\", \"2b8f910e\"]","isMerchantRequest":"false","hashVersion":"032da393w19368061p0cc732e2m671615c3","publish":"custom","events":"[[\"page\_viewed\",{}]]"});})();
window.ShopifyAnalytics = window.ShopifyAnalytics || {};
window.ShopifyAnalytics.meta = window.ShopifyAnalytics.meta || {};
window.ShopifyAnalytics.meta.currency = 'USD';
var meta = {"page":{"pageType":"cart","requestId":"d301d72c-6eec-44e1-903f-af721b86d8b6-1781460400"}};
for (var attr in meta) {
window.ShopifyAnalytics.meta[attr] = meta[attr];
}

(function () {
var customDocumentWrite = function(content) {
var jquery = null;
if (window.jQuery) {
jquery = window.jQuery;
} else if (window.Checkout && window.Checkout.$) {
jquery = window.Checkout.$;
}
if (jquery) {
jquery('body').append(content);
}
};
var hasLoggedConversion = function(token) {
if (token) {
return document.cookie.indexOf('loggedConversion=' + token) !== -1;
}
return false;
}
var setCookieIfConversion = function(token) {
if (token) {
var twoMonthsFromNow = new Date(Date.now());
twoMonthsFromNow.setMonth(twoMonthsFromNow.getMonth() + 2);
document.cookie = 'loggedConversion=' + token + '; expires=' + twoMonthsFromNow;
}
}
var trekkie = window.ShopifyAnalytics.lib = window.trekkie = window.trekkie || [];
window.ShopifyAnalytics.lib.trekkie = window.trekkie;
if (trekkie.integrations) {
return;
}
trekkie.methods = [
'identify',
'page',
'ready',
'track',
'trackForm',
'trackLink'
];
trekkie.factory = function(method) {
return function() {
var args = Array.prototype.slice.call(arguments);
args.unshift(method);
trekkie.push(args);
if (window.\_\_TREKKIE\_SHIM\_QUEUE && (method == 'track' || method == 'page')) {
try {
window.\_\_TREKKIE\_SHIM\_QUEUE.push({
from: 'trekkie-stub',
method: method,
args: args.slice(1)
});
} catch (e) {
// no-op
}
}
return trekkie;
};
};
for (var i = 0; i < trekkie.methods.length; i++) {
var key = trekkie.methods[i];
trekkie[key] = trekkie.factory(key);
}
trekkie.load = function(config) {
trekkie.config = config || {};
trekkie.config.initialDocumentCookie = document.cookie;
var first = document.getElementsByTagName('script')[0];
var script = document.createElement('script');
script.type = 'text/javascript';
script.onerror = function(e) {
var scriptFallback = document.createElement('script');
scriptFallback.type = 'text/javascript';
scriptFallback.onerror = function(error) {
var Monorail = {
produce: function produce(monorailDomain, schemaId, payload) {
var currentMs = new Date().getTime();
var event = {
schema\_id: schemaId,
payload: payload,
metadata: {
event\_created\_at\_ms: currentMs,
event\_sent\_at\_ms: currentMs
}
};
return Monorail.sendRequest("https://" + monorailDomain + "/v1/produce", JSON.stringify(event));
},
sendRequest: function sendRequest(endpointUrl, payload) {
// Try the sendBeacon API
if (window && window.navigator && typeof window.navigator.sendBeacon === 'function' && typeof window.Blob === 'function' && !Monorail.isIos12()) {
var blobData = new window.Blob([payload], {
type: 'text/plain'
});
if (window.navigator.sendBeacon(endpointUrl, blobData)) {
return true;
} // sendBeacon was not successful
} // XHR beacon
var xhr = new XMLHttpRequest();
try {
xhr.open('POST', endpointUrl);
xhr.setRequestHeader('Content-Type', 'text/plain');
xhr.send(payload);
} catch (e) {
console.log(e);
}
return false;
},
isIos12: function isIos12() {
return window.navigator.userAgent.lastIndexOf('iPhone; CPU iPhone OS 12\_') !== -1 || window.navigator.userAgent.lastIndexOf('iPad; CPU OS 12\_') !== -1;
}
};
Monorail.produce('monorail-edge.shopifysvc.com',
'trekkie\_storefront\_load\_errors/1.1',
{shop\_id: 2090478,
theme\_id: 190866391410,
app\_name: "storefront",
context\_url: window.location.href,
source\_url: "//www.beardbrand.com/cdn/s/trekkie.storefront.370ef8ffef154dc56bb5a814fea4666724353464.min.js"});
};
scriptFallback.async = true;
scriptFallback.src = '//www.beardbrand.com/cdn/s/trekkie.storefront.370ef8ffef154dc56bb5a814fea4666724353464.min.js';
first.parentNode.insertBefore(scriptFallback, first);
};
script.async = true;
script.src = '//www.beardbrand.com/cdn/s/trekkie.storefront.370ef8ffef154dc56bb5a814fea4666724353464.min.js';
first.parentNode.insertBefore(script, first);
};
trekkie.load(
{"Trekkie":{"appName":"storefront","development":false,"defaultAttributes":{"shopId":2090478,"isMerchantRequest":null,"themeId":190866391410,"themeCityHash":"7446295004394335014","contentLanguage":"en","currency":"USD","eventMetadataId":"d9919564-9f55-46e4-a650-bb58d0a94d41"},"isServerSideCookieWritingEnabled":true,"monorailRegion":"shop\_domain","enabledBetaFlags":["b5387b81","d5bdd5d0"]},"Session Attribution":{},"S2S":{"facebookCapiEnabled":false,"source":"trekkie-storefront-renderer","apiClientId":580111}}
);
var loaded = false;
trekkie.ready(function() {
if (loaded) return;
loaded = true;
window.ShopifyAnalytics.lib = window.trekkie;
var originalDocumentWrite = document.write;
document.write = customDocumentWrite;
try { window.ShopifyAnalytics.merchantGoogleAnalytics.call(this); } catch(error) {};
document.write = originalDocumentWrite;
window.ShopifyAnalytics.lib.page(null,{"pageType":"cart","requestId":"d301d72c-6eec-44e1-903f-af721b86d8b6-1781460400","shopifyEmitted":true});
var match = window.location.pathname.match(/checkouts\/(.+)\/(thank\_you|post\_purchase)/)
var token = match? match[1]: undefined;
if (!hasLoggedConversion(token)) {
setCookieIfConversion(token);
}
});
var eventsListenerScript = document.createElement('script');
eventsListenerScript.async = true;
eventsListenerScript.src = "//www.beardbrand.com/cdn/shopifycloud/storefront/assets/shop\_events\_listener-4e26a9ce.js";
document.getElementsByTagName('head')[0].appendChild(eventsListenerScript);
})();

.site-nav.style--classic .submenu { padding-top: 24.5px; } .site-nav.style--classic .submenu:after { top: 24.5px; height: calc(100% - 24.5px) !important; } .site-nav.style--classic .submenu.mega-menu { padding-top: 94.5px; } .site-nav.style--classic .submenu.mega-menu:after { top: 24.5px; }@property --tw-translate-x{syntax:"\*";inherits:false;initial-value:0}@property --tw-translate-y{syntax:"\*";inherits:false;initial-value:0}@property --tw-translate-z{syntax:"\*";inherits:false;initial-value:0}@property --tw-rotate-x{syntax:"\*";inherits:false;initial-value:rotateX(0)}@property --tw-rotate-y{syntax:"\*";inherits:false;initial-value:rotateY(0)}@property --tw-rotate-z{syntax:"\*";inherits:false;initial-value:rotateZ(0)}@property --tw-skew-x{syntax:"\*";inherits:false;initial-value:skewX(0)}@property --tw-skew-y{syntax:"\*";inherits:false;initial-value:skewY(0)}@property --tw-space-y-reverse{syntax:"\*";inherits:false;initial-value:0}@property --tw-border-style{syntax:"\*";inherits:false;initial-value:solid}@property --tw-leading{syntax:"\*";inherits:false}@property --tw-font-weight{syntax:"\*";inherits:false}@property --tw-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-shadow-color{syntax:"\*";inherits:false}@property --tw-inset-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-inset-shadow-color{syntax:"\*";inherits:false}@property --tw-ring-color{syntax:"\*";inherits:false}@property --tw-ring-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-inset-ring-color{syntax:"\*";inherits:false}@property --tw-inset-ring-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-ring-inset{syntax:"\*";inherits:false}@property --tw-ring-offset-width{syntax:"<length>";inherits:false;initial-value:0}@property --tw-ring-offset-color{syntax:"\*";inherits:false;initial-value:#fff}@property --tw-ring-offset-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-outline-style{syntax:"\*";inherits:false;initial-value:solid}@property --tw-blur{syntax:"\*";inherits:false}@property --tw-brightness{syntax:"\*";inherits:false}@property --tw-contrast{syntax:"\*";inherits:false}@property --tw-grayscale{syntax:"\*";inherits:false}@property --tw-hue-rotate{syntax:"\*";inherits:false}@property --tw-invert{syntax:"\*";inherits:false}@property --tw-opacity{syntax:"\*";inherits:false}@property --tw-saturate{syntax:"\*";inherits:false}@property --tw-sepia{syntax:"\*";inherits:false}@property --tw-drop-shadow{syntax:"\*";inherits:false}@property --tw-duration{syntax:"\*";inherits:false}@property --tw-ease{syntax:"\*";inherits:false}@property --tw-space-x-reverse{syntax:"\*";inherits:false;initial-value:0}@keyframes spin{to{transform:rotate(360deg)}}@property --tw-translate-x{syntax:"\*";inherits:false;initial-value:0}@property --tw-translate-y{syntax:"\*";inherits:false;initial-value:0}@property --tw-translate-z{syntax:"\*";inherits:false;initial-value:0}@property --tw-rotate-x{syntax:"\*";inherits:false;initial-value:rotateX(0)}@property --tw-rotate-y{syntax:"\*";inherits:false;initial-value:rotateY(0)}@property --tw-rotate-z{syntax:"\*";inherits:false;initial-value:rotateZ(0)}@property --tw-skew-x{syntax:"\*";inherits:false;initial-value:skewX(0)}@property --tw-skew-y{syntax:"\*";inherits:false;initial-value:skewY(0)}@property --tw-space-y-reverse{syntax:"\*";inherits:false;initial-value:0}@property --tw-border-style{syntax:"\*";inherits:false;initial-value:solid}@property --tw-leading{syntax:"\*";inherits:false}@property --tw-font-weight{syntax:"\*";inherits:false}@property --tw-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-shadow-color{syntax:"\*";inherits:false}@property --tw-inset-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-inset-shadow-color{syntax:"\*";inherits:false}@property --tw-ring-color{syntax:"\*";inherits:false}@property --tw-ring-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-inset-ring-color{syntax:"\*";inherits:false}@property --tw-inset-ring-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-ring-inset{syntax:"\*";inherits:false}@property --tw-ring-offset-width{syntax:"<length>";inherits:false;initial-value:0}@property --tw-ring-offset-color{syntax:"\*";inherits:false;initial-value:#fff}@property --tw-ring-offset-shadow{syntax:"\*";inherits:false;initial-value:0 0 #0000}@property --tw-outline-style{syntax:"\*";inherits:false;initial-value:solid}@property --tw-blur{syntax:"\*";inherits:false}@property --tw-brightness{syntax:"\*";inherits:false}@property --tw-contrast{syntax:"\*";inherits:false}@property --tw-grayscale{syntax:"\*";inherits:false}@property --tw-hue-rotate{syntax:"\*";inherits:false}@property --tw-invert{syntax:"\*";inherits:false}@property --tw-opacity{syntax:"\*";inherits:false}@property --tw-saturate{syntax:"\*";inherits:false}@property --tw-sepia{syntax:"\*";inherits:false}@property --tw-drop-shadow{syntax:"\*";inherits:false}@property --tw-duration{syntax:"\*";inherits:false}@property --tw-ease{syntax:"\*";inherits:false}@property --tw-space-x-reverse{syntax:"\*";inherits:false;initial-value:0}@keyframes spin{to{transform:rotate(360deg)}}{}.richpanel-app-modal-container{width:100%;height:100%;top:0px;left:0px;position:fixed;z-index:2147483647}.richpanel-app-modal-container.hide{display:none}.richpanel-app-modal-container\_\_bg{position:absolute;background-color:rgba(0,0,0,.5);width:100%;height:100%;cursor:pointer;display:block !important}.richpanel-app-modal-container\_\_cross{width:19px;height:19px;position:absolute;top:30px;right:30px;cursor:pointer}.richpanel-app-modal-container\_\_cross svg{fill:#fff}.richpanel-app-modal-container\_\_content{position:absolute;left:50%;top:50%;transform:translate(-50%, -50%);width:90%;height:90%;display:flex;justify-content:center;align-items:center}@import url(https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Inter:wght@400;500;600;700&display=swap);.rp-micro-app-messenger{position:fixed;width:375px;max-width:100%;border-radius:12px;overflow:hidden;box-sizing:border-box;font-weight:400;box-shadow:0 18px 48px rgba(26,26,26,.12),0 2px 8px rgba(26,26,26,.08);display:flex;flex-direction:column;background-color:#f8f5f1;border:1px solid #e0dbd4;font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;z-index:2236374112}@media only screen and (min-device-width: 320px)and (max-device-width: 480px){.rp-micro-app-messenger{top:0 !important;bottom:0 !important;left:0 !important;right:0 !important;height:unset !important;width:auto;border:0;border-radius:0;box-shadow:none;max-height:unset !important}}.rp-micro-app-messenger-header\_\_start{border-top-right-radius:12px;border-top-left-radius:12px;height:214px;font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}@media only screen and (min-device-width: 320px)and (max-device-width: 480px){.rp-micro-app-messenger-header\_\_start{border-top-right-radius:0px;border-top-left-radius:0px}}.rp-micro-app-fade-enter-active{transition:opacity 180ms ease,transform 180ms ease;transform-origin:bottom right}.rp-micro-app-fade-enter{opacity:0;transform:translateY(10px) scale(0.98)}.rp-micro-app-fade-enter-to{opacity:1;transform:translateY(0) scale(1)}.rp-micro-app-fade-leave-active{transition:opacity 160ms ease,transform 160ms ease;transform-origin:bottom right}.rp-micro-app-fade-leave-to{opacity:0;transform:translateY(10px) scale(0.98)}.rp-micro-app-messenger-header\_\_start-title{font-family:"Instrument Serif",Georgia,serif;font-weight:400;font-size:36px;line-height:1.08;margin:0;-webkit-animation-duration:.5s;animation-duration:.5s;white-space:nowrap;overflow:hidden;max-width:300px;text-overflow:ellipsis;color:#fff}.rp-micro-app-messenger-header\_\_start-message{max-width:300px;max-height:65px;overflow:hidden;margin:.3rem auto;font-weight:200;font-size:14px;line-height:1.4;-webkit-animation-duration:.75s;animation-duration:.75s;overflow-wrap:break-word;word-wrap:break-word;word-break:break-word;opacity:1;text-align:left;margin-left:0;color:rgba(255,255,255,.9);font-weight:400}.rp-micro-app-messenger-mobile-close-trigger{position:absolute;right:7px;top:12px;width:48px;height:48px;align-items:center;justify-content:center;display:none}.rp-micro-app-messenger-mobile-close-trigger .rp-micro-app-cross-icon{width:15px;height:15px}.rp-micro-app-messenger-mobile-close-trigger .rp-micro-app-cross-icon path{stroke:#fff}.rp-micro-app-messenger-mobile-close-trigger .rp-micro-app-cross-icon.dark path{stroke:#000}@media only screen and (min-device-width: 320px)and (max-device-width: 480px){.rp-micro-app-messenger-mobile-close-trigger{display:flex}}.rp-micro-app-loading-spinner{position:absolute;z-index:2000;top:0;right:0;bottom:0;left:0;margin:0;display:block;width:100%;height:100%;max-width:100%;max-height:100%;min-height:0;overflow:hidden;border-radius:inherit;box-sizing:border-box;contain:layout paint;background:var(--rp-micro-loader-bg, #fbf7f2);font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.rp-micro-app-loading-spinner,.rp-micro-app-loading-spinner \*{box-sizing:border-box}.rp-micro-app-loader{width:100%;height:100%;max-width:100%;display:flex;flex-direction:column;overflow:hidden;border-radius:inherit;background:var(--rp-micro-loader-bg, #fbf7f2)}.rp-micro-app-loader\_\_header{flex:0 0 214px;height:214px;padding:16px 32px 0;overflow:hidden;background:var(--rp-micro-loader-accent, #004e96)}.rp-micro-app-loader\_\_header--gradient{background-image:linear-gradient(135deg, var(--rp-micro-loader-accent-light) 0%, var(--rp-micro-loader-accent-dark) 100%)}.rp-micro-app-loader\_\_topbar,.rp-micro-app-loader\_\_reply,.rp-micro-app-loader\_\_avatars{display:flex;align-items:center}.rp-micro-app-loader\_\_topbar{justify-content:space-between;min-height:30px;margin-bottom:16px}.rp-micro-app-loader\_\_lang-pill{width:76px;height:28px;margin-left:auto;margin-right:12px;border-radius:8px;border:1px solid rgba(255,255,255,.35);background:rgba(255,255,255,.1)}.rp-micro-app-loader\_\_mark{width:20px;height:20px;border-radius:6px;background:rgba(255,255,255,.28)}.rp-micro-app-loader\_\_close{width:22px;height:22px;position:relative;opacity:.72}.rp-micro-app-loader\_\_close::before,.rp-micro-app-loader\_\_close::after{content:"";position:absolute;top:10px;left:0;width:22px;height:2px;border-radius:999px;background:rgba(255,255,255,.78)}.rp-micro-app-loader\_\_close::before{transform:rotate(45deg)}.rp-micro-app-loader\_\_close::after{transform:rotate(-45deg)}.rp-micro-app-loader\_\_hero-line,.rp-micro-app-loader\_\_reply-line,.rp-micro-app-loader\_\_line{position:relative;overflow:hidden;border-radius:999px;background:linear-gradient(90deg, rgba(236, 229, 220, 0.82) 0%, rgba(250, 246, 240, 0.98) 48%, rgba(236, 229, 220, 0.82) 100%);background-size:220% 100%;animation:rp-micro-app-loading-shimmer 1.35s ease-in-out infinite}.rp-micro-app-loader\_\_hero-line,.rp-micro-app-loader\_\_reply-line{background:linear-gradient(90deg, rgba(255, 255, 255, 0.22) 0%, rgba(255, 255, 255, 0.46) 48%, rgba(255, 255, 255, 0.22) 100%);background-size:220% 100%}.rp-micro-app-loader\_\_hero-line--title{width:54%;height:38px;margin-bottom:12px}.rp-micro-app-loader\_\_hero-line--copy{width:78%;height:16px;margin-bottom:16px}.rp-micro-app-loader\_\_reply{width:100%;height:40px;padding:7px 16px;border-radius:10px;background:rgba(255,255,255,.14);box-sizing:border-box}.rp-micro-app-loader\_\_avatars{flex:0 0 auto;margin-right:12px}.rp-micro-app-loader\_\_avatar{width:26px;height:26px;margin-left:-8px;border:1px solid rgba(255,255,255,.8);border-radius:999px;background:linear-gradient(135deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.58))}.rp-micro-app-loader\_\_avatar:first-child{margin-left:0}.rp-micro-app-loader\_\_reply-line{width:62%;height:14px}.rp-micro-app-loader\_\_clock{width:14px;height:14px;margin-left:8px;border-radius:999px;background:rgba(255,255,255,.42)}.rp-micro-app-loader\_\_body{flex:1 1 auto;min-height:0;overflow:hidden;padding:18px 20px 20px;box-sizing:border-box}.rp-micro-app-loader\_\_card{width:100%;padding:22px 20px;border:1px solid #e0dbd4;border-radius:12px;background:#fff;box-sizing:border-box;overflow:hidden}.rp-micro-app-loader\_\_line{width:66%;height:10px;margin-bottom:8px}.rp-micro-app-loader\_\_line--title{width:58%;height:18px;margin-bottom:18px}.rp-micro-app-loader\_\_line--wide{width:86%}@media only screen and (max-device-width: 480px)and (min-device-width: 320px){.rp-micro-app-loader\_\_header{flex-basis:214px;height:214px;padding:16px 32px 0}.rp-micro-app-loader\_\_topbar{margin-bottom:16px}.rp-micro-app-loader\_\_hero-line--title{width:58%;height:38px;margin-bottom:12px}.rp-micro-app-loader\_\_hero-line--copy{width:80%;height:16px;margin-bottom:16px}.rp-micro-app-loader\_\_reply{height:40px;padding:7px 12px}.rp-micro-app-loader\_\_body{padding:16px 14px}.rp-micro-app-loader\_\_card{padding:20px 18px}}@keyframes rp-micro-app-loading-shimmer{0%{background-position:120% 0}100%{background-position:-120% 0}}.rp-micro-app-dummy-icon{height:60px;width:60px;background:#004e96;border-radius:60px;cursor:pointer;max-width:300px;-webkit-box-shadow:rgba(0,0,0,.16) 0px 5px 40px;box-shadow:rgba(0,0,0,.16) 0px 5px 40px;-webkit-transition:width .6s;transition:width .6s;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.rp-micro-app-dummy-icon.miansai-logo{background-image:url(//cdn.shopify.com/s/files/1/1994/2941/files/chat\_icon\_thicker\_300x.png?v=3240152291644892867);background-size:98% 98%;background-position:1px 1px;background-repeat:no-repeat;box-shadow:none !important;background-color:transparent !important}.rp-micro-app-dummy-icon.miansai-logo .rp-micro-app-icon{display:none}.rp-micro-app-dummy-icon.rp-badge-logo{align-items:center !important}.rp-micro-app-dummy-icon.rp-badge-logo .rp-micro-app-icon{display:none}.rp-micro-app-dummy-icon .rp-micro-app-cross-icon{display:none;width:17px;height:17px}.rp-micro-app-dummy-icon .rp-micro-app-cross-icon path{stroke:#fff}.rp-micro-app-dummy-icon .rp-micro-app-cross-icon.dark path{stroke:#000}.rp-micro-app-icon{height:44px;width:42.181px;position:absolute}.rp-micro-app-icon svg{height:44px;width:44.181px;fill:#fff;filter:drop-shadow(0px 2px 1px rgba(0, 0, 0, 0.3))}.rp-micro-app-icon svg path,.rp-micro-app-icon svg rect{fill:#fff !important;stroke:#fff !important}.rp-micro-app-icon.dark svg path,.rp-micro-app-icon.dark svg rect{fill:#424242 !important;stroke:#424242 !important}.rp-micro-app-label-icon{height:100%;width:100%;display:flex;justify-content:center;align-items:center}.rp-micro-app-label-icon svg{height:100%;width:100%;fill:#fff}.rp-micro-app-label-icon svg path{fill:none !important}.rp-micro-app-label-icon svg rect{fill:none}.rp-micro-app-label-icon.dark svg path{fill:#424242 !important}.rp-micro-app-label-icon.rp-icon-light svg path{fill:#fff !important}.rp-micro-app-dummy-icon-container{border:none;position:fixed;max-width:421px;z-index:2147483646;user-select:none;box-sizing:border-box;padding:20px}.rp-micro-app-dummy-icon-container.rp-micro-app-opened .rp-micro-app-dummy-icon .rp-micro-app-icon,.rp-micro-app-dummy-icon-container.rp-micro-app-opened .rp-micro-app-dummy-icon .rp-micro-app-label-icon{display:none}.rp-micro-app-dummy-icon-container.rp-micro-app-opened .rp-micro-app-dummy-icon .rp-micro-app-cross-icon{display:flex;justify-content:center;align-items:center}@media only screen and (min-device-width: 320px)and (max-device-width: 480px){.rp-micro-app-dummy-icon-container.rp-micro-app-opened .rp-micro-app-dummy-icon{display:none}}.rp-micro-app-label-icon-container{display:flex;align-items:center}.rp-micro-app-hide{display:none !important;opacity:0;visibility:hidden}
@import 'https://fonts.googleapis.com/css2?family=Bebas+Neue:ital,wght@0,400&family=Nunito+Sans:ital,wght@0,200;0,300;0,400;0,600;0,700;0,800;0,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&family=Space+Grotesk:ital,wght@0,400;0,700&display=swap';
@import 'https://use.typekit.net/faq1tcb.css';
@font-face {
font-family: 'HW\_Pano\_Bold';
src: url(https://cdn.shopify.com/s/files/1/0209/0478/files/HW\_Pano\_Bold.woff?v=1689187304);
font-weight: 400;
font-style: normal;
font-display: swap;
}
@font-face {
font-family: 'Pano';
src: url(https://cdn.shopify.com/s/files/1/0209/0478/t/249/assets/HW\_Pano\_Bold.woff?v=150975146254878240241652822236);
font-weight: 700;
font-style: normal;
font-display: swap;
}
@font-face {
font-family: 'Poppins-Klaviyo-Hosted';
src: url(https://static.klaviyo.com/onsite/hosted-fonts/Poppins/latin/poppins\_latin\_italic\_400.woff2);
font-weight: 400;
font-style: italic;
font-display: swap;
}
@font-face {
font-family: 'Poppins-Klaviyo-Hosted';
src: url(https://static.klaviyo.com/onsite/hosted-fonts/Poppins/latin/poppins\_latin\_italic\_700.woff2);
font-weight: 700;
font-style: italic;
font-display: swap;
}
@font-face {
font-family: 'Poppins-Klaviyo-Hosted';
src: url(https://static.klaviyo.com/onsite/hosted-fonts/Poppins/latin/poppins\_latin\_regular\_400\_2.woff2);
font-weight: 400;
font-style: normal;
font-display: swap;
}
@font-face {
font-family: 'Poppins-Klaviyo-Hosted';
src: url(https://static.klaviyo.com/onsite/hosted-fonts/Poppins/latin/poppins\_latin\_regular\_700.woff2);
font-weight: 700;
font-style: normal;
font-display: swap;
}
.rc\_theme--avenue .rc-container,.rc\_theme--avenue .rc-container label{font-size:15px}.rc\_theme--avenue .rc-radio\_\_input:before{display:none}.rc\_theme--avenue .rc-selling-plans\_\_dropdown{background:#fff;min-width:204px;font-size:15px;border:1px solid #ccc}.rc\_theme--pacific .rc-selling-plans\_\_dropdown{appearance:auto}.rc\_theme--envy .rc-option{padding:10px}.rc\_theme--envy .rc-option input[type=radio]{display:none}.rc\_theme--envy .rc-selling-plans\_\_dropdown{padding:10px}.rc\_theme--vantage .rc-selling-plans{margin-bottom:40px}.rc\_theme--vantage .rc-selling-plans\_\_dropdown{padding:10px 28px 10px 18px}.rc\_theme--california .rc-radio\_\_label:after{display:none}.rc\_theme--reach .site-main{z-index:auto}div.rc\_popup{display:block;padding:8px;white-space:nowrap}div.rc\_block\_\_type--active+div.rc\_popup{margin-top:8px}.rc\_popup\_label\_wrapper{background:rgba(0,0,0,0);border:0;outline:0}.rc\_popup\_label\_wrapper:focus{outline:.2rem solid var(--rc-active-color)}div.rc\_popup\_\_hover,a.rc\_popup\_\_hover{display:inline-flex;align-items:center;position:relative;padding-bottom:12px;cursor:pointer}div.rc\_popup\_\_block{display:none;position:absolute;top:100%;cursor:default;left:0;text-align:left;white-space:initial}div.rc\_popup\_\_block.active{display:block}div.rc\_popup\_\_hover:hover .rc\_popup\_\_block,div.rc\_popup\_\_block:hover{display:block}div.rc\_popup\_\_hover--mobile div.rc\_popup\_\_block:hover{display:none}div.rc\_popup\_\_block{width:300px;padding:0}div.rc\_popup\_\_close{display:block;width:40px;height:40px;position:absolute;top:0;right:0;color:#fff;font-size:23px;text-align:center;line-height:40px;z-index:300;cursor:pointer;font-family:arial}div.rc\_popup\_\_block\_\_content a{text-decoration:none}#rc\_login{display:block;width:100%;text-align:center;margin:20px auto}.rc\_popup\_\_hover a[data-v-7bc675e0]{text-decoration:none}.rc\_popup\_\_hover[data-v-7bc675e0]:after{display:none;content:"";width:1px;border:10px solid rgba(0,0,0,0);position:absolute;top:18px;border-bottom-color:var(--backgroundColor)}.rc\_popup\_\_hover[data-v-7bc675e0]:hover:after{display:block}.rc\_popup\_\_block[data-v-7bc675e0]:before{border-bottom-color:var(--backgroundColor)}.rc\_popup\_\_block\_\_content[data-v-7bc675e0]{padding-bottom:8px}.rc\_popup\_\_block[data-v-7bc675e0]{font-size:12px;padding:12px;z-index:1000}.rc\_popup\_\_label[data-v-7bc675e0]{padding-left:8px}.rc\_popup\_\_block\_\_footer[data-v-7bc675e0]{display:flex;justify-content:flex-end}.reload-icon[data-v-7bc675e0]{height:16px;width:16px;color:var(--rc-icon-color)}.tooltip-badge[data-v-7bc675e0]{font-size:12px;display:inline-flex;justify-content:center;align-items:center;background-color:#fff;border-radius:50px;padding:4px 12px}.tooltip-badge .powered-by[data-v-7bc675e0]{color:#191d48;font-weight:400;padding-right:4px}.tooltip-badge svg[data-v-7bc675e0]{color:#191d48;width:5em}.rc-selling-plans\_\_label[data-v-335eb9f1]{cursor:initial}.rc-selling-plans\_\_label[data-v-7965ef98]{cursor:initial}.rc-template\_\_legacy-radio .rc-radio{display:block;white-space:nowrap;padding:8px}.rc-template\_\_legacy-radio .rc-radio+.rc-radio{padding-top:0}.rc-template\_\_legacy-radio .rc-radio.rc-option\_\_subsave{padding-bottom:0}.rc-template\_\_legacy-radio .rc-radio\_\_input,.rc-template\_\_legacy-radio .rc-radio\_\_label{display:inline;vertical-align:middle}.rc-template\_\_legacy-radio .rc\_widget\_\_option\_\_selector+.rc-selling-plans{padding-left:30px;padding-bottom:8px}.rc-checkbox{display:inline-flex;align-items:center;vertical-align:top;cursor:pointer;margin-bottom:0}.rc-checkbox\_\_input{width:16px}.rc-checkbox\_\_input:focus{outline:0}.rc-checkbox\_\_label{margin-inline-start:8px;line-height:2}.rc-radio{display:inline-flex;align-items:center;vertical-align:top;cursor:pointer;margin-bottom:0}.rc-radio\_\_input{width:16px}.rc-radio\_\_input:focus{outline:0}.rc-radio\_\_label{margin-left:8px;line-height:2}.rc-template\_\_button-group .rc-radio{border:1px solid #ccc;border-radius:10px;padding:12px 20px;text-align:center;flex:1 1 50%}.rc-template\_\_button-group .rc-radio.rc-option--active{box-shadow:0px 0px 0px 1px #ccc}.rc-template\_\_button-group .rc-radio:first-child{margin-right:4px;border-top-right-radius:0;border-bottom-right-radius:0}.rc-template\_\_button-group .rc-radio:nth-child(2){border-top-left-radius:0;border-bottom-left-radius:0}.rc-template\_\_button-group .rc-radio .rc-radio\_\_input{border:0px;clip:rect(0px, 0px, 0px, 0px);height:1px;width:1px;margin:-1px;padding:0px;overflow:hidden;white-space:nowrap;position:absolute}.rc-template\_\_button-group .rc-radio .rc-radio\_\_input:focus-visible+.rc-radio\_\_label{outline:.2rem solid var(--rc-active-color);outline-offset:.3rem}.rc-template\_\_button-group .rc-radio .rc-radio\_\_label{margin-left:0;line-height:1;width:100%}.rc-template\_\_button-group .rc-radio .rc-option\_\_price{display:block;font-weight:bold;font-size:20px;margin-top:8px}.rc-template\_\_button-group .rc-button-group\_\_options{justify-content:center}.rc-template\_\_button-group .rc-radio-group\_\_options{display:flex;justify-content:center}.rc-template\_\_button-group .rc-radio-group\_\_options+.rc-selling-plans{margin-top:12px}.rc-template\_\_checkbox{padding:0 8px}.rc-template\_\_checkbox .rc-option\_\_text,.rc-template\_\_checkbox .rc-option\_\_discount{font-weight:bold}.rc-widget .rc-template\_\_checkbox .rc-option\_\_discount{padding-right:0}.rc-template\_\_radio-group .rc-radio-group\_\_options{overflow:hidden}.rc-template\_\_radio-group .rc-radio{display:flex;padding:8px 20px}.rc-template\_\_radio-group .rc-radio:not(:first-child){border-top:1px solid #ccc}.rc-template\_\_radio-group .rc-radio .rc-radio\_\_input{min-height:0}.rc-template\_\_radio-group .rc-radio.rc-option\_\_subsave .rc-radio\_\_label{font-weight:bold}.rc-template\_\_radio-group .rc-radio .rc-radio\_\_label{display:flex}.rc-template\_\_radio-group .rc-radio .rc-radio\_\_label .rc-option\_\_text{order:2}.rc-template\_\_radio-group .rc-radio .rc-radio\_\_label .rc-option\_\_discount{order:3}.rc-template\_\_radio-group .rc-radio .rc-radio\_\_label .rc-option\_\_price{order:1;font-weight:bold;margin-right:16px}.rc-template\_\_radio-group .rc-radio-group\_\_options{border:1px solid #ccc;border-radius:10px}.rc-template\_\_radio-group .rc-radio-group\_\_options+.rc-selling-plans{margin-top:16px;font-weight:bold}.rc-container{margin-bottom:.5em}.rc-widget{color:var(--rc-color)}.rc-widget .rc-option--active{color:var(--rc-active-color);background-color:var(--rc-active-bg)}.rc-widget .rc-option\_\_text,.rc-widget .rc-option\_\_discount{padding-right:4px}.rc-widget label{color:inherit}:root{--rc-color: #040404;--rc-active-bg: #efefef;--rc-active-color: #000000}.visually-hidden{border:0px;clip:rect(0px, 0px, 0px, 0px);height:1px;width:1px;margin:-1px;padding:0px;overflow:hidden;white-space:nowrap;position:absolute}


if ('loading' in HTMLImageElement.prototype) {
document.body.classList.add('loading-support');
}

[Skip to content](#main)

[**40% Off Cologne Sets**](/products/custom-mens-cologne-set)
announcement-bar {
background-color: #101010;
color: #f9f8f6 !important;
}
announcement-bar a {
color: #f9f8f6 !important;
text-decoration: none;
}
announcement-bar svg \* {
fill: #f9f8f6;
}
.announcement-bar\_\_text {
display: inline-flex;
align-items: center;
}
.announcement-bar\_\_text p {
margin: 0;
}
.announcement-bar\_\_icon {
margin-left: 8px;
display: inline-flex;
align-items: center;
transition: transform 0.2s ease;
}
.announcement-bar\_\_link:hover .announcement-bar\_\_icon,
.announcement-bar\_\_link:focus .announcement-bar\_\_icon {
transform: translateX(2px);
}
.announcement\_\_exit {
background: transparent;
border: 0;
padding: 0;
cursor: pointer;
color: #f9f8f6;
}



Go to Home Page[![Beardbrand logo](//www.beardbrand.com/cdn/shop/files/circle-beard__101010.svg?v=1766173834)](/)
/\* Default (static) values \*/:root {
--header-logo: 56px;
--header-size: 96px;
}
@media screen and (max-width: 480px){
:root {
--header-logo: 30px;
--header-size: 60px !important;
}
}

const fixVhByVars = function(){
const maxDeskHeight = parseInt( document.getElementById('header-size-settings').dataset.max\_desk\_height ),
maxMobileHeight = parseInt( document.getElementById('header-size-settings').dataset.max\_mobile\_height );
const addMoreToWindow =
( document.querySelector('announcement-bar') && document.querySelector('announcement-bar').style.display != "none" ? document.querySelector('announcement-bar').offsetHeight : 0 ) +
( document.querySelector('nav.breadcrumb') ? document.querySelector('nav.breadcrumb').offsetHeight : 0 );
if ( window.innerWidth < 480 ) {
document.documentElement.style.setProperty('--header-padding', `15px`);
document.documentElement.style.setProperty('--header-logo', `${maxMobileHeight}px`);
document.documentElement.style.setProperty('--header-size', `${parseInt( maxMobileHeight + ( 15 \* 2 ) )}px`);
document.documentElement.style.setProperty('--window-height', `${parseInt( 1 + document.documentElement.clientHeight - maxMobileHeight - ( 15 \* 2 ) ) - addMoreToWindow}px`);
} else {
document.documentElement.style.setProperty('--header-padding', `20px`);
document.documentElement.style.setProperty('--header-logo', `${maxDeskHeight}px`);
document.documentElement.style.setProperty('--header-size', `${parseInt( maxDeskHeight + ( 20 \* 2 ) )}px`);
document.documentElement.style.setProperty('--window-height', `${parseInt( 1 + document.documentElement.clientHeight - maxDeskHeight - ( 20 \* 2 ) ) - addMoreToWindow}px`);
}
}
window.addEventListener('resize', debounce(fixVhByVars, 200));
window.addEventListener('DOMContentLoaded', fixVhByVars);
fixVhByVars();

* [Shop](/collections)


  + [Condition](#)




    - [Beard Oil](/collections/beard-oil)
    - [Beard Balm](/collections/beard-balm)
    - [Utility Beard Softener](/collections/utility-beard-softener)
  + [Cleanse](#)




    - [Utility Beard Wash](/collections/utility-beard-wash)
    - [Utility Bar Soap](/collections/utility-bar-soap)
  + [Fragrance](#)




    - [Men's Cologne](/collections/mens-cologne)
    - [Utility Deodorant](/collections/aluminum-free-deodorant)
  + [Style](#)




    - [Styling Paste](/collections/styling-paste)
    - [Sea Salt Spray](/collections/sea-salt-spray)
    - [Mustache Wax](/collections/mustache-wax)
  + [Tools & Gear](#)




    - [Utility Beard Trimmer](/products/utility-beard-trimmer)
    - [Combs, Brushes & Tools](/collections/combs-brushes-tools)
    - [Book of Reminders](/products/book-of-reminders)
    - [Alliance Membership](/products/alliance-membership)
* [Deals](/collections/current-deals)
* [Beard](/collections/beard)
* [Hair](/collections/hair)
* [Body](/collections/body)
* [Fragrances](/pages/fragrances)

Open search


Open cart
[0](/cart "Open cart")

Open menu

var ad = localStorage.getItem('announcement-dismissed');
if (false && ad === 'true') {
document.querySelector('.site-header').style.marginTop = '0';
document.querySelector('body').classList.remove('show-announcement-bar');
} else {
document.querySelector('.box\_\_banner').style.display = 'block';
document.querySelector('.site-header').style.marginTop = '34px';
document.querySelector('body').classList.add('show-announcement-bar');
fixVhByVars();
}

document.addEventListener('DOMContentLoaded', function() {
// Cache the rendered icon HTML so we can swap between them.
const plusIconHTML = `<svg class="plus\_icon\_mobile\_menu" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="30" height="30">
<path d="M12 4v16M4 12h16" stroke="#F9F8F6" stroke-width="2" stroke-linecap="round"/>
</svg>`;
const closeIconHTML = `<svg class="close\_icon\_mobile\_menu" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="30" height="30">
<path d="M6 6l12 12M6 18L18 6" stroke="#F9F8F6" stroke-width="2" stroke-linecap="round"/>
</svg>`;
// Helper to set open/closed state on a menuItem
function setSubmenuState(menuItem, open) {
const submenu = menuItem.querySelector('.babymenu');
const icon = menuItem.querySelector('.icon');
const titleEl = menuItem.querySelector('.menu-link .underline-animation');
const titleText = titleEl ? titleEl.textContent.trim() : 'submenu';
if (!submenu) return;
if (open) {
menuItem.classList.add('active');
submenu.style.display = 'block';
menuItem.setAttribute('aria-expanded', 'true');
submenu.setAttribute('aria-hidden', 'false');
if (icon) {
icon.innerHTML = closeIconHTML;
icon.setAttribute('aria-label', `Close ${titleText} submenu`);
}
} else {
menuItem.classList.remove('active');
submenu.style.display = 'none';
menuItem.setAttribute('aria-expanded', 'false');
submenu.setAttribute('aria-hidden', 'true');
if (icon) {
icon.innerHTML = plusIconHTML;
icon.setAttribute('aria-label', `Open ${titleText} submenu`);
}
}
}
// Toggle convenience
function toggleMenu(menuItem) {
const isActive = menuItem.classList.contains('active');
setSubmenuState(menuItem, !isActive);
}
// Click delegation
document.addEventListener('click', function(e) {
const icon = e.target.closest('.site-nav.style--sidebar .icon');
if (!icon) return;
const menuItem = icon.closest('.mega-link');
const submenu = menuItem ? menuItem.querySelector('.babymenu') : null;
if (menuItem && submenu) {
e.preventDefault();
e.stopPropagation();
toggleMenu(menuItem);
}
});
// Keyboard support (Enter / Space)
document.addEventListener('keydown', function(e) {
if (e.key !== 'Enter' && e.key !== ' ') return;
const icon = e.target.closest('.site-nav.style--sidebar .icon');
if (!icon) return;
const menuItem = icon.closest('.mega-link');
const submenu = menuItem ? menuItem.querySelector('.babymenu') : null;
if (menuItem && submenu) {
e.preventDefault();
toggleMenu(menuItem);
}
});
});


Close sidebar

Menu

* [Shop](/collections)


  + [Shop All](/collections)
  + [Condition](#)




    - [Beard Oil](/collections/beard-oil)
    - [Beard Balm](/collections/beard-balm)
    - [Utility Beard Softener](/collections/utility-beard-softener)
  + [Cleanse](#)




    - [Utility Beard Wash](/collections/utility-beard-wash)
    - [Utility Bar Soap](/collections/utility-bar-soap)
  + [Fragrance](#)




    - [Men's Cologne](/collections/mens-cologne)
    - [Utility Deodorant](/collections/aluminum-free-deodorant)
  + [Style](#)




    - [Styling Paste](/collections/styling-paste)
    - [Sea Salt Spray](/collections/sea-salt-spray)
    - [Mustache Wax](/collections/mustache-wax)
  + [Tools & Gear](#)




    - [Utility Beard Trimmer](/products/utility-beard-trimmer)
    - [Combs, Brushes & Tools](/collections/combs-brushes-tools)
    - [Book of Reminders](/products/book-of-reminders)
    - [Alliance Membership](/products/alliance-membership)
* [Deals](/collections/current-deals)
* [Beard](/collections/beard)
* [Hair](/collections/hair)
* [Body](/collections/body)
* [Fragrances](/pages/fragrances)
* [Account](https://www.beardbrand.com/customer_authentication/redirect?locale=en&region_country=US)

© 2026 [Beardbrand](/)

Shopping Cart
=============

➤ Free US Shipping with orders $75+ USD

Subscribe and save 17% every single time.

#cart-page-subtitle {
margin-bottom: 0px!important;
opacity: var(--alternate-opacity);
}

Your cart is currently empty.

[Start shopping](/pages/build-a-custom-kit)

 #shopify-section-template--27795702612338\_\_main {border-bottom: solid 1px; } #shopify-section-template--27795702612338\_\_main #AJAX-checkout-button {display: block; width: 100%;}

#section-template--27795702612338\_\_1652484034e78ce879 {
--main-background: #f9f8f6;
}
#section-template--27795702612338\_\_1652484034e78ce879 {
--main-text: #101010;
--main-text-foreground: #fff;
--main-background-secondary: rgba(16, 16, 16, 0.18);
--main-borders: #101010;
}

WANT MORE?
----------

#section-text-columns-with-icons {
--main-background: #f9f8f6;
}
#section-text-columns-with-icons {
--main-text: #101010;
--main-text-foreground: #fff;
--main-background-secondary: rgba(16, 16, 16, 0.18);
--main-borders: #101010;
}

### Beardbrand Assurance

#### Get Free US Shipping

On orders of $75 or more.

#### Swaps Are Always Free

If a product or fragrance doesn’t work for you, we’ll get you one that does.

#### Formulated with Love

Non-endocrine disrupting products that work with your body’s natural chemistry.

#section-custom-newsletter {
--main-background: #f9f8f6;
}
#section-custom-newsletter {
--main-text: #101010;
--main-text-foreground: #fff;
--main-background-secondary: rgba(16, 16, 16, 0.18);
--main-borders: #101010;
}

Grow Your Mind
--------------

.custom-newsletter-container {
background-color: #F9F8F6;
padding: var(--box-smaller-padding);
border-top: 1px solid #101010;
display: flex;
justify-content: center;
flex-wrap: wrap;
text-align: left;
align-items: center;
}
.custom-newsletter-title {
color: #101010;
margin: 0 30px 0 0;
white-space: nowrap;
font-size: calc(60px / 60 \* var(--base-headings-size) + 0px);
line-height: 1;
padding: 0;
display: flex;
align-items: center;
}
.custom-newsletter-form {
display: flex;
align-items: center;
max-width: 500px;
width: auto;
flex-grow: 0;
}
.input-group {
display: flex;
align-items: center;
}
.custom-newsletter-form input[type="email"] {
padding: 5px 10px !important;
border: 1px solid #101010 !important;
font-size: 18px;
height: 40px !important;
box-sizing: border-box;
width: 250px;
}
.custom-newsletter-form .alert {
margin-bottom: 0em;
}
.custom-newsletter-form button {
background-color: #101010;
color: #F9F8F6;
padding: 0 !important;
border: 1px solid #101010;
cursor: pointer;
height: 40px !important;
width: 40px !important;
display: flex;
align-items: center;
justify-content: center;
flex-shrink: 0;
max-width: 40px;
}
.custom-newsletter-form button .button-content {
display: flex;
align-items: center;
justify-content: center;
width: 24px;
height: 24px;
}
.custom-newsletter-form button svg {
width: 100%;
height: 100%;
display: block;
}
@media screen and (max-width: 1106px) {
.custom-newsletter-container {
flex-direction: column;
text-align: left;
align-items: flex-start;
}
.custom-newsletter-title {
font-size: calc(42px / 60 \* var(--base-headings-size) + 0px);
white-space: normal;
text-align: left;
margin-bottom: 30px;
}
.custom-newsletter-form {
width: auto;
align-items: flex-start;
}
.custom-newsletter-form input[type="email"],
.custom-newsletter-form button {
width: auto;
margin-bottom: 10px;
}
.custom-newsletter-form input[type="email"] {
width: 250px;
}
.custom-newsletter-form button {
padding: 10px 0;
max-width: 80px;
}
}
@media screen and (min-width: 1107px) {
.custom-newsletter-container {
flex-direction: row;
align-items: center;
justify-content: center;
text-align: left;
}
.custom-newsletter-title {
font-size: calc(60px / 60 \* var(--base-headings-size) + 0px);
white-space: nowrap;
margin-top: 10px;
}
.custom-newsletter-form {
max-width: 500px;
align-items: center;
}
}
@media screen and (min-width: 1367px) {
.custom-newsletter-title {
font-size: calc(60px / 60 \* var(--base-headings-size) + 0px);
}
}
@media screen and (min-width: 1024px) and (max-width: 1367px) {
.custom-newsletter-title {
font-size: calc(50px / 60 \* var(--base-headings-size) + 0px);
}
}
@media screen and (min-width: 768px) and (max-width: 1024px) {
.custom-newsletter-title {
font-size: calc(50px / 60 \* var(--base-headings-size) + 0px);
}
}
@media screen and (max-width: 768px) {
.custom-newsletter-title {
font-size: calc(48px / 60 \* var(--base-headings-size) + 0px);
}
}
@media (max-width: 600px) {
.custom-newsletter-title {
font-size: calc(42px / 60 \* var(--base-headings-size) + 0px);
}
}

#section-footer {
--main-background: #f9f8f6;
}
#section-footer {
--main-text: #101010;
--main-text-foreground: #fff;
--main-background-secondary: rgba(16, 16, 16, 0.18);
--main-borders: #101010;
}
@media screen and (min-width: 1020px) {
#section-footer .footer-bottom.footer-bottom--has-badge {
display: grid;
grid-template-columns: minmax(320px, max-content) 1fr;
align-items: start;
column-gap: 40px;
}
#section-footer .footer-bottom\_\_badge {
justify-self: start;
align-self: start;
min-width: 320px;
width: max-content;
}
#section-footer .footer-bottom\_\_right {
justify-self: end;
display: flex;
flex-direction: column;
align-items: flex-end;
width: max-content;
text-align: right;
row-gap: 20px;
}
#section-footer .footer-bottom\_\_right > \* {
width: 100%;
align-self: flex-end;
margin: 0;
}
#section-footer .footer-bottom\_\_social {
display: flex;
justify-content: flex-end;
width: 100%;
margin: 0;
}
#section-footer .footer-bottom\_\_localization,
#section-footer .footer-bottom\_\_copyright,
#section-footer .footer-bottom\_\_copyright .footer-copyright,
#section-footer .footer-bottom\_\_copyright .site-payment,
#section-footer .footer-bottom\_\_copyright .site-copyright,
#section-footer .footer-bottom\_\_copyright .copyright-text {
text-align: right;
width: 100%;
margin: 0;
}
#section-footer .footer-bottom\_\_localization .localization-form-holder,
#section-footer .footer-bottom\_\_localization .localization-form,
#section-footer .footer-bottom\_\_localization form {
display: flex;
flex-direction: column;
align-items: flex-end;
justify-content: flex-end;
}
#section-footer .footer-bottom\_\_localization .localization-form\_\_item,
#section-footer .footer-bottom\_\_localization .localization-form\_\_item > span {
text-align: right;
}
}
@media screen and (max-width: 1019px) {
#section-footer .footer-bottom {
display: grid;
grid-template-columns: 1fr;
align-items: start !important;
justify-items: start;
text-align: left;
row-gap: 20px;
}
#section-footer .footer-bottom > div:first-child {
margin-bottom: 0 !important;
margin-right: 0 !important;
}
#section-footer .footer-bottom\_\_right {
display: contents;
}
#section-footer .footer-bottom\_\_badge {
grid-row: 1;
justify-self: start;
align-self: start;
width: 100%;
min-width: 320px;
max-width: 100%;
margin: 0;
}
#section-footer .footer-bottom\_\_social {
grid-row: 2;
display: flex;
justify-content: flex-start;
width: 100%;
margin: 0;
}
#section-footer .footer-bottom\_\_localization {
grid-row: 3;
width: 100%;
text-align: left;
margin: 0;
}
#section-footer .footer-bottom\_\_copyright {
grid-row: 4;
width: 100%;
text-align: left;
margin: 0;
}
#section-footer .footer-bottom\_\_copyright,
#section-footer .footer-bottom\_\_copyright .footer-copyright,
#section-footer .footer-bottom\_\_copyright .site-payment,
#section-footer .footer-bottom\_\_copyright .site-copyright,
#section-footer .footer-bottom\_\_copyright .copyright-text {
text-align: left !important;
margin: 0;
}
#section-footer .footer-bottom\_\_localization .localization-form-holder,
#section-footer .footer-bottom\_\_localization .localization-form,
#section-footer .footer-bottom\_\_localization form {
display: flex;
flex-direction: column;
align-items: flex-start;
justify-content: flex-start;
}
#section-footer .footer-bottom\_\_localization .localization-form\_\_item,
#section-footer .footer-bottom\_\_localization .localization-form\_\_item > span {
text-align: left;
}
}

### Shoppers with Disabilities Toggle Shoppers with Disabilities content

If you are vision-impaired or have any impairment covered by the Americans with Disabilities Act or a similar law, and you wish to discuss potential accommodations related to using this website, please contact us at 844-662-3273 ext 0 or [contact us here](https://beardbrand.customerdesk.io/#rp-customer-widget-home "Contact us on Beardbrand's customer service dashboard (opens in a new tab)").

### Beardbrand Toggle Beardbrand content

[Beardbrand Barbershop](https://www.beardbrandbarbershop.com/)
[About Us](/pages/learn-about-us)
[Ingredient Glossary](/pages/ingredient-glossary)
[Terms of Use, Privacy Policy & Trademarks](/pages/legal)
[Beardbrand Logo](/pages/beardbrand-logo)

### Community Toggle Community content

[Account Login](https://account.beardbrand.com/orders?locale=en&region_country=US&buyer_flags=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJiZWFyZGJyYW5kLm15c2hvcGlmeS5jb20iLCJmbGFncyI6W10sImV4cCI6MTc4MjA2NTIwMCwibmJmIjoxNzgxNDYwNDAwfQ.RP4amA8r8ASk29_T-qQZV8RDd2wiQtLAcTswPHYc6R8)
[Returns & Exchanges](/pages/returns-exchanges)
[FAQs](/pages/faqs)
[Contact Us](https://beardbrand.customerdesk.io/)
[Alliance Forums](https://alliance.beardbrand.com/login)
[Affiliate Program](/pages/affiliates)
[Urban Beardsman Blog](/blogs/urbanbeardsman)

.site-footer .regular-select-cover {
background-image: url("data:image/svg+xml,%0A%3Csvg width='14' height='9' viewBox='0 0 14 9' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M8.42815 7.47604L7.01394 8.89025L0.528658 2.40497L1.94287 0.990753L8.42815 7.47604Z' fill='rgb(16, 16, 16)'/%3E%3Cpath d='M6.98591 8.89025L5.5717 7.47604L12.057 0.990755L13.4712 2.40497L6.98591 8.89025Z' fill='rgb(16, 16, 16)'/%3E%3C/svg%3E%0A");
}

Country/region



United States
(USD $)

* Albania
  (ALL L)
* Andorra
  (EUR €)
* Angola
  (USD $)
* Antigua & Barbuda
  (XCD $)
* Argentina
  (USD $)
* Aruba
  (AWG ƒ)
* Australia
  (AUD $)
* Austria
  (EUR €)
* Bahamas
  (BSD $)
* Bangladesh
  (BDT ৳)
* Barbados
  (BBD $)
* Belgium
  (EUR €)
* Belize
  (BZD $)
* Benin
  (XOF Fr)
* Bermuda
  (USD $)
* Bhutan
  (USD $)
* Bolivia
  (BOB Bs.)
* Bosnia & Herzegovina
  (BAM КМ)
* Botswana
  (BWP P)
* Brazil
  (USD $)
* British Virgin Islands
  (USD $)
* Brunei
  (BND $)
* Bulgaria
  (EUR €)
* Burkina Faso
  (XOF Fr)
* Burundi
  (BIF Fr)
* Cambodia
  (KHR ៛)
* Cameroon
  (XAF CFA)
* Canada
  (CAD $)
* Caribbean Netherlands
  (USD $)
* Cayman Islands
  (KYD $)
* Central African Republic
  (XAF CFA)
* Chad
  (XAF CFA)
* Chile
  (USD $)
* China
  (CNY ¥)
* Colombia
  (USD $)
* Congo - Brazzaville
  (XAF CFA)
* Congo - Kinshasa
  (CDF Fr)
* Costa Rica
  (CRC ₡)
* Croatia
  (EUR €)
* Curaçao
  (ANG ƒ)
* Cyprus
  (EUR €)
* Czechia
  (CZK Kč)
* Denmark
  (DKK kr.)
* Djibouti
  (DJF Fdj)
* Dominica
  (XCD $)
* Dominican Republic
  (DOP $)
* Ecuador
  (USD $)
* Egypt
  (EGP ج.م)
* El Salvador
  (USD $)
* Equatorial Guinea
  (XAF CFA)
* Eritrea
  (USD $)
* Estonia
  (EUR €)
* Eswatini
  (USD $)
* Ethiopia
  (ETB Br)
* Falkland Islands
  (FKP £)
* Fiji
  (FJD $)
* Finland
  (EUR €)
* France
  (EUR €)
* French Guiana
  (EUR €)
* Gabon
  (XOF Fr)
* Gambia
  (GMD D)
* Georgia
  (USD $)
* Germany
  (EUR €)
* Ghana
  (USD $)
* Gibraltar
  (GBP £)
* Greece
  (EUR €)
* Grenada
  (XCD $)
* Guadeloupe
  (EUR €)
* Guatemala
  (GTQ Q)
* Guernsey
  (GBP £)
* Guyana
  (GYD $)
* Haiti
  (USD $)
* Honduras
  (HNL L)
* Hong Kong SAR
  (HKD $)
* Hungary
  (HUF Ft)
* Iceland
  (ISK kr)
* India
  (INR ₹)
* Indonesia
  (IDR Rp)
* Ireland
  (EUR €)
* Italy
  (EUR €)
* Jamaica
  (JMD $)
* Japan
  (JPY ¥)
* Jersey
  (USD $)
* Kazakhstan
  (KZT ₸)
* Kenya
  (KES KSh)
* Laos
  (LAK ₭)
* Latvia
  (EUR €)
* Lesotho
  (USD $)
* Liberia
  (USD $)
* Libya
  (USD $)
* Liechtenstein
  (CHF CHF)
* Lithuania
  (EUR €)
* Luxembourg
  (EUR €)
* Macao SAR
  (MOP P)
* Madagascar
  (USD $)
* Malawi
  (MWK MK)
* Maldives
  (MVR MVR)
* Mali
  (XOF Fr)
* Malta
  (EUR €)
* Martinique
  (EUR €)
* Mauritius
  (MUR ₨)
* Mayotte
  (EUR €)
* Monaco
  (EUR €)
* Mongolia
  (MNT ₮)
* Montenegro
  (EUR €)
* Montserrat
  (XCD $)
* Morocco
  (MAD د.م.)
* Mozambique
  (USD $)
* Myanmar (Burma)
  (MMK K)
* Namibia
  (USD $)
* Netherlands
  (EUR €)
* New Caledonia
  (XPF Fr)
* New Zealand
  (NZD $)
* Nicaragua
  (NIO C$)
* Niger
  (XOF Fr)
* Nigeria
  (NGN ₦)
* Niue
  (NZD $)
* Norway
  (USD $)
* Pakistan
  (PKR ₨)
* Panama
  (USD $)
* Papua New Guinea
  (PGK K)
* Paraguay
  (PYG ₲)
* Peru
  (PEN S/)
* Philippines
  (PHP ₱)
* Poland
  (PLN zł)
* Portugal
  (EUR €)
* Réunion
  (EUR €)
* Romania
  (RON Lei)
* Rwanda
  (RWF FRw)
* Senegal
  (XOF Fr)
* Serbia
  (RSD РСД)
* Sierra Leone
  (SLL Le)
* Singapore
  (SGD $)
* Sint Maarten
  (ANG ƒ)
* Slovakia
  (EUR €)
* Slovenia
  (EUR €)
* Somalia
  (USD $)
* South Africa
  (USD $)
* South Korea
  (KRW ₩)
* Spain
  (EUR €)
* Sri Lanka
  (LKR ₨)
* St. Barthélemy
  (EUR €)
* St. Kitts & Nevis
  (XCD $)
* St. Lucia
  (XCD $)
* St. Vincent & Grenadines
  (XCD $)
* Suriname
  (USD $)
* Sweden
  (SEK kr)
* Switzerland
  (CHF CHF)
* Taiwan
  (TWD $)
* Tanzania
  (TZS Sh)
* Thailand
  (THB ฿)
* Timor-Leste
  (USD $)
* Togo
  (XOF Fr)
* Trinidad & Tobago
  (TTD $)
* Turks & Caicos Islands
  (USD $)
* Tuvalu
  (AUD $)
* Uganda
  (UGX USh)
* United Kingdom
  (GBP £)
* United States
  (USD $)
* Uruguay
  (UYU $U)
* Vanuatu
  (VUV Vt)
* Vatican City
  (EUR €)
* Venezuela
  (USD $)
* Vietnam
  (VND ₫)
* Zambia
  (USD $)
* Zimbabwe
  (USD $)

© 2026 [Beardbrand](/)  
1003 E 52nd St, Austin TX 78751

document.addEventListener('DOMContentLoaded', function() {
const isMobile = () => window.innerWidth <= 1019;
if (isMobile()) {
const style = document.createElement('style');
style.textContent = `
@media (max-width: 1019px) {
.footer-item .footer-content,
.footer-item .footer-menu {
display: none;
}
}
`;
document.head.appendChild(style);
}
function initializeFooter() {
const footerItems = document.querySelectorAll('.footer-item');
footerItems.forEach(item => {
const header = item.querySelector('h3');
if (!header) return;
const content = item.querySelector('.footer-content, .footer-menu');
if (content && isMobile()) {
content.style.display = 'none';
}
const newHeader = header.cloneNode(true);
header.parentNode.replaceChild(newHeader, header);
newHeader.addEventListener('click', function(e) {
if (!isMobile()) return;
e.preventDefault();
const currentItem = this.closest('.footer-item');
const plusIcon = this.querySelector('.plus\_icon\_mobile\_menu');
const closeIcon = this.querySelector('.close\_icon\_mobile\_menu');
footerItems.forEach(otherItem => {
if (otherItem !== currentItem && otherItem.classList.contains('active')) {
otherItem.classList.remove('active');
const otherContent = otherItem.querySelector('.footer-content, .footer-menu');
const otherHeader = otherItem.querySelector('h3');
const otherPlusIcon = otherItem.querySelector('.plus\_icon\_mobile\_menu');
const otherCloseIcon = otherItem.querySelector('.close\_icon\_mobile\_menu');
if (otherContent) {
otherContent.style.display = 'none';
otherHeader.setAttribute('aria-expanded', 'false');
}
if (otherPlusIcon && otherCloseIcon) {
otherPlusIcon.classList.remove('hidden');
otherCloseIcon.classList.add('hidden');
}
}
});
const isExpanding = !currentItem.classList.contains('active');
currentItem.classList.toggle('active');
if (plusIcon && closeIcon) {
plusIcon.classList.toggle('hidden');
closeIcon.classList.toggle('hidden');
}
this.setAttribute('aria-expanded', isExpanding);
if (content) {
content.style.display = isExpanding ? 'block' : 'none';
}
});
newHeader.addEventListener('keydown', function(e) {
if (e.key === 'Enter' || e.key === ' ') {
e.preventDefault();
this.click();
}
});
});
}
initializeFooter();
const debounce = (func, wait) => {
let timeout;
return function executedFunction(...args) {
const later = () => {
clearTimeout(timeout);
func(...args);
};
clearTimeout(timeout);
timeout = setTimeout(later, wait);
};
};
const handleResize = debounce(function() {
const footerItems = document.querySelectorAll('.footer-item');
if (!isMobile()) {
footerItems.forEach(item => {
item.classList.remove('active');
const content = item.querySelector('.footer-content, .footer-menu');
const header = item.querySelector('h3');
if (content) {
content.style.display = 'block';
}
if (header) {
header.setAttribute('aria-expanded', 'false');
}
});
} else {
footerItems.forEach(item => {
const content = item.querySelector('.footer-content, .footer-menu');
if (content && !item.classList.contains('active')) {
content.style.display = 'none';
const plusIcon = item.querySelector('.plus\_icon\_mobile\_menu');
const closeIcon = item.querySelector('.close\_icon\_mobile\_menu');
if (plusIcon && closeIcon) {
plusIcon.classList.remove('hidden');
closeIcon.classList.add('hidden');
}
}
});
}
}, 250);
window.addEventListener('resize', handleResize);
});

Close sidebar

Search

Search

window.preloadImages = (element=document)=> {
let lazyImages = element.querySelectorAll('img.lazy');
for (let img of lazyImages) {
if (!img.complete) {
img.addEventListener('load', lazyImageLoad, false);
} else if (img.complete) {
lazyImageLoad({currentTarget: img});
}
}
function lazyImageLoad(e) {
e.currentTarget.removeEventListener('load', lazyImageLoad);
e.currentTarget.classList.add('lazyloaded');
if ( e.currentTarget.id && e.currentTarget.id.includes('responsive-background') ) {
ribSetSize(e.currentTarget)
}
}
}
window.preloadImages();
KROWN = {
settings: {
shop\_money\_format: '${{amount}}',
cart\_action: "no-overlay",
routes: {
cart\_url: "/cart",
cart\_add\_url: "/cart/add",
cart\_change\_url: "/cart/change",
predictive\_search\_url: "/search/suggest",
product\_recommendations\_url: "/recommendations/products"
},
locales: {
cart\_add\_error: `Max amount of {{ title }} are in your cart.`,
cart\_general\_error: `There was an error. Please refresh the page and try again.`,
products\_add\_to\_cart\_button: `Add to cart`,
products\_sold\_out\_variant: `Unavailable`,
products\_unavailable\_variant: `Unavailable`,
products\_one\_product: `There is only one product left!`,
products\_few\_products: `There are {{ count }} products left`,
products\_no\_products: `There are no products left`,
products\_preorder: `This product is out of stock, but you can still order it.`,
product\_sku: `SKU`,
product\_barcode: `ISBN`,
product\_no\_reviews: `There are no reviews for this product. Be the first to leave one!`,
next: `Next`,
prev: `Previous`
},
symbols: {
arrow: ``,
zoom\_out: `<svg width="21" height="21" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="9.08008" cy="9" r="8" stroke="var(--main-text)" stroke-width="2" style="fill:#F9F8F6;" /><rect x="14.2988" y="15.9062" width="1.98612" height="6.65426" transform="rotate(-45 14.2988 15.9062)" fill="#111111"/><path d="M13.0801 8V10L5.08008 10L5.08008 8L13.0801 8Z" fill="#111111"/></svg>`,
zoom\_in: `<svg width="21" height="21" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="9.08008" cy="9" r="8" stroke="var(--main-text)" stroke-width="2" style="fill:#F9F8F6;" /><rect x="14.2988" y="15.9062" width="1.98612" height="6.65426" transform="rotate(-45 14.2988 15.9062)" fill="#111111"/><path d="M8.08008 5H10.0801V13H8.08008V5Z" fill="#111111"/><path d="M13.0801 8V10L5.08008 10L5.08008 8L13.0801 8Z" fill="#111111"/></svg>`,
close: `<svg aria-hidden="true" focusable="false" role="presentation" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.41418 0L16.9705 15.5563L15.5563 16.9706L-2.89679e-05 1.41421L1.41418 0Z" fill="#111111"/><path d="M16.9706 1.41431L1.41423 16.9707L1.85966e-05 15.5564L15.5564 9.31025e-05L16.9706 1.41431Z" fill="#111111"/></svg>`,
star: `<svg width="18" height="17" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9 0L11.0206 6.21885H17.5595L12.2694 10.0623L14.2901 16.2812L9 12.4377L3.70993 16.2812L5.73056 10.0623L0.440492 6.21885H6.97937L9 0Z" fill="#262627"/></svg>`,
toggle\_pack: `<svg class="svg symbol symbol--plus" width="12" height="13" viewBox="0 0 12 13" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 0.5H7V12.5H5V0.5Z" fill="#262627"/><path d="M12 5.5V7.5L0 7.5L1.19209e-07 5.5L12 5.5Z" fill="#262627"/></svg><svg class="svg symbol symbol--minus" width="12" height="13" viewBox="0 0 12 3" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 0.5V2.5L0 2.5L1.19209e-07 0.5L12 0.5Z" fill="#262627"/></svg>`
},
predictive\_search\_enabled: "true",
predictive\_search\_placeholder: `<a class="search-item blank"><div class="thumbnail"></div><div class="content"><span class="title"></span><span class="caption"></span></div></a><a class="search-item blank"><div class="thumbnail"></div><div class="content"><span class="title"></span><span class="caption"></span></div></a><a class="search-item blank"><div class="thumbnail"></div><div class="content"><span class="title"></span><span class="caption"></span></div></a>`
}
}
if ( ! JSON.parse(document.getElementById('shopify-features').text).predictiveSearch ) {
KROWN.settings.predictive\_search\_enabled = "false";
document.getElementById('site-search-handle').setAttribute('id', '');
}
if ( 'ontouchstart' in window || window.DocumentTouch && document instanceof DocumentTouch ) {
document.querySelector('body').classList.remove('no-touchevents');
document.querySelector('body').classList.add('touchevents');
}



Close sidebar

#modal-popup {
--main-text: #2b2e30;
--main-text-foreground: #fff;
}#modal-popup {
--main-background: #f3efe2;
}




window.Shopify.loadFeatures([{ name: 'consent-tracking-api', version: '0.1' }], function(error) {
if (error) {
console.warn('Consent tracking API failed to load:', error);
return;
}
const trackingAllowed = Shopify.customerPrivacy.userCanBeTracked();
if (!trackingAllowed) return;
// === FBCLID → \_fbc (Meta enhancement) ===
// Start FBCLID Capture Snippet Code
(function() {
const generateFbc = (fbclid) => 'fb.1.' + Date.now() + '.' + fbclid;
const fbclid = new URLSearchParams(window.location.search).get('fbclid');
if (fbclid) {
document.cookie = '\_fbc=' + generateFbc(fbclid) +
'; path=/; domain=.beardbrand.com; max-age=7776000; samesite=lax';
}
})();
// End FBCLID Capture Snippet Code
// === PostPilot SiteMatch Pixel ===
var script = document.createElement('script');
script.src = 'https://xp2023-pix.s3.amazonaws.com/px\_SkE8m.js';
document.head.appendChild(script);
});
 .shopify-cleanslate .DnvZqPMEvBFbBre5UuP9 {background-color: #101010 !important; border-color: #101010 !important;} 

.recharge-theme {
/\* App \*/
--recharge-app-background: #F9F8F6;
--recharge-app-container: 850px;
--recharge-app-vertical-padding: 32px;
/\* Brand colors \*/
--recharge-color-brand: #101010;
/\* Tints \*/
--recharge-color-brand-120: #000000;
--recharge-color-brand-20: #404040;
--recharge-color-brand-40: #707070;
--recharge-color-brand-60: #9f9f9f;
--recharge-color-brand-75: #c3c3c3;
--recharge-color-brand-85: #dbdbdb;
/\* Neutral \*/
--recharge-color-neutral: hsl(0, 35%, 7%);
--recharge-color-neutral-80: hsl(0, 7%, 25%);
--recharge-color-neutral-70: hsl(0, 5%, 35%);
--recharge-color-neutral-40: hsl(0, 3%, 63%);
--recharge-color-neutral-10: hsl(0, 2%, 91%);
/\* Links \*/
--recharge-button-secondary: #101010;
--recharge-button-secondary-120: #000000;
--recharge-button-secondary-60: #707070;
/\* Images \*/
--recharge-images-ratio: 1;
/\* Cards \*/
--recharge-cards-background: #F9F8F6;
--recharge-cards-border-color: #101010;
/\* Fonts \*/
--recharge-typography-scale: 16px;
--recharge-typography-size-1: calc(3 \* var(--recharge-typography-scale));
--recharge-typography-size-2: calc(2.25 \* var(--recharge-typography-scale));
--recharge-typography-size-3: calc(1.625 \* var(--recharge-typography-scale));
--recharge-typography-size-4: calc(1.25 \* var(--recharge-typography-scale));
--recharge-typography-size-5: calc(1 \* var(--recharge-typography-scale));
--recharge-typography-size-6: calc(.875 \* var(--recharge-typography-scale));
/\*\* Text \*\*/
--recharge-typography-light: #FFFFFF;
--recharge-typography-primary: var(--recharge-color-neutral);
--recharge-typography-secondary: var(--recharge-color-neutral-70);
/\* Corners \*/
--recharge-corners-radius: 16px;
/\* Button corners \*/
--recharge-button-border-radius: calc(var(--recharge-corners-radius) \* 1.5);
/\* Views \*/
--recharge-views-background: #F9F8F6;
/\* Buttons \*/
--recharge-button-font-family: inherit;
--recharge-button-brand: var(--recharge-color-brand);
--recharge-button-color: #F9F8F6;
}

(function () {
window.RechargeStorefrontConfig = {
customer: null,
shop: {
currency: "USD",
locale: "en",
identifier: "beardbrand.myshopify.com",
market\_id: 7053738067,
currency\_format: "${{amount}}",
routes: {
cart: "\/cart",
root: "\/",
},
},
cart\_overlay:{"enabled":true},
cart\_overlay\_preview:{},
cart\_drawer:{"config":{"config":{"cross\_sell":{"enabled":true,"config\_list":[{"trigger":{"type":"any"},"cross\_sell":{"type":"specific\_products","products":[{"id":"14958730445170","handle":"tree-ranger-aluminum-free-deodorant","variant\_ids":["61544778760562"],"purchase\_option":"onetime\_only","frequency\_selection":"customer"},{"id":"14958729888114","handle":"old-money-aluminum-free-deodorant","variant\_ids":["61544777941362"],"purchase\_option":"onetime\_only","frequency\_selection":"customer"},{"id":"14958726414706","handle":"bold-fortune-aluminum-free-deodorant","variant\_ids":["61544772567410"],"purchase\_option":"onetime\_only","frequency\_selection":"customer"},{"id":"14958730936690","handle":"temple-smoke-aluminum-free-deodorant","variant\_ids":["61544784200050"],"purchase\_option":"onetime\_only","frequency\_selection":"customer"}],"number\_of\_products":4}}]},"upsell\_cart\_items":true,"shipping\_progress\_bar":{"enabled":true,"required\_amount":"75","required\_amount\_type":"discounted","subscriptions\_unlock\_free\_shipping":false}},"settings":{"theme":{"link\_color":"#467c99","error\_color":"#EC3D10","muted\_color":"rgba(43, 46, 48, 1)","accent\_color":"rgba(16, 16, 16, 1)","padding\_left":48,"border\_radius":"square","padding\_right":48,"primary\_color":"rgba(229, 255, 82, 1)","secondary\_color":"rgba(16, 16, 16, 1)","background\_color":"rgba(249, 248, 246, 1)","foreground\_color":"rgba(16, 16, 16, 1)","primary\_foreground\_color":"rgba(16, 16, 16, 1)","secondary\_foreground\_color":"rgba(249, 248, 246, 1)"},"advanced":{"selectors":{"add\_to\_cart":"product-quick-view button.product\_\_add-to-cart[name=\"add\"],\nbutton.product\_\_add-to-cart[name=\"add\"],\n.product--add-to-cart-button\n","cart\_trigger":"#site-cart-handle,.site-cart-handle a,.site-cart-handle","cart\_count\_enabled":false,"add\_to\_cart\_enabled":true,"cart\_trigger\_enabled":true,"add\_to\_cart\_override\_type":"manual"},"drawer\_settings":{"z\_index":9999,"z\_index\_enabled":true,"drawer\_width\_enabled":false}},"templates":{"empty":{"body":{"blocks":[{"type":"text\_area","settings":{"text":"\u003ch3\u003e\u003cstrong\u003eYour cart is empty.\u003c\/strong\u003e\u003c\/h3\u003e","padding\_top":0,"padding\_bottom":25}},{"type":"empty\_cart\_button","settings":{"button\_text":"START SHOPPING","redirect\_url":"https:\/\/www.beardbrand.com\/collections","button\_action":"redirect"}}],"alignment":"top","padding\_top":32,"padding\_bottom":0},"footer":{"blocks":[],"padding\_top":20,"padding\_bottom":20,"section\_divider":"shadow","background\_color":"#FFFFFF"},"header":{"blocks":[{"type":"cart\_title","settings":{"title":"\u003ch3\u003eCART ({{items\_count}})\u003c\/h3\u003e","padding\_top":32,"padding\_bottom":16}},{"type":"shipping\_progress\_bar","settings":{"icon":"https:\/\/static.rechargecdn.com\/merchant-image-library\/YzNiZTMyN2ZiMw\/images\/MzdlYzU4ZWZmYw","show\_icon":true,"padding\_top":25,"completed\_text":"\u003cp style=\"text-align: center\"\u003e🎉 \u003cstrong\u003eCongrats—you've unlocked free shipping!\u003c\/strong\u003e\u003c\/p\u003e","padding\_bottom":25,"background\_color":"rgba(249, 248, 246, 1)","in\_progress\_text":"\u003cp style=\"text-align: center\"\u003e\u003cstrong\u003eYou're {{amount}} away from free USA shipping.\u003c\/strong\u003e\u003c\/p\u003e","divider\_placement":"top","show\_divider\_line":false,"bar\_background\_color":"rgba(243, 239, 226, 1)","bar\_foreground\_color":"rgba(43, 46, 48, 1)"}}],"show\_divider\_line":false}},"line\_items":{"body":{"blocks":[{"type":"line\_items","settings":{"upsell":{"display\_type":"button","text\_discount":"SUBSCRIBE TO SAVE {{discount}}","text\_no\_discount":"Upgrade to a subscription","frequency\_select\_label":"Deliver every","show\_onetime\_frequency":true,"onetime\_frequency\_label":"One-time","upsell\_in\_progress\_text":"Upgrading to subscription...","text\_discount\_quantity\_upsell":"Subscribe and buy {{quantity}}, save {{discount}}!"},"padding\_top":16,"savings\_text":"Saving {{discount}}","padding\_bottom":16,"show\_divider\_line":false,"show\_savings\_text":true,"show\_strikethrough\_price":true}},{"type":"cross\_sell","settings":{"show\_title":true,"title\_text":"\u003ch4\u003eWANT MORE?\u003c\/h4\u003e","padding\_top":6,"padding\_bottom":48,"display\_options":"dropdown","card\_background\_color":"#F6F8FA","add\_to\_cart\_button\_text":"ADD","section\_background\_color":"rgba(249, 248, 246, 1)","display\_products\_on\_cards":false,"prompt\_one\_time\_option\_text":"One-time purchase","prompt\_add\_to\_cart\_button\_text":"ADD TO CART","prompt\_variant\_selection\_label":"Options","prompt\_frequency\_selection\_label":"Deliver every"}}],"alignment":"top","padding\_top":0,"padding\_bottom":0},"footer":{"blocks":[{"type":"subtotal","settings":{"padding\_top":0,"padding\_bottom":4,"subtotal\_text\_plural":"\u003cstrong\u003eSubtotal ({{items\_count}} items):\u003c\/strong\u003e","subtotal\_text\_singular":"\u003cstrong\u003eSubtotal ({{items\_count}} item):\u003c\/strong\u003e","show\_strikethrough\_price":true}},{"type":"checkout\_button","settings":{"padding\_top":31,"padding\_bottom":0,"checkout\_button\_text":"CHECKOUT"}}],"padding\_top":20,"padding\_bottom":48,"section\_divider":"none","background\_color":"rgba(249, 248, 246, 1)"},"header":{"blocks":[{"type":"cart\_title","settings":{"title":"\u003ch3\u003eCART ({{items\_count}})\u003c\/h3\u003e","padding\_top":32,"padding\_bottom":16,"show\_divider\_line":false}},{"type":"shipping\_progress\_bar","settings":{"icon":"https:\/\/static.rechargecdn.com\/merchant-image-library\/YzNiZTMyN2ZiMw\/images\/MzdlYzU4ZWZmYw","show\_icon":true,"padding\_top":25,"completed\_text":"\u003cp style=\"text-align: center\"\u003e🎉 \u003cstrong\u003eCongrats\u003c\/strong\u003e—\u003cstrong\u003eyou've unlocked free USA shipping!\u003c\/strong\u003e\u003c\/p\u003e","padding\_bottom":25,"background\_color":"rgba(249, 248, 246, 1)","in\_progress\_text":"\u003cp style=\"text-align: center\"\u003e\u003cstrong\u003eYou're {{amount}} away from free USA shipping.\u003c\/strong\u003e\u003c\/p\u003e","divider\_placement":"top","show\_divider\_line":false,"bar\_background\_color":"rgba(243, 239, 226, 1)","bar\_foreground\_color":"rgba(43, 46, 48, 1)"}}],"show\_divider\_line":false}}}},"passed\_activation\_ready\_schema":true,"flow\_id":506378},"enabled":true},
cart\_drawer\_preview:{"config":{"settings":{"advanced":{"drawer\_settings":{"drawer\_width\_enabled":false,"z\_index":9999,"z\_index\_enabled":true},"selectors":{"add\_to\_cart":"product-quick-view button.product\_\_add-to-cart[name=\"add\"],\nbutton.product\_\_add-to-cart[name=\"add\"],\n.product--add-to-cart-button\n","add\_to\_cart\_enabled":true,"add\_to\_cart\_override\_type":"manual","cart\_count\_enabled":false,"cart\_trigger":"#site-cart-handle,.site-cart-handle a,.site-cart-handle","cart\_trigger\_enabled":true}},"templates":{"empty":{"body":{"alignment":"top","blocks":[{"settings":{"padding\_bottom":25,"padding\_top":0,"text":"\u003ch3\u003e\u003cstrong\u003eYour cart is empty.\u003c\/strong\u003e\u003c\/h3\u003e"},"type":"text\_area"},{"settings":{"button\_action":"redirect","button\_text":"START SHOPPING","redirect\_url":"https:\/\/www.beardbrand.com\/collections"},"type":"empty\_cart\_button"}],"padding\_bottom":0,"padding\_top":32},"footer":{"background\_color":"#FFFFFF","blocks":[],"padding\_bottom":20,"padding\_top":20,"section\_divider":"shadow"},"header":{"blocks":[{"settings":{"padding\_bottom":16,"padding\_top":32,"title":"\u003ch3\u003eCART ({{items\_count}})\u003c\/h3\u003e"},"type":"cart\_title"},{"settings":{"background\_color":"rgba(249, 248, 246, 1)","bar\_background\_color":"rgba(243, 239, 226, 1)","bar\_foreground\_color":"rgba(43, 46, 48, 1)","completed\_text":"\u003cp style=\"text-align: center\"\u003e🎉 \u003cstrong\u003eCongrats—you've unlocked free shipping!\u003c\/strong\u003e\u003c\/p\u003e","divider\_placement":"top","icon":"https:\/\/static.rechargecdn.com\/merchant-image-library\/YzNiZTMyN2ZiMw\/images\/MzdlYzU4ZWZmYw","in\_progress\_text":"\u003cp style=\"text-align: center\"\u003e\u003cstrong\u003eYou're {{amount}} away from free USA shipping.\u003c\/strong\u003e\u003c\/p\u003e","padding\_bottom":25,"padding\_top":25,"show\_divider\_line":false,"show\_icon":true},"type":"shipping\_progress\_bar"}],"show\_divider\_line":false}},"line\_items":{"body":{"alignment":"top","blocks":[{"settings":{"padding\_bottom":16,"padding\_top":16,"savings\_text":"Saving {{discount}}","show\_divider\_line":false,"show\_savings\_text":true,"show\_strikethrough\_price":true,"upsell":{"display\_type":"button","frequency\_select\_label":"Deliver every","onetime\_frequency\_label":"One-time","show\_onetime\_frequency":true,"text\_discount":"SUBSCRIBE TO SAVE {{discount}}","text\_discount\_quantity\_upsell":"Subscribe and buy {{quantity}}, save {{discount}}!","text\_no\_discount":"Upgrade to a subscription","upsell\_in\_progress\_text":"Upgrading to subscription..."}},"type":"line\_items"},{"settings":{"add\_to\_cart\_button\_text":"ADD","card\_background\_color":"#F6F8FA","display\_options":"dropdown","display\_products\_on\_cards":false,"padding\_bottom":48,"padding\_top":6,"prompt\_add\_to\_cart\_button\_text":"ADD TO CART","prompt\_frequency\_selection\_label":"Deliver every","prompt\_one\_time\_option\_text":"One-time purchase","prompt\_variant\_selection\_label":"Options","section\_background\_color":"rgba(249, 248, 246, 1)","show\_title":true,"title\_text":"\u003ch4\u003eWANT MORE?\u003c\/h4\u003e"},"type":"cross\_sell"}],"padding\_bottom":0,"padding\_top":0},"footer":{"background\_color":"rgba(249, 248, 246, 1)","blocks":[{"settings":{"padding\_bottom":4,"padding\_top":0,"show\_strikethrough\_price":true,"subtotal\_text\_plural":"\u003cstrong\u003eSubtotal ({{items\_count}} items):\u003c\/strong\u003e","subtotal\_text\_singular":"\u003cstrong\u003eSubtotal ({{items\_count}} item):\u003c\/strong\u003e"},"type":"subtotal"},{"settings":{"checkout\_button\_text":"CHECKOUT","padding\_bottom":0,"padding\_top":31},"type":"checkout\_button"}],"padding\_bottom":48,"padding\_top":20,"section\_divider":"none"},"header":{"blocks":[{"settings":{"padding\_bottom":16,"padding\_top":32,"show\_divider\_line":false,"title":"\u003ch3\u003eCART ({{items\_count}})\u003c\/h3\u003e"},"type":"cart\_title"},{"settings":{"background\_color":"rgba(249, 248, 246, 1)","bar\_background\_color":"rgba(243, 239, 226, 1)","bar\_foreground\_color":"rgba(43, 46, 48, 1)","completed\_text":"\u003cp style=\"text-align: center\"\u003e🎉 \u003cstrong\u003eCongrats\u003c\/strong\u003e—\u003cstrong\u003eyou've unlocked free USA shipping!\u003c\/strong\u003e\u003c\/p\u003e","divider\_placement":"top","icon":"https:\/\/static.rechargecdn.com\/merchant-image-library\/YzNiZTMyN2ZiMw\/images\/MzdlYzU4ZWZmYw","in\_progress\_text":"\u003cp style=\"text-align: center\"\u003e\u003cstrong\u003eYou're {{amount}} away from free USA shipping.\u003c\/strong\u003e\u003c\/p\u003e","padding\_bottom":25,"padding\_top":25,"show\_divider\_line":false,"show\_icon":true},"type":"shipping\_progress\_bar"}],"show\_divider\_line":false}}},"theme":{"accent\_color":"rgba(89, 222, 59, 1)","background\_color":"rgba(249, 248, 246, 1)","border\_radius":"square","error\_color":"#EC3D10","foreground\_color":"rgba(16, 16, 16, 1)","link\_color":"#467c99","muted\_color":"rgba(43, 46, 48, 1)","padding\_left":48,"padding\_right":48,"primary\_color":"rgba(229, 255, 82, 1)","primary\_foreground\_color":"rgba(16, 16, 16, 1)","secondary\_color":"rgba(16, 16, 16, 1)","secondary\_foreground\_color":"rgba(249, 248, 246, 1)"}},"config":{"cross\_sell":{"config\_list":[{"cross\_sell":{"number\_of\_products":4,"products":[{"id":"14958730445170","variant\_ids":["61544778760562"],"frequency\_selection":"customer","handle":"tree-ranger-aluminum-free-deodorant","purchase\_option":"onetime\_only"},{"id":"14958729888114","variant\_ids":["61544777941362"],"frequency\_selection":"customer","handle":"old-money-aluminum-free-deodorant","purchase\_option":"onetime\_only"},{"id":"14958726414706","variant\_ids":["61544772567410"],"frequency\_selection":"customer","handle":"bold-fortune-aluminum-free-deodorant","purchase\_option":"onetime\_only"},{"id":"14958730936690","variant\_ids":["61544784200050"],"frequency\_selection":"customer","handle":"temple-smoke-aluminum-free-deodorant","purchase\_option":"onetime\_only"}],"type":"specific\_products"},"trigger":{"type":"any"}}],"enabled":true},"shipping\_progress\_bar":{"enabled":true,"required\_amount":"75","required\_amount\_type":"discounted","subscriptions\_unlock\_free\_shipping":false},"upsell\_cart\_items":true},"flow\_id":0}},
bundles\_selling\_plan\_sync\_enabled:false,
};
})();

![](https://aa.trkn.us/1/e/c.gif?cid=c013&evid=4d746137-8d1d-465b-981b-f81f6382dec0&r=1781460439374&dmn=www.beardbrand.com&pn=/cart&qs=&suu=1&v1=&v2=SkE8m&v3=64X3AR0vG5jZhN3H_mqe3j8kn&v4=C7xwofhAv5eFetRb_mqe3j8kn&v5=2674)