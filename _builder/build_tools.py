# -*- coding: utf-8 -*-
"""build_tools.py — 生成 06_赛时工具/ 交互工具页（每页前三行为定位声明）"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import EVENT_START_MS, EVENT_END_MS
EV = (EVENT_START_MS, EVENT_END_MS)
from page_shell import page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

TOOL_CSS = """
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

# 选型问卷：选项 → 题型计分（基于 2024-2026 官方题面画像，核查 2026-11-22）
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
html = html.replace("</style>", TOOL_CSS + "\n</style>", 1)
out = P("06_赛时工具", "selector.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)
print("  tools: selector.html {} KB".format(os.path.getsize(out) // 1024))


def build():
    pass
