# -*- coding: utf-8 -*-
"""build_tools.py — 生成 06_赛时工具/ 交互工具页（每页前三行为定位声明）
工具：selector 选型助手 / budget 页数预算器 / warroom 作战室 / flashcards 闪卡库
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import EVENT_START_MS, EVENT_END_MS, PHASES
from page_shell import page
from flashcards_data import CARDS
from prompts_data import PROMPTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
EV = (EVENT_START_MS, EVENT_END_MS)

BASE_CSS = """
.q{border:1px solid #D9D0BD;background:#FDFCF8;border-radius:4px;padding:14px 18px;margin-bottom:10px}
.q h3{margin:0 0 6px;font-size:14px}
.opt{display:inline-block;margin:3px 6px 3px 0;padding:5px 12px;border:1px solid #D9D0BD;border-radius:3px;
     font-size:12.5px;cursor:pointer;background:#FDFCF8}
.opt.on{background:#2B5C8A;border-color:#2B5C8A;color:#FDFCF8}
.opt:hover{border-color:#2B5C8A}
#verdict{border:1px solid #2B5C8A;background:#FDFCF8;border-radius:4px;padding:16px 20px;margin-top:14px}
#verdict .bar{height:8px;border-radius:4px;background:#E7E0D1;margin:4px 0 10px;position:relative}
#verdict .bar i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#2B5C8A}
.suggest{font-size:13px;color:#6E6557;margin-top:4px}
"""

QUIZ = [
    ('队里最能打的技能是？', [
        ('微分方程 / 物理机理', {"A": 3, "B": 1}),
        ('优化 / 算法 / 编程', {"B": 3, "D": 1}),
        ('统计 / 数据处理', {"C": 3, "E": 1}),
        ('运筹 / 网络分析', {"D": 3, "B": 2}),
        ('指标体系 / 综合评价', {"E": 3, "F": 2}),
        ('政策分析 / 写作论证', {"F": 3, "E": 1}),
    ]),
    ('你们更擅长哪种工作方式？', [
        ('推公式、写方程、做机理分析', {"A": 2, "B": 1}),
        ('跑数据、画图、找规律', {"C": 2, "E": 1}),
        ('搭模型、调约束、解出最优解', {"B": 2, "D": 1}),
    ]),
    ('对「自带数据集」的题（C 类）感觉如何？', [
        ('很适应——处理脏数据是乐趣', {"C": 3}),
        ('一般——能做但不偏爱', {"C": 1}),
        ('不适应——想要机理或结构清晰的题', {"A": 1, "B": 1, "D": 1}),
    ]),
    ('写作与论证能力自评？', [
        ('强——能把复杂模型讲得清晰可信', {"F": 2, "E": 1}),
        ('中——重模型轻写作', {"B": 1, "A": 1, "D": 1}),
    ]),
]

TYPE_PAGE = {"A": "A_%E8%BF%9E%E7%BB%AD", "B": "B_%E7%A6%BB%E6%95%A3",
             "C": "C_%E6%95%B0%E6%8D%AE%E6%B4%9E%E5%AF%9F", "D": "D_%E8%BF%90%E7%AD%B9%E7%BD%91%E7%BB%9C",
             "E": "E_%E5%8F%AF%E6%8C%81%E7%BB%AD", "F": "F_%E6%94%BF%E7%AD%96"}
TYPE_ORG = {"A": "A_连续", "B": "B_离散", "C": "C_数据洞察",
            "D": "D_运筹网络", "E": "E_可持续", "F": "F_政策"}
TYPE_MODULE = {"A": "02_微分方程与动力学", "B": "01_优化方法族",
               "C": "03_统计与机器学习", "D": "04_图论与网络",
               "E": "05_评价与决策", "F": "07_写作与SummarySheet"}


def _finish(name, html, label):
    out = P("06_赛时工具", name)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("  tools: {} {} KB".format(name, os.path.getsize(out) // 1024))


def build_selector():
    body = [
        '<p class="suggest">用途：赛前 5 分钟自测，输出六题型的匹配度排序与主攻模块建议。'
        '依据：2024–2026 官方题面画像 + 方法族映射（题型打法各页）。本页不联网，数据只存本浏览器。</p>',
    ]
    for i, (q, opts) in enumerate(QUIZ):
        body.append('<div class="q"><h3>{}. {}</h3>'.format(i + 1, q))
        for j, (label, _) in enumerate(opts):
            body.append('<span class="opt" data-q="{}" data-o="{}">{}</span>'.format(i, j, label))
        body.append('</div>')
    body.append('<button class="btn solid" id="go" style="margin-top:6px">生成匹配度报告</button>')
    body.append('<div id="verdict" style="display:none"></div>')
    script = """
var QUIZ=__QUIZ__, TP=__TP__, TO=__TO__, TM=__TM__;
var LABEL={A:'MCM·连续',B:'MCM·离散',C:'MCM·数据洞察',D:'ICM·运筹网络',E:'ICM·可持续',F:'ICM·政策'};
var pick={};
function bind(){
  document.querySelectorAll('.opt').forEach(function(el){
    el.addEventListener('click', function(){
      var q=el.dataset.q, o=+el.dataset.o;
      document.querySelectorAll('.opt[data-q="'+q+'"]').forEach(function(x){x.classList.remove('on');});
      el.classList.add('on'); pick[q]=o;
    });
  });
  document.getElementById('go').addEventListener('click', report);
}
function report(){
  for (var i=0;i<QUIZ.length;i++){ if(pick[i]===undefined){ alert('还有未作答的题'); return; } }
  var sc={};
  Object.keys(pick).forEach(function(qi){
    var o=QUIZ[qi][1][pick[qi]][1];
    Object.keys(o).forEach(function(t){ sc[t]=(sc[t]||0)+o[t]; });
  });
  var order=Object.keys(sc).sort(function(a,b){return sc[b]-sc[a];});
  var max=sc[order[0]]||1;
  var v=document.getElementById('verdict');
  v.style.display='block';
  var html='<b style="font-family:Georgia,serif">匹配度排序</b>';
  order.forEach(function(t){
    var pct=Math.round(sc[t]/max*100);
    html+='<div style="margin-top:10px"><b>'+t+' '+LABEL[t]+'</b>—— 匹配 '+pct+'%'+
      '<div class="bar"><i style="width:'+pct+'%"></i></div>'+
      '<div class="suggest">打法：<a href="../docs/03_'+encodeURIComponent('题型打法')+'/'+TP[t]+'.html">'+TO[t]+'</a> · '+
      '主攻模块：<a href="../docs/02_'+encodeURIComponent('知识模块')+'/'+encodeURIComponent(TM[t])+'.html">'+TM[t]+'</a></div></div>';
  });
  html+='<p class="suggest">提醒：匹配度只是先验。开赛当天务必六题全读一遍，用题面任务清单对照本报告再定题。</p>';
  v.innerHTML=html;
  try{ localStorage.setItem('mcm-quiz', JSON.stringify(pick)); }catch(e){}
}
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', bind); else bind();
"""
    script = script.replace("__QUIZ__", json.dumps(QUIZ, ensure_ascii=False))
    script = script.replace("__TP__", json.dumps(TYPE_PAGE))
    script = script.replace("__TO__", json.dumps(TYPE_ORG, ensure_ascii=False))
    script = script.replace("__TM__", json.dumps(TYPE_MODULE, ensure_ascii=False))
    desc = "MCM/ICM 备赛工具：五分钟自测队内技能与六题型的匹配度。数据只存本浏览器，不联网。"
    html = page("选型助手", "赛时工具", desc, "\n".join(body), script, uiroot="../", ev=EV)
    html = html.replace("</style>", BASE_CSS + "\n</style>", 1)
    _finish("selector.html", html, "选型助手")


BUDGET_SECTIONS = [
    ("Summary Sheet", 1.0, "评委初筛唯一依据，最后写但每天写一版"),
    ("1 Introduction（问题重述与分析）", 1.5, "把题面翻译成『我们要决定什么』"),
    ("2 Assumptions & Justifications", 1.0, "每条假设可追溯、有理由"),
    ("3 Notations", 0.5, "符号表"),
    ("4 Model I（基础模型）", 4.0, "先跑通的最小可行模型"),
    ("5 Model II（改进 / 优化模型）", 4.5, "逐条加约束的扩展"),
    ("6 Sensitivity & Validation", 3.0, "影子价格 / gap / 收敛 / 参数扫描"),
    ("7 Results & Discussion", 4.0, "每图一个论点，结论带数字"),
    ("8 Strengths & Weaknesses", 1.5, "诚实，弱点给改进方向"),
    ("9 Conclusion & Policy", 1.5, "条件化结论 + 谁该做什么"),
    ("References", 1.0, "外部数据/图/结论/AI 工具都要进列表"),
    ("Appendix（代码 / 长表）", 1.5, "清洗流水线账本放这里"),
]

BUDGET_CSS = """
table.budget td{padding:6px 8px}
table.budget input{width:100%;border:1px solid #E7E0D1;border-radius:3px;padding:4px 6px;font-size:12.5px;
                   background:#FDFCF8;color:#2A251E;font-family:inherit}
table.budget input.num{width:64px;text-align:right}
.tot{font-family:Georgia,serif;font-size:15px}
.bar{height:10px;border-radius:5px;background:#E7E0D1;position:relative;margin:8px 0}
.bar i{position:absolute;left:0;top:0;bottom:0;border-radius:5px;background:#2B5C8A}
.bar.over i{background:#B04A3A}
.ok{color:#2B5C8A}.over{color:#B04A3A}
.suggest{font-size:13px;color:#6E6557;margin-top:4px}
"""


def build_budget():
    rows = "".join(
        '<tr><td style="font-size:12.5px">{nm}</td>'
        '<td><input class="num tgt" data-i="{i}" type="number" step="0.5" min="0" value="{tg}"></td>'
        '<td><input class="num act" data-i="{i}" type="number" step="0.25" min="0" value="0"></td>'
        '<td><input class="nt" data-i="{i}" value="{nt}"></td></tr>'.format(
            i=i, nm=nm, tg=tg, nt=nt)
        for i, (nm, tg, nt) in enumerate(BUDGET_SECTIONS))
    body = [
        '<p class="suggest">用途：赛时对 25 页硬上限做逐节对账——目标页数可改，实写页数随时填，超额立刻变红。'
        '口径：25 页含 Summary、正文、附录与参考文献全算（官方口径见 01_COMAP官方/竞赛要点）。数据存本浏览器。</p>',
        '<table class="budget"><thead><tr><th>章节</th><th>目标页</th><th>实写页</th><th>备注</th></tr></thead>'
        '<tbody id="rows">' + rows + '</tbody></table>',
        '<div style="margin-top:10px"><span class="tot" id="tot"></span>'
        '<div class="bar" id="bar"><i></i></div>'
        '<button class="btn" id="add">加一节</button> '
        '<button class="btn" id="export">复制为 Markdown</button> '
        '<button class="btn" id="reset">重置</button></div>',
        '<div id="mdbox" class="suggest" style="display:none"></div>',
    ]
    script = """
var KEY='mcm-budget';
function rows(){ return Array.from(document.querySelectorAll('#rows tr')); }
function read(){ return rows().map(function(tr){
  return { nm: tr.children[0].textContent.trim(),
           tg: +tr.querySelector('.tgt').value || 0,
           act: +tr.querySelector('.act').value || 0,
           nt: tr.querySelector('.nt').value }; }); }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(read())); }catch(e){} }
function load(){
  try{ var d = JSON.parse(localStorage.getItem(KEY)); if(!d) return;
    var tb = document.getElementById('rows');
    tb.innerHTML = d.map(function(r, i){
      return '<tr><td style="font-size:12.5px">'+r.nm+'</td>'+
        '<td><input class="num tgt" data-i="'+i+'" type="number" step="0.5" min="0" value="'+r.tg+'"></td>'+
        '<td><input class="num act" data-i="'+i+'" type="number" step="0.25" min="0" value="'+r.act+'"></td>'+
        '<td><input class="nt" data-i="'+i+'" value="'+String(r.nt).replace(/"/g,'&quot;')+'"></td></tr>';
    }).join('');
  }catch(e){}
}
function render(){
  var d = read();
  var tgt = d.reduce(function(a,r){return a+r.tg;},0);
  var act = d.reduce(function(a,r){return a+r.act;},0);
  var left = 25 - act;
  var el = document.getElementById('tot');
  el.innerHTML = '目标合计 <b>'+tgt.toFixed(1)+'</b> 页 · 已写 <b>'+act.toFixed(2)+'</b> 页 · 剩余 <b>'+
    left.toFixed(2)+'</b> 页'+(left<0?' <span class="over">—— 超限 '+(-left).toFixed(2)+' 页！</span>':' <span class="ok">（25 页硬上限内）</span>');
  var bar = document.getElementById('bar');
  bar.className = 'bar' + (act>25 ? ' over' : '');
  bar.querySelector('i').style.width = Math.min(100, act/25*100)+'%';
  save();
}
function bind(){
  document.getElementById('rows').addEventListener('input', render);
  document.getElementById('rows').addEventListener('change', render);
  document.getElementById('add').addEventListener('click', function(){
    var tr = document.createElement('tr');
    var i = rows().length;
    tr.innerHTML = '<td style="font-size:12.5px">新章节</td>'+
      '<td><input class="num tgt" data-i="'+i+'" type="number" step="0.5" min="0" value="0.5"></td>'+
      '<td><input class="num act" data-i="'+i+'" type="number" step="0.25" min="0" value="0"></td>'+
      '<td><input class="nt" data-i="'+i+'" value=""></td>';
    document.getElementById('rows').appendChild(tr); render();
  });
  document.getElementById('reset').addEventListener('click', function(){
    if (confirm('清空本浏览器里的预算记录？')) { localStorage.removeItem(KEY); location.reload(); }
  });
  document.getElementById('export').addEventListener('click', function(){
    var md = '| 章节 | 目标页 | 实写页 | 备注 |\\n|---|---|---|---|\\n' +
      read().map(function(r){ return '| '+r.nm+' | '+r.tg+' | '+r.act+' | '+r.nt+' |'; }).join('\\n');
    var tot = read().reduce(function(a,r){return a+r.act;},0);
    md += '\\n\\n合计实写 '+tot.toFixed(2)+' / 25 页';
    var box = document.getElementById('mdbox');
    box.style.display='block'; box.textContent = md;
    try { navigator.clipboard.writeText(md).then(function(){}, function(){}); } catch(e){}
  });
  load(); render();
}
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', bind); else bind();
"""
    desc = "MCM/ICM 备赛工具：25 页硬上限的逐节页数对账。目标可改、实写随时填、超额变红。数据只存本浏览器。"
    html = page("页数预算器", "赛时工具", desc, "\n".join(body), script, uiroot="../", ev=EV)
    html = html.replace("</style>", BUDGET_CSS + "\n</style>", 1)
    _finish("budget.html", html, "页数预算器")


WAR_ITEMS = [
    ["六题全读，每题写三行表（变量/目标/约束）", "对照选型助手报告定主攻题 + 备份题", "锁定题目后建立 LaTeX 骨架与仓库", "约定『Summary 每天写一版』的轮值"],
    ["文献检索一轮（近三年同场景方法）", "数据获取 + 清洗留账（C 题）", "假设表初稿（编号可追溯）"],
    ["核心机理方程 / 三行翻译表落纸", "最小可行模型跑通一条完整路径", "扩展方向排序（先易后难）"],
    ["主模型全量跑通（最优值/gap/时间三件套）", "收敛性 / 样本外检验落地", "扩展模型逐条加、逐条重跑", "每 2h 推送一次阶段性结果给全队"],
    ["关键参数 ±20% 扫描出图", "影子价格 / gap 界写进结论", "守恒量 / 对账检查"],
    ["Summary 每天迭代一版", "图表逐图过『一图一论点』", "假设表终版与正文一致"],
    ["页数预算器逐节对账 25 页", "数字三处一致对账（Summary/正文/图表）", "图题全部结论化"],
    ["AI 披露核对（完整输出三要素）", "提前 2h 提交", "Summary 最后通读 15 分钟视角"],
]

WAR_CSS = """
.ph{border:1px solid #D9D0BD;background:#FDFCF8;border-radius:4px;padding:12px 18px;margin-bottom:10px}
.ph.now{border-color:#2B5C8A;background:#F2F6FA;box-shadow:0 0 0 1px #2B5C8A inset}
.ph h3{margin:0;font-size:14px}
.ph .win{font-family:ui-monospace,Consolas,monospace;font-size:11px;color:#6E6557;border:1px solid #D9D0BD;
         border-radius:3px;padding:1px 6px;margin-left:6px}
.ph .live{color:#2B5C8A;font-size:11px}
.chk{list-style:none;margin:8px 0 0;padding:0;font-size:13px;line-height:2}
.bar{height:10px;border-radius:5px;background:#E7E0D1;position:relative;margin:8px 0}
.bar i{position:absolute;left:0;top:0;bottom:0;border-radius:5px;background:#2B5C8A}
.suggest{font-size:13px;color:#6E6557;margin-top:4px}
"""


def build_warroom():
    phases_html = []
    for i, ph in enumerate(PHASES):
        lo, hi, tag, task, note = ph
        ch = "".join('<li><label><input type="checkbox" data-p="{}" data-i="{}"> {}</label></li>'.format(i, j, t)
                     for j, t in enumerate(WAR_ITEMS[i]))
        phases_html.append(
            '<div class="ph" id="ph{i}" data-lo="{lo}" data-hi="{hi}">'
            '<h3>{tag} {task} <span class="win">{lo}–{hi}h</span></h3>'
            '<p class="suggest">{note}</p><ul class="chk">{ch}</ul></div>'.format(
                i=i, lo=lo, hi=hi, tag=tag, task=task, note=note, ch=ch))
    body = [
        '<p class="suggest">用途：赛时 96 小时的阶段轴 + 每阶段 checklist，勾选状态存本浏览器。'
        '时段按开赛时刻自动推算，赛中当前阶段高亮。口径见 01_COMAP官方/竞赛要点。</p>',
        '<div id="prog" class="suggest"></div><div class="bar" id="pbar"><i></i></div>',
        "\n".join(phases_html),
    ]
    script = """
var EVS=__EVS__;
function load(){ try{ return JSON.parse(localStorage.getItem('mcm-warroom')) || {}; }catch(e){ return {}; } }
function save(d){ try{ localStorage.setItem('mcm-warroom', JSON.stringify(d)); }catch(e){} }
function progress(){
  var all = document.querySelectorAll('input[type=checkbox]');
  var done = Array.prototype.filter.call(all, function(c){ return c.checked; }).length;
  var pct = all.length ? Math.round(done/all.length*100) : 0;
  document.getElementById('prog').innerHTML = '总进度 <b>'+done+'/'+all.length+'</b>（'+pct+'%）';
  document.querySelector('#pbar i').style.width = pct+'%';
}
function markNow(){
  var t = Date.now(), inContest = t >= EVS;
  document.querySelectorAll('.ph').forEach(function(el){
    var lo = +el.dataset.lo, hi = +el.dataset.hi;
    var on = inContest && t >= EVS + lo*36e5 && t < EVS + hi*36e5;
    el.classList.toggle('now', on);
    var head = el.querySelector('h3');
    var tag = head.querySelector('.live');
    if (on && !tag) {
      tag = document.createElement('span'); tag.className='live'; tag.textContent=' ← 当前时段';
      head.appendChild(tag);
    } else if (!on && tag) { tag.remove(); }
  });
}
function bind(){
  var st = load();
  document.querySelectorAll('input[type=checkbox]').forEach(function(c){
    var k = c.dataset.p + '-' + c.dataset.i;
    if (st[k]) c.checked = true;
    c.addEventListener('change', function(){ st[k] = c.checked; save(st); progress(); });
  });
  progress(); markNow();
  setInterval(markNow, 60000);
}
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', bind); else bind();
"""
    script = script.replace("__EVS__", str(EVENT_START_MS))
    desc = "MCM/ICM 备赛工具：96 小时阶段轴 + 每阶段 checklist，当前时段自动高亮。数据只存本浏览器。"
    html = page("96h 作战室", "赛时工具", desc, "\n".join(body), script, uiroot="../", ev=EV)
    html = html.replace("</style>", WAR_CSS + "\n</style>", 1)
    _finish("warroom.html", html, "96h 作战室")


FL_CARDS_CSS = """
.cats{margin:10px 0}
.cat{display:inline-block;margin:3px 6px 3px 0;padding:4px 10px;border:1px solid #D9D0BD;border-radius:3px;
     font-size:12px;cursor:pointer;background:#FDFCF8}
.cat.on{background:#2B5C8A;border-color:#2B5C8A;color:#FDFCF8}
#card{border:1px solid #D9D0BD;background:#FDFCF8;border-radius:4px;min-height:170px;padding:18px 22px;
      cursor:pointer;position:relative}
#card .cat-tag{position:absolute;top:10px;right:12px;font-size:11px;color:#786E60;border:1px solid #D9D0BD;
               border-radius:3px;padding:1px 8px}
#card .face{font-size:14.5px;line-height:1.9}
#card .back{color:#6E6557;margin-top:10px;border-top:1px dashed #D9D0BD;padding-top:10px;font-size:13.5px}
#card .hint{position:absolute;bottom:10px;left:22px;font-size:11px;color:#B9B0A0}
.nav{margin-top:12px}
.stat{font-size:12.5px;color:#6E6557;margin-top:8px}
.katex-display{margin:6px 0}
"""


def build_flashcards():
    cats = []
    for c, _, _, _ in CARDS:
        if c not in cats:
            cats.append(c)
    body = [
        '<p class="suggest">用途：方法族核心概念的自测闪卡（{} 张，全部出自 02_知识模块 七篇正文：正面自问、点卡翻答案，答案带出处跳转）。'
        '熟悉/不熟的进度存本浏览器。先读正文再刷卡——卡片是自测工具，不是替代品。</p>'.format(len(CARDS)),
        '<div class="cats"><span class="cat on" data-c="全部">全部</span>' +
        "".join('<span class="cat" data-c="{}">{}</span>'.format(c, c) for c in cats) +
        '</div>',
        '<div id="card"><span class="cat-tag" id="ftag"></span><div class="face" id="fface"></div></div>',
        '<div class="nav"><button class="btn solid" id="know">熟悉</button> '
        '<button class="btn" id="unknow">不熟</button> '
        '<button class="btn" id="skip">跳过</button> '
        '<button class="btn" id="shuffle">打乱</button> '
        '<button class="btn" id="reset">重置进度</button>'
        '<span class="hint">快捷键：空格翻卡 · ←/→ 切卡</span></div>',
        '<div class="stat" id="stat"></div>',
    ]
    script = """
var CARDS=__CARDS__;
var KEY='mcm-flash', cur=0, shown=false, cat='全部', deck=[];
var known={}, seen=0;
function load(){ try{
  var d=JSON.parse(localStorage.getItem(KEY));
  if(d){ known=d.known||{}; seen=d.seen||0; }
}catch(e){} }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify({known:known, seen:seen})); }catch(e){} }
function rebuild(){ deck = CARDS.map(function(_,i){return i;})
  .filter(function(i){ return cat==='全部' || CARDS[i][0]===cat; });
  for (var i=deck.length-1;i>0;i--){ var j=Math.floor(Math.random()*(i+1)); var t=deck[i]; deck[i]=deck[j]; deck[j]=t; } }
function katexify(el){ if(window.renderMathInElement){ renderMathInElement(el,
  {delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}], throwOnError:false}); } }
function statline(){
  document.getElementById('stat').textContent =
    '卡片 ' + (cur+1) + '/' + deck.length + '（分类：' + cat + '）· 已熟悉 ' +
    Object.keys(known).filter(function(k){return known[k];}).length + ' · 已翻看 ' + seen;
}
function show(){
  if(!deck.length){ document.getElementById('fface').textContent='该分类暂无卡片'; return; }
  cur = cur % deck.length;
  var c = CARDS[deck[cur]];
  document.getElementById('ftag').textContent = c[0];
  var face = document.getElementById('fface');
  face.innerHTML = '<b>' + c[1] + '</b>';
  var old = document.querySelector('#card .back'); if(old) old.remove();
  shown = false;
  statline();
  katexify(face);
}
function flip(){
  if(shown){ return; }
  var c = CARDS[deck[cur]];
  var back = document.createElement('div');
  back.className = 'back';
  back.innerHTML = c[2] + '<br><a href="../docs/02_'+encodeURIComponent('知识模块')+'/'+encodeURIComponent(c[3])+'.html" ' +
    'style="font-size:12px">→ 出处：' + c[3] + '</a>';
  document.getElementById('card').appendChild(back);
  katexify(back);
  shown = true; seen++;
  statline(); save();
}
function next(step){ if(!deck.length) return; cur = (cur + step + deck.length) % deck.length; shown=false;
  var old = document.querySelector('#card .back'); if(old) old.remove(); show(); }
function bind(){
  load(); rebuild(); show();
  document.getElementById('card').addEventListener('click', function(e){
    if (e.target.tagName === 'A' || e.target.tagName === 'INPUT') return; flip(); });
  document.getElementById('know').addEventListener('click', function(){ known[deck[cur]] = true; save(); next(1); });
  document.getElementById('unknow').addEventListener('click', function(){ known[deck[cur]] = false; save(); next(1); });
  document.getElementById('skip').addEventListener('click', function(){ next(1); });
  document.getElementById('shuffle').addEventListener('click', function(){ cur=0; shown=false; rebuild(); show(); });
  document.getElementById('reset').addEventListener('click', function(){
    if (confirm('清空熟悉/浏览进度？')) { known={}; seen=0; save(); show(); } });
  document.querySelectorAll('.cat').forEach(function(el){
    el.addEventListener('click', function(){
      document.querySelectorAll('.cat').forEach(function(x){x.classList.remove('on');});
      el.classList.add('on'); cat = el.dataset.c; cur=0; shown=false; rebuild(); show();
    });
  });
  document.addEventListener('keydown', function(e){
    if (e.code==='Space'){ e.preventDefault(); flip(); }
    if (e.code==='ArrowRight'){ next(1); }
    if (e.code==='ArrowLeft'){ next(-1); }
  });
}
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', bind); else bind();
"""
    script = script.replace("__CARDS__", json.dumps(CARDS, ensure_ascii=False))
    desc = "MCM/ICM 备赛工具：方法族核心概念闪卡，正反翻看与熟悉度自测。数据只存本浏览器。"
    html = page("闪卡库", "赛时工具", desc, "\n".join(body), script, uiroot="../", ev=EV)
    html = html.replace("</style>", FL_CARDS_CSS + "\n</style>", 1)
    _finish("flashcards.html", html, "闪卡库")


PROMPTS_CSS = """
.cats{margin:10px 0}
.cat{display:inline-block;margin:3px 6px 3px 0;padding:4px 10px;border:1px solid #D9D0BD;border-radius:3px;
     font-size:12px;cursor:pointer;background:#FDFCF8}
.cat.on{background:#2B5C8A;border-color:#2B5C8A;color:#FDFCF8}
.pr{border:1px solid #D9D0BD;background:#FDFCF8;border-radius:4px;padding:14px 18px;margin-bottom:12px}
.pr h3{margin:0 0 2px;font-size:14px}
.pr .when{font-size:12px;color:#786E60;margin:2px 0 8px}
.pr pre{background:#F9F6EF;border:1px solid #E7E0D1;border-radius:4px;padding:10px 14px;
        font-size:12.5px;line-height:1.8;white-space:pre-wrap;word-break:break-word;margin:8px 0 6px}
.pr .note{font-size:12.5px;color:#6E6557}
.pr .btn{height:26px;font-size:11.5px;padding:0 10px}
.disc{border:1px solid #B04A3A;background:#FBF3F1;border-radius:4px;padding:10px 16px;font-size:12.5px;
      color:#8A4A3E;margin-top:6px}
"""


def build_prompts():
    cats = []
    for c, _, _, _, _ in PROMPTS:
        if c not in cats:
            cats.append(c)
    body = [
        '<p class="suggest">用途：赛时 AI 协作的 12 条提示词，全部锚定 02_知识模块 的方法纪律；'
        '【】为需要队伍自己填的槽位，一键复制后粘进对话框。使用前必读页底披露纪律。</p>',
        '<div class="cats"><span class="cat on" data-c="全部">全部</span>' +
        "".join('<span class="cat" data-c="{}">{}</span>'.format(c, c) for c in cats) +
        '</div>',
        '<div id="list"></div>',
        '<div class="disc"><b>AI 使用披露纪律（COMAP 政策 v102025，2026-11-22 核）：</b>'
        '每条 AI 使用都要记录原始提问与<b>完整输出</b>（不是摘要）；生成内容必须人工验证后才可进论文；'
        '纯翻译类可只附一句声明。报告格式见 <a href="../docs/02_%E7%9F%A5%E8%AF%86%E6%A8%A1%E5%9D%97/07_%E5%86%99%E4%BD%9C%E4%B8%8ESummarySheet.html">07_写作与SummarySheet</a> §1.5 与官方 AI Policy。</div>',
    ]
    items = []
    for idx, (c, name, when, text, note) in enumerate(PROMPTS):
        items.append(
            '<div class="pr" data-c="{c}" style="display:none">'
            '<h3>{idx}. {name} <span class="cat-tag" style="font-size:11px;color:#786E60">[{c}]</span></h3>'
            '<div class="when">何时用：{when}</div>'
            '<button class="btn" data-k="{idx}">复制提示词</button>'
            '<pre id="p{idx}">{text}</pre>'
            '<div class="note">纪律：{note}</div></div>'.format(
                idx=idx, c=c, name=name, when=when,
                text=text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'),
                note=note))
    body.append(chr(10).join(items))
    script = """
function bind(){
  document.querySelectorAll('.cat').forEach(function(el){
    el.addEventListener('click', function(){
      document.querySelectorAll('.cat').forEach(function(x){x.classList.remove('on');});
      el.classList.add('on');
      var c = el.dataset.c;
      document.querySelectorAll('.pr').forEach(function(p){
        p.style.display = (c === '全部' || p.dataset.c === c) ? 'block' : 'none';
      });
    });
  });
  document.querySelectorAll('.pr').forEach(function(p){ p.style.display='block'; });
  document.querySelectorAll('button[data-k]').forEach(function(b){
    b.addEventListener('click', function(){
      var k = b.dataset.k, pre = document.getElementById('p'+k);
      var txt = pre.textContent;
      var done = function(){ b.textContent = '已复制 ✓'; setTimeout(function(){ b.textContent='复制提示词'; }, 1500); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(txt).then(done, function(){ fallback(txt, done); });
      } else { fallback(txt, done); }
    });
  });
}
function fallback(txt, done){
  var ta = document.createElement('textarea');
  ta.value = txt; document.body.appendChild(ta); ta.select();
  try { document.execCommand('copy'); done(); } catch(e) {}
  document.body.removeChild(ta);
}
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', bind); else bind();
"""
    desc = "MCM/ICM 备赛工具：赛时 AI 协作提示词 12 条（一键复制）。纪律与披露要求随附，数据不联网。"
    html = page("提示词包", "赛时工具", desc, chr(10).join(body), script, uiroot="../", ev=EV)
    html = html.replace("</style>", PROMPTS_CSS + chr(10) + "</style>", 1)
    _finish("prompts.html", html, "提示词包")


ASM_CSS = """
.f{border:1px solid #D9D0BD;background:#FDFCF8;border-radius:4px;padding:14px 18px;margin-bottom:10px}
.f h3{margin:0 0 8px;font-size:14px}
.f label{display:inline-block;margin:4px 14px 4px 0;font-size:13px}
.f input[type=text]{width:200px;border:1px solid #E7E0D1;border-radius:3px;padding:5px 8px;font-family:inherit}
.f select{border:1px solid #E7E0D1;border-radius:3px;padding:5px 8px;font-family:inherit}
#texout{display:none;margin-top:12px}
#texview{background:#F9F6EF;border:1px solid #E7E0D1;border-radius:4px;padding:12px 16px;
         font-family:ui-monospace,Consolas,monospace;font-size:11.5px;line-height:1.7;
         max-height:340px;overflow:auto;white-space:pre}
.suggest{font-size:13px;color:#6E6557;margin-top:4px}
"""


def build_assembler():
    body = [
        '<p class="suggest">用途：赛前生成 MCM 论文 LaTeX 骨架（含 Summary Sheet 结构、按所选模型组合的章节、'
        'AI 披露附录占位），骨架注释里内嵌各模块纪律提醒。生成完全在本页完成，不联网。编译请用本地 XeLaTeX/Overleaf。</p>',
        '<div class="f"><h3>① 基本信息</h3>'
        '<label>题目：<select id="prob"><option value="A">A</option><option value="B">B</option>'
        '<option value="C">C</option><option value="D">D</option><option value="E">E</option>'
        '<option value="F">F</option></select></label>'
        '<label>控制号：<input type="text" id="ctl" placeholder="公布后填写"></label>'
        '<label>队名可留空：<input type="text" id="team" placeholder="Team (可选)"></label></div>',
        '<div class="f"><h3>② 模型组合（勾选的进骨架）</h3>'
        '<label><input type="checkbox" value="ode" checked> 微分方程 / 动力学</label>'
        '<label><input type="checkbox" value="opt" checked> 优化（LP/MILP）</label>'
        '<label><input type="checkbox" value="stat"> 统计 / 机器学习</label>'
        '<label><input type="checkbox" value="net"> 图论 / 网络</label>'
        '<label><input type="checkbox" value="mcdm"> 评价 / 多准则决策</label>'
        '<label><input type="checkbox" value="mc" checked> 蒙特卡洛 / 模拟</label></div>',
        '<div class="f"><h3>③ 生成</h3>'
        '<button class="btn solid" id="gen">生成骨架</button> '
        '<a class="btn" id="dl" style="display:none" download="mcm-skeleton.tex">下载 .tex</a>'
        '<p class="suggest">生成后：把 §Summary 六要素模板逐槽填掉；每个 section 的注释是纪律检查点；'
        'AI 报告附录按官方政策放完整提问与输出。</p></div>',
        '<div id="texout"><div id="texview"></div></div>',
    ]
    script = """
var TM={A:'02_微分方程与动力学',B:'01_优化方法族',C:'03_统计与机器学习',D:'04_图论与网络',
        E:'05_评价与决策',F:'07_写作与SummarySheet'};
function gen(){
  var prob=document.getElementById('prob').value;
  var ctl=document.getElementById('ctl').value.trim();
  var team=document.getElementById('team').value.trim();
  var use={};
  document.querySelectorAll('.f input[type=checkbox]').forEach(function(c){
    if(c.checked) use[c.value]=true; });
  var L=[];
  L.push('% MCM/ICM 2027 LaTeX 骨架 —— 由 mcm-archive 论文组装机生成');
  L.push('% 题目 '+prob+'；纪律注释来自 mcm-archive 知识模块，逐条核对后再删');
  L.push('\\\\documentclass[11pt]{article}');
  L.push('\\\\usepackage[margin=1in]{geometry}');
  L.push('\\\\usepackage{amsmath,amssymb,graphicx,booktabs,hyperref}');
  L.push('\\\\usepackage{authblk}');
  L.push('\\\\title{The ' + prob + ' Problem: 【把题面问题翻译成一句可研究的问题】}');
  if (team) L.push('\\\\author{'+team+'}');
  if (ctl) L.push('\\\\date{Team Control Number: '+ctl+'}');
  else L.push('\\\\date{Team Control Number: 【公布后填写】}');
  L.push('\\\\begin{document}');
  L.push('\\\\maketitle');
  L.push('');
  L.push('% ============ Summary Sheet（六要素，全部带数字） ============');
  L.push('\\\\section*{Summary}');
  L.push('% ① 问题与目标：具体到量（ 我们要决定/预测/评估的是什么 ）');
  L.push('% ② 方法主线：模型链条 + 每一环的输入输出（ 如 ODE 刻画机理 -> 蒙特卡洛灌入不确定性 -> 分位数结论 ）');
  L.push('% ③ 关键结果：2-3 句，每句 = 数值 + 单位 + 对照物（ 比基准低 12% 而非 显著降低 ）');
  L.push('% ④ 检验与稳健性：收敛/样本外/敏感度至少一句');
  L.push('% ⑤ 亮点或政策含义：一句话');
  L.push('% 提醒：Summary 每天写一版，最后一天做压缩与数字对账，不要从零写');
  L.push('');
  L.push('\\\\section{Introduction}');
  L.push('% 把题面翻译成 我们要决定什么 ；问题编号 <-> 论文小节一一映射');
  L.push('');
  L.push('\\\\section{Assumptions and Justifications}');
  L.push('% 每条假设编号 A1, A2, ...，每条给 justifications（ 来自什么机制/文献/数据 ）');
  L.push('% 扩展问题换模型时，本节必须同步更新');
  L.push('');
  L.push('\\\\section{Notations}');
  L.push('% 符号表：符号 / 含义 / 单位 三列');
  L.push('');
  if (use.ode) {
    L.push('\\\\section{Model I: Dynamic Model}');
    L.push('% 机理方程：右端每一项指着说 来自什么机制');
    L.push('% 无量纲化 -> solve_ivp（rtol/atol/max_step 写进正文）-> 收敛性检验 -> 守恒量漂移检查');
    L.push('% 多时间尺度（比值 > 1e3）换 BDF/LSODA；平衡点线性化 + 特征值判稳');
    L.push('');
  }
  if (use.opt) {
    L.push('\\\\section{Model II: Optimization Model}');
    L.push('% 三行翻译（变量/目标/约束）先于代码；变量类型表（哪些 0-1/整数/连续，为什么）');
    L.push('% big-M = 系数*变量上界+eps（禁 1e6）；对称对象加字典序约束；报告 最优值/gap/时间 三件套');
    L.push('% infeasible 三步排查：区间表找冲突 / 单位 / big-M 压死可行域');
    L.push('');
  }
  if (use.stat) {
    L.push('\\\\section{Statistical Analysis}');
    L.push('% 清洗流水线表（步骤/理由/影响行数）进附录；EDA 三件套（分布/相关/时序）');
    L.push('% 预测任务只认样本外误差：训练/验证/测试三分，测试集只用一次；时序防泄漏（只往前填）');
    L.push('% 共线性查相关矩阵与 VIF；聚类先标准化+固定种子');
    L.push('');
  }
  if (use.net) {
    L.push('\\\\section{Network Model}');
    L.push('% 节点/边/权定义表先行（语义决定一切）；Dijkstra 前提边权非负；最大流报告最小割');
    L.push('% 中心性多指标互证（度/介数/接近按用途选）；鲁棒性删点实验给决策依据');
    L.push('');
  }
  if (use.mcdm) {
    L.push('\\\\section{Evaluation Model}');
    L.push('% 指标来源声明；逆指标变换（含 0 值禁用 1/x）；极差正规化');
    L.push('% AHP 过 CR<0.1；熵权与主观法组合；劣解淘汰设硬底线；权重 ±20% 敏感度 -> 条件化结论');
    L.push('');
  }
  if (use.mc) {
    L.push('\\\\section{Monte Carlo Simulation}');
    L.push('% 固定种子（default_rng）写进论文；输入分布三级来源声明（数据/三角估算/文献）');
    L.push('% 样本量按 (1.96 sigma / eps)^2 估；报分位数与超限概率，不报单点；排队仿真丢弃预热期');
    L.push('');
  }
  L.push('\\\\section{Sensitivity Analysis}');
  L.push('% LP 用影子价格；MILP 参数扫描报趋势与拐点；权重扰动给条件化结论');
  L.push('');
  L.push('\\\\section{Strengths and Weaknesses}');
  L.push('% 诚实，弱点配改进方向');
  L.push('');
  L.push('\\\\section{Conclusion}');
  L.push('% 条件化结论 + 谁该做什么 + 怎么度量效果');
  L.push('');
  L.push('\\\\begin{thebibliography}{9}');
  L.push('% 外部数据 / 他人图表与结论 / AI 工具都要进引用列表；图注标数据来源');
  L.push('\\\\end{thebibliography}');
  L.push('');
  L.push('\\\\appendix');
  L.push('\\\\section{Appendix A: Code}');
  L.push('% 环境锁定说明（requirements.txt 与版本号）');
  L.push('');
  L.push('\\\\section{Appendix B: Report on Use of AI}');
  L.push('% COMAP 政策 v102025：每条 Query 原文 + Output 完整原文；纯翻译类可附一句声明');
  L.push('% 生成内容必须人工验证后才可进论文——未验证与未披露同样危险');
  L.push('');
  L.push('\\\\end{document}');
  var tex = L.join('\\n');
  document.getElementById('texview').textContent = tex;
  document.getElementById('texout').style.display = 'block';
  var blob = new Blob([tex], {type:'text/plain'});
  var a = document.getElementById('dl');
  a.href = URL.createObjectURL(blob);
  a.style.display = 'inline-flex';
  a.download = 'mcm-' + prob + '-skeleton.tex';
}
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', function(){
  document.getElementById('gen').addEventListener('click', gen);
}); else document.getElementById('gen').addEventListener('click', gen);
"""
    desc = "MCM/ICM 备赛工具：生成 LaTeX 论文骨架（Summary 六要素模板 + 按模型组合的章节 + AI 披露附录），纪律内嵌注释。"
    html = page("论文组装机", "赛时工具", desc, chr(10).join(body), script, uiroot="../", ev=EV)
    html = html.replace("</style>", ASM_CSS + chr(10) + "</style>", 1)
    _finish("assembler.html", html, "论文组装机")


def build():
    build_selector()
    build_budget()
    build_warroom()
    build_flashcards()
    build_prompts()
    build_assembler()
