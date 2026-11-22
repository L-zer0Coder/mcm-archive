(function(){
var R=window.UPC_UI_ROOT||'';
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
var st=document.createElement('style');st.textContent=".uig-btnL,.uig-btnR{position:fixed;top:50%;transform:translateY(-50%);z-index:85;\nwriting-mode:vertical-rl;letter-spacing:.2em;font-size:12.5px;padding:14px 6px;\nborder:1px solid #D9D0BD;background:#FDFCF8;color:#6E6557;cursor:pointer;font-family:inherit}\n.uig-btnL{left:0;border-left:none;border-radius:0 4px 4px 0}\n.uig-btnR{right:0;border-right:none;border-radius:4px 0 0 4px}\n.uig-btnL:hover,.uig-btnR:hover{color:#2B5C8A;border-color:#2B5C8A}\n.uig-panel{position:fixed;top:0;bottom:0;width:min(380px,88vw);z-index:95;background:#F7F4ED;\nbox-shadow:0 0 40px rgba(43,92,138,.25);transition:transform .25s;overflow-y:auto;visibility:hidden}\n.uig-panel.on{visibility:visible}\n#uig-nav{left:0;transform:translateX(-105%)}#uig-nav.on{transform:none}\n#uig-doc{right:0;transform:translateX(105%)}#uig-doc.on{transform:none}\n.uig-h{font-family:Georgia,serif;font-size:16px;font-weight:700;padding:14px 16px;border-bottom:1px solid #E7E0D1}\n.uig-x{position:absolute;top:10px;right:10px;width:30px;height:30px;border:1px solid #D9D0BD;background:#FDFCF8;border-radius:3px;font-size:16px;color:#6E6557;cursor:pointer}\n.uig-tree,.uig-doc{padding:8px 12px 20px;font-size:13px;line-height:2}\n.uig-tn{line-height:2}\n.uig-tn a{color:#2B5C8A}.uig-tn a:hover{text-decoration:underline}\n.uig-c{width:18px;height:18px;border:none;background:none;color:#6E6557;cursor:pointer;font-family:monospace;padding:0;margin-right:3px}\n.uig-kids{border-left:1px dashed #D9D0BD;margin-left:8px}\n@media print{.uig-btnL,.uig-btnR,.uig-panel{display:none!important}}";document.head.appendChild(st);
var open=false,current='';
function toggle(side){
  if(current===side){close();return;}
  var old=document.getElementById('uig-'+current);if(old)old.remove();
  current=side;open=true;
  ensureData(function(){
    var w=document.createElement('div');w.id='uig-'+side;w.className='uig-panel on';
    w.innerHTML='<button class="uig-x" type="button">×</button>'+(side==='nav'?navHtml():docHtml());
    w.querySelector('.uig-x').addEventListener('click',close);
    document.body.appendChild(w);
    if(side==='nav')bindTree(w);
  });
}
function close(){var p=document.getElementById('uig-'+current);if(p)p.remove();current='';open=false;}
function ensureData(cb){if(window.UPC_UI_DATA)return cb();
  var s=document.createElement('script');s.src=R+'global-ui-data.js';
  s.onload=cb;s.onerror=function(){alert('导航数据加载失败');};document.head.appendChild(s);}
function navHtml(){return '<div class="uig-h">☰ 全站目录</div><div style="padding:6px 10px"><input id="uig-q" placeholder="过滤…" style="width:calc(100% - 20px);margin:0 10px;height:28px;border:1px solid #D9D0BD;border-radius:3px;font-size:12.5px"></div><div id="uig-tree"></div>';}
function docHtml(){return '<div class="uig-h">📖 全站说明</div><div style="padding:8px 14px">'+window.UPC_UI_DATA.manual+'</div>';}
function bindTree(w){
  var tree=w.querySelector('#uig-tree');
  tree.innerHTML=nodeHtml(window.UPC_UI_DATA.tree,0);
  var rk=tree.querySelector(':scope > div.uig-kids');if(rk)rk.style.display='block';
  tree.addEventListener('click',function(ev){var b=ev.target.closest('.uig-c');if(!b)return;
    var k=b.parentElement.nextElementSibling;var o=k.style.display!=='none';
    k.style.display=o?'none':'block';b.textContent=o?'▸':'▾';});
  var q=w.querySelector('#uig-q');
  q.addEventListener('input',function(){var kw=this.value.trim().toLowerCase();
    var tns=tree.querySelectorAll('.uig-tn');
    tns.forEach(function(d){d.style.display=(!kw||d.textContent.toLowerCase().indexOf(kw)>=0)?'':'none';});
    tree.querySelectorAll('.uig-kids').forEach(function(k){k.style.display=kw?'block':'none';});
    if(!kw){var rk=tree.querySelector(':scope > div.uig-kids');if(rk)rk.style.display='block';}});
}
function nodeHtml(n,depth){
  var row='<div class="uig-tn" style="padding-left:'+(depth*13+4)+'px">'+
    (n.ch?'<button class="uig-c" type="button">▸</button>':'<span style="color:#D9D0BD;margin:0 5px 0 9px">·</span>')+
    (n.u?'<a href="'+R+n.u+'">'+esc(n.n)+'</a>':'<span>'+esc(n.n)+'</span>')+
    (n.d?' <span style="color:#8a8172;font-size:10.5px">'+esc(n.d)+'</span>':'')+'</div>';
  if(n.ch)row+='<div class="uig-kids" style="display:none">'+
    n.ch.map(function(c){return nodeHtml(c,depth+1);}).join('')+'</div>';
  return row;
}
function btn(side,label){var b=document.createElement('button');b.id='uig-'+side+'-btn';
  b.type='button';b.textContent=label;b.className=(side==='nav'?'uig-btnL':'uig-btnR');
  b.addEventListener('click',function(){toggle(side);});
  document.body.appendChild(b);}
function init(){btn('nav','☰ 目录');btn('doc','📖 说明');}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
