(()=>{
 const languages=['fr','en','ja'],languageSelect=document.querySelector('[data-language-select]');
 const switchLanguage=lang=>{
  try{localStorage.setItem('europe-language',lang)}catch{}
  const file=location.pathname.split('/').pop()||'index.html';
  const target=new URL('../'+lang+'/'+file,location.href);target.search=location.search;target.hash=location.hash;
  location.replace(target.href);
 };
 let preferred;
 try{preferred=localStorage.getItem('europe-language')}catch{}
 if(!languages.includes(preferred)){
  preferred=(navigator.languages||[navigator.language||'fr']).map(l=>l.toLowerCase().split('-')[0]).find(l=>languages.includes(l))||'fr';
  try{localStorage.setItem('europe-language',preferred)}catch{}
  if(languageSelect&&preferred!==document.documentElement.lang){switchLanguage(preferred);return}
 }
 languageSelect?.addEventListener('change',()=>switchLanguage(languageSelect.value));
 const root=document.documentElement,theme=document.querySelector('[data-theme-toggle]');
 try{const saved=localStorage.getItem('europe-theme');if(saved)root.dataset.theme=saved;else if(matchMedia('(prefers-color-scheme:dark)').matches)root.dataset.theme='dark'}catch{}
 theme?.addEventListener('click',()=>{const next=root.dataset.theme==='dark'?'light':'dark';root.dataset.theme=next;theme.setAttribute('aria-pressed',String(next==='dark'));try{localStorage.setItem('europe-theme',next)}catch{}});
 if(theme)theme.setAttribute('aria-pressed',String(root.dataset.theme==='dark'));
 const filters=[...document.querySelectorAll('[data-filter]')],items=[...document.querySelectorAll('.glyph')],count=document.querySelector('[data-result-count]');
 for(const button of filters)button.addEventListener('click',()=>{
  const filter=button.dataset.filter;for(const b of filters)b.setAttribute('aria-pressed',String(b===button));
  let shown=0;for(const item of items){item.hidden=filter!=='all'&&item.dataset.status!==filter;if(!item.hidden)shown++}
  for(const line of document.querySelectorAll('[data-line]'))line.hidden=![...line.querySelectorAll('.glyph')].some(g=>!g.hidden);
  if(count)count.textContent=count.dataset.template.replace('{n}',shown);
 });
})();
// Menu « Dossiers » : ouverture au clic, fermeture au clic extérieur ou avec Échap.
document.querySelectorAll('.nav-menu').forEach(m=>{const b=m.querySelector('.nav-toggle');b.addEventListener('click',()=>{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',String(o))})});document.addEventListener('click',e=>{document.querySelectorAll('.nav-menu.open').forEach(m=>{if(!m.contains(e.target)){m.classList.remove('open');m.querySelector('.nav-toggle').setAttribute('aria-expanded','false')}})});document.addEventListener('keydown',e=>{if(e.key==='Escape')document.querySelectorAll('.nav-menu.open').forEach(m=>{m.classList.remove('open');m.querySelector('.nav-toggle').setAttribute('aria-expanded','false')})});
