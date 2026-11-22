# -*- coding: utf-8 -*-
"""builder.py — mcm-archive 构建器主入口
用法：python _builder/builder.py   （构建 index + 文档页 + 全局挂件 + 链接校验）
"""
import os, re, json, glob, sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import (BRAND, PROBLEMS, MODULES, EVENT_START_MS, EVENT_END_MS,
                       EVENT_LABEL, EVENT_HOURS, PHASES, ACC)
from page_shell import page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
OUT_DOCS = os.path.join(ROOT, "docs")

DOC_ROOTS = ["01_COMAP官方", "02_知识模块", "03_题型打法"]
EV = (EVENT_START_MS, EVENT_END_MS)


def render_docs():
    os.makedirs(OUT_DOCS, exist_ok=True)
    built = []
    import markdown as _m
    md = _m.Markdown(extensions=["tables", "fenced_code", "sane_lists"], output_format="html5")
    for root in DOC_ROOTS:
        for f in sorted(glob.glob(P(root, "**", "*.md"), recursive=True)):
            rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
            if os.path.basename(f).startswith("_"):
                continue
            out_rel = rel[:-3] + ".html"
            out = os.path.join(OUT_DOCS, *out_rel.split("/"))
            page_dir = os.path.dirname(out)
            text = open(f, encoding="utf-8").read()
            # 链接重写：md 内相对链接 → 相对【输出页目录】的产物路径（与 UPC link_from 同构）
            base_dir = os.path.dirname(f)
            def link_to(abs_t):
                return quote(os.path.relpath(abs_t, page_dir).replace(os.sep, "/"))
            def sub(m):
                label, tgt = m.group(1), m.group(2).strip()
                if re.match(r"^(https?:|data:|#|mailto:)", tgt):
                    return m.group(0)
                tgt_clean, frag = tgt, ""
                if "#" in tgt:
                    tgt_clean, frag = tgt.split("#", 1)
                    frag = "#" + frag
                abs_t = os.path.normpath(os.path.join(base_dir, tgt_clean))
                if os.path.exists(abs_t):
                    if abs_t.lower().endswith(".md"):
                        t_rel = os.path.relpath(abs_t, ROOT).replace(os.sep, "/")[:-3] + ".html"
                        return "[{}]({}{})".format(
                            label, link_to(os.path.join(OUT_DOCS, *t_rel.split("/"))), frag)
                    return "[{}]({}{})".format(label, link_to(abs_t), frag)
                return "\\[" + label + "\\](" + tgt + ")"
            text = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", sub, text)
            # 数学隔离：公式先抽走再转 markdown，防 $x_{ij}$ 被斜体/转义破坏（代码围栏不动）
            stash = []
            def stash_math(m):
                stash.append(m.group(0))
                return "QQMATH{}QQ".format(len(stash) - 1)  # 纯字母数字，markdown 不动它
            seg = text.split("```")
            for j in range(0, len(seg), 2):  # 偶数段在围栏外
                seg[j] = re.sub(r"\$\$[^$]+\$\$|\$[^$\n]+\$", stash_math, seg[j])
            text = "```".join(seg)
            m = re.match(r"\s*#\s+(.+)", text)
            title = m.group(1).strip() if m else os.path.splitext(os.path.basename(f))[0]
            if m:
                text = text[m.end():]  # 标题交给页面骨架渲染，正文不重复
            html = md.reset().convert(text)
            for i, s in enumerate(stash):
                html = html.replace("QQMATH{}QQ".format(i), s)
            # 任务清单：- [ ] / - [x] → 勾选框（免 pymdownx 依赖）
            html = html.replace("<li>[ ] ", '<li><input type="checkbox" disabled> ')
            html = html.replace("<li>[x] ", '<li><input type="checkbox" checked disabled> ')
            html = html.replace("<li>[X] ", '<li><input type="checkbox" checked disabled> ')
            crumb = rel.split("/")[0]
            os.makedirs(os.path.dirname(out), exist_ok=True)
            page_html = page(title, crumb,
                             "MCM/ICM 备赛知识库 · " + title,
                             html, "", uiroot="../../", ev=EV)
            with open(out, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(page_html)
            built.append((rel, title))
    return built


def render_index(built_docs):
    cards = "".join(
        '<div class="card" style="margin-bottom:10px"><b style="font-family:var(--serif)">{cn}</b>'
        '<span style="color:var(--dim);font-size:12px;margin-left:8px">{org} · {ty}</span>'
        '<p style="margin:6px 0;font-size:13px;color:var(--mut)">{desc}</p>'
        '<div style="font-size:12px;color:var(--acc)">方法族：{methods}</div>'
        '<div style="font-size:12px;color:var(--dim);margin-top:4px">适合：{suit}</div></div>'.format(
            cn=x["type"], org=x["org"], ty=x["code"],
            desc=x["desc"], methods=" / ".join(x["methods"]), suit=x["suit"])
        for x in PROBLEMS)
    mods = "".join(
        '<tr><td>{id}</td><td>{nm}</td><td>{st}</td><td>{entry}</td></tr>'.format(
            id=x["id"], nm=x["name"],
            st=("✓ 就绪" if x["status"] == "ready" else "M" + x["id"] + " 待写"),
            entry=('<a href="docs/{fu}">{f}</a>'.format(
                       fu=quote(x["file"][:-3] + ".html"),
                       f=os.path.basename(x["file"]))
                   if x["status"] == "ready"
                   else '<span style="color:var(--dim)">{f}（待写）</span>'.format(
                       f=os.path.basename(x["file"]))))
        for x in MODULES)
    phases = "".join(
        '<tr><td>{c}</td><td>{t}</td><td>{d}</td><td class="num">{a}–{b}h</td></tr>'.format(
            c=ph[2], t=ph[3], d=ph[4], a=ph[0], b=ph[1]) for ph in PHASES)
    body = (
        '<div class="card" style="margin-bottom:14px">'
        '<b style="font-family:var(--serif);font-size:16px">' + EVENT_LABEL + '</b>'
        '<p style="margin:6px 0;font-size:13px;color:var(--mut)">96 小时 · 3 人一队 · 六题选一 · 25 页英文论文 ·  价值：国际认可 + 保研加分</p>'
        '<div id="clockrow" style="margin-top:8px"></div></div>'
        '<h2 style="font-family:var(--serif)">六大题型 · 选对题赢一半</h2>'
        '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px">' + cards + '</div>'
        '<h2 style="font-family:var(--serif);margin-top:26px">方法族模块（学习核心）</h2>'
        '<table><thead><tr><th>#</th><th>模块</th><th>状态</th><th>入口</th></tr></thead><tbody>' + mods + '</tbody></table>'
        '<h2 style="font-family:var(--serif);margin-top:26px">96 小时作战室阶段表</h2>'
        '<table><thead><tr><th>阶段</th><th>任务</th><th>要点</th><th>时间</th></tr></thead><tbody>' + phases + '</tbody></table>'
        '<p style="margin-top:14px;font-size:12.5px;color:var(--dim)">本站为 2027 MCM/ICM 备赛知识库 · '
        '构建自 upc-archive 管线 · 官方事实核查于 2026-11-21</p>')
    script = """
(function(){
  var S=EV_START, E=EV_END, el=document.getElementById('clockrow');
  function p2(n){return n<10?'0'+n:''+n;}
  function upd(){var t=Date.now();
    if(t<S){var ms=S-t,d=Math.floor(ms/864e5),h=Math.floor(ms%864e5/36e5),m=Math.floor(ms%36e5/6e4),s=Math.floor(ms%6e4/1e3);
      el.innerHTML='<b style="font-family:var(--serif);font-size:22px">开赛倒计时 '+d+' 天 '+p2(h)+':'+p2(m)+':'+p2(s)+
        '</b> <span style="color:var(--dim);font-size:12px">（'+new Date(S).toLocaleString()+'）</span>';}
    else if(t<E){var u=Math.floor((t-S)/1000);
      el.innerHTML='<b style="font-family:var(--serif);font-size:22px;color:var(--acc)">赛中</b> '+
        p2(Math.floor(u/3600))+':'+p2(Math.floor(u%3600/60))+':'+p2(u%60);}
    else{el.innerHTML='<b style="font-family:var(--serif);font-size:20px">已结束</b>';}}
  upd();setInterval(upd,1000);
})();
"""
    html = page("MCM/ICM 备赛知识库", "首页",
                "MCM/ICM 2027 备赛知识库：方法族学习、O 奖语料对照、赛时工具。",
                body, script, uiroot="", ev=EV, doc_title="首页 · MCM/ICM 备赛知识库")
    with open(P("index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def gen_global_ui():
    """生成 global-ui.js（挂件逻辑）+ global-ui-data.js（树 + 说明数据），全部根相对"""
    css = '\n'.join([
        ".uig-btnL,.uig-btnR{position:fixed;top:50%;transform:translateY(-50%);z-index:85;",
        "writing-mode:vertical-rl;letter-spacing:.2em;font-size:12.5px;padding:14px 6px;",
        "border:1px solid #D9D0BD;background:#FDFCF8;color:#6E6557;cursor:pointer;font-family:inherit}",
        ".uig-btnL{left:0;border-left:none;border-radius:0 4px 4px 0}",
        ".uig-btnR{right:0;border-right:none;border-radius:4px 0 0 4px}",
        ".uig-btnL:hover,.uig-btnR:hover{color:#2B5C8A;border-color:#2B5C8A}",
        ".uig-panel{position:fixed;top:0;bottom:0;width:min(380px,88vw);z-index:95;background:#F7F4ED;",
        "box-shadow:0 0 40px rgba(43,92,138,.25);transition:transform .25s;overflow-y:auto;visibility:hidden}",
        ".uig-panel.on{visibility:visible}",
        "#uig-nav{left:0;transform:translateX(-105%)}#uig-nav.on{transform:none}",
        "#uig-doc{right:0;transform:translateX(105%)}#uig-doc.on{transform:none}",
        ".uig-h{font-family:Georgia,serif;font-size:16px;font-weight:700;padding:14px 16px;border-bottom:1px solid #E7E0D1}",
        ".uig-x{position:absolute;top:10px;right:10px;width:30px;height:30px;border:1px solid #D9D0BD;background:#FDFCF8;border-radius:3px;font-size:16px;color:#6E6557;cursor:pointer}",
        ".uig-tree,.uig-doc{padding:8px 12px 20px;font-size:13px;line-height:2}",
        ".uig-tn{line-height:2}",
        ".uig-tn a{color:#2B5C8A}.uig-tn a:hover{text-decoration:underline}",
        ".uig-c{width:18px;height:18px;border:none;background:none;color:#6E6557;cursor:pointer;font-family:monospace;padding:0;margin-right:3px}",
        ".uig-kids{border-left:1px dashed #D9D0BD;margin-left:8px}",
        "@media print{.uig-btnL,.uig-btnR,.uig-panel{display:none!important}}",
    ])
    logic = (
        "(function(){\n"
        "var R=window.UPC_UI_ROOT||'';\n"
        "function esc(s){return String(s).replace(/[&<>\"]/g,function(c){"
        "return{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c];});}\n"
        "var st=document.createElement('style');st.textContent=" + json.dumps(css) + ";document.head.appendChild(st);\n"
        "var open=false,current='';\n"
        "function toggle(side){\n"
        "  if(current===side){close();return;}\n"
        "  var old=document.getElementById('uig-'+current);if(old)old.remove();\n"
        "  current=side;open=true;\n"
        "  ensureData(function(){\n"
        "    var w=document.createElement('div');w.id='uig-'+side;w.className='uig-panel on';\n"
        "    w.innerHTML='<button class=\"uig-x\" type=\"button\">×</button>'+(side==='nav'?navHtml():docHtml());\n"
        "    w.querySelector('.uig-x').addEventListener('click',close);\n"
        "    document.body.appendChild(w);\n"
        "    if(side==='nav')bindTree(w);\n"
        "  });\n"
        "}\n"
        "function close(){var p=document.getElementById('uig-'+current);if(p)p.remove();current='';open=false;}\n"
        "function ensureData(cb){if(window.UPC_UI_DATA)return cb();\n"
        "  var s=document.createElement('script');s.src=R+'global-ui-data.js';\n"
        "  s.onload=cb;s.onerror=function(){alert('导航数据加载失败');};document.head.appendChild(s);}\n"
        "function navHtml(){return '<div class=\"uig-h\">☰ 全站目录</div><div style=\"padding:6px 10px\">"
        "<input id=\"uig-q\" placeholder=\"过滤…\" style=\"width:calc(100% - 20px);margin:0 10px;height:28px;"
        "border:1px solid #D9D0BD;border-radius:3px;font-size:12.5px\"></div><div id=\"uig-tree\"></div>';}\n"
        "function docHtml(){return '<div class=\"uig-h\">📖 全站说明</div><div style=\"padding:8px 14px\">'"
        "+window.UPC_UI_DATA.manual+'</div>';}\n"
        "function bindTree(w){\n"
        "  var tree=w.querySelector('#uig-tree');\n"
        "  tree.innerHTML=nodeHtml(window.UPC_UI_DATA.tree,0);\n"
        "  var rk=tree.querySelector(':scope > div.uig-kids');if(rk)rk.style.display='block';\n"
        "  tree.addEventListener('click',function(ev){var b=ev.target.closest('.uig-c');if(!b)return;\n"
        "    var k=b.parentElement.nextElementSibling;var o=k.style.display!=='none';\n"
        "    k.style.display=o?'none':'block';b.textContent=o?'▸':'▾';});\n"
        "  var q=w.querySelector('#uig-q');\n"
        "  q.addEventListener('input',function(){var kw=this.value.trim().toLowerCase();\n"
        "    var tns=tree.querySelectorAll('.uig-tn');\n"
        "    tns.forEach(function(d){d.style.display=(!kw||d.textContent.toLowerCase().indexOf(kw)>=0)?'':'none';});\n"
        "    tree.querySelectorAll('.uig-kids').forEach(function(k){k.style.display=kw?'block':'none';});\n"
        "    if(!kw){var rk=tree.querySelector(':scope > div.uig-kids');if(rk)rk.style.display='block';}});\n"
        "}\n"
        "function nodeHtml(n,depth){\n"
        "  var row='<div class=\"uig-tn\" style=\"padding-left:'+(depth*13+4)+'px\">'+\n"
        "    (n.ch?'<button class=\"uig-c\" type=\"button\">▸</button>':'<span style=\"color:#D9D0BD;margin:0 5px 0 9px\">·</span>')+\n"
        "    (n.u?'<a href=\"'+R+n.u+'\">'+esc(n.n)+'</a>':'<span>'+esc(n.n)+'</span>')+\n"
        "    (n.d?' <span style=\"color:#8a8172;font-size:10.5px\">'+esc(n.d)+'</span>':'')+'</div>';\n"
        "  if(n.ch)row+='<div class=\"uig-kids\" style=\"display:none\">'+\n"
        "    n.ch.map(function(c){return nodeHtml(c,depth+1);}).join('')+'</div>';\n"
        "  return row;\n"
        "}\n"
        "function btn(side,label){var b=document.createElement('button');b.id='uig-'+side+'-btn';\n"
        "  b.type='button';b.textContent=label;b.className=(side==='nav'?'uig-btnL':'uig-btnR');\n"
        "  b.addEventListener('click',function(){toggle(side);});\n"
        "  document.body.appendChild(b);}\n"
        "function init(){btn('nav','☰ 目录');btn('doc','📖 说明');}\n"
        "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();\n"
        "})();\n")
    with open(P("global-ui.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(logic)


def gen_data():
    """global-ui-data.js：树（构建期扫描）+ 说明书（精简版）+ 赛事常量"""
    def node(abspath, rel, depth, maxdepth):
        """树 = 站点视图：只收录可访问页面（docs 镜像 + 根页面），标题去扩展名"""
        name = os.path.basename(rel) or rel
        if depth and name.startswith("."):
            return None
        if os.path.isfile(abspath):
            ext = os.path.splitext(name)[1].lower()
            if ext == ".html":
                return {"n": "首页" if name.lower() == "index.html" else name[:-5],
                        "u": rel.replace(os.sep, "/")}
            if ext in (".pdf", ".txt", ".png"):
                return {"n": name, "u": rel.replace(os.sep, "/")}
            return None  # js/py/json 等源码资产不进树
        if depth >= maxdepth:
            return None
        ch = []
        try:
            entries = sorted(os.listdir(abspath))
        except OSError:
            return None
        for e in entries:
            if depth and e.startswith("."):
                continue
            c = node(os.path.join(abspath, e), os.path.join(rel, e), depth + 1, maxdepth)
            if c:
                ch.append(c)
        if not ch:
            return None
        return {"n": name, "ch": ch}
    home = {"n": "首页", "u": "index.html"}
    docs_tree = node(P("docs"), "docs", 0, 4)
    tree = {"n": "全站目录", "ch": [home] + (docs_tree["ch"] if docs_tree else [])}
    manual_links = ("index.html", "docs/02_知识模块/00_学习路径.html", "docs/01_COMAP官方/竞赛要点.html")
    for u in manual_links:
        if not os.path.exists(P(u)):
            raise SystemExit("manual link missing: " + u)
    data = ("window.UPC_UI_DATA=" + json.dumps(
        {"tree": tree,
         "manual": "<p><b>MCM/ICM 备赛知识库</b> —— 点两侧 ☰ / 📖 按钮随时打开目录与说明。</p>"
                   "<p><b>核心页面：</b></p><ul>"
                   "<li><a href=\"index.html\">首页</a>：赛程时钟 · 六题型 · 方法族模块 · 96h 阶段表</li>"
                   "<li><a href=\"docs/02_知识模块/00_学习路径.html\">学习路径</a>：68 天备赛计划（先读这个）</li>"
                   "<li><a href=\"docs/01_COMAP官方/竞赛要点.html\">竞赛要点</a>：官方规则中文导读</li>"
                   "</ul>"
                   "<p><b>赛时工具页</b>（作战室 · 实验台 · 提示词包）在 M5 阶段上线。</p>"},
        ensure_ascii=False) + ";")
    with open(P("global-ui-data.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(data)
    print("  global-ui-data: {} KB".format(os.path.getsize(P("global-ui-data.js")) // 1024))


def validate():
    """链接校验：href 必须解析到真实文件 + 死链接探测（md 链接未渲染成 <a> 的残留）"""
    idx = {}
    for dp, dns, fns in os.walk(ROOT):
        rel = os.path.relpath(dp, ROOT).replace(os.sep, "/")
        if rel == ".git" or rel.startswith(".git/") or "__pycache__" in rel:
            dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
            continue
        if ".git" in rel.split("/") or "__pycache__" in rel.split("/"):
            continue
        for fn in fns:
            r = fn if rel == "." else rel + "/" + fn
            idx.setdefault(r.replace(os.sep, "/").lower(), r.replace(os.sep, "/"))
    from urllib.parse import unquote
    bad = []
    pages = [P("index.html")] + glob.glob(P("docs", "**", "*.html"), recursive=True) \
        + glob.glob(P("12_赛时工具", "*.html"))
    href_re = re.compile(r'(?:href|src)="([^"]+)"')
    dead_re = re.compile(r"\]\([^) ]{1,200}\)")  # 正文里残留的 ](...) 死链接痕迹
    dead_skips = ("<pre", "<code")
    for pg in pages:
        base = os.path.dirname(pg)
        text = open(pg, encoding="utf-8").read()
        body = re.sub(r"<pre[\s\S]*?</pre>|<code[\s\S]*?</code>", " ", text)
        for m in dead_re.finditer(body):
            frag = body[max(0, m.start() - 60):m.start() + 60].replace("\n", " ")
            if not any(s in frag for s in dead_skips):
                bad.append(("DEADLINK", os.path.relpath(pg, ROOT), m.group(0)[:60]))
        for u in href_re.findall(text):
            if re.match(r"^(https?:|data:|#|mailto:|javascript:)", u):
                continue
            if "'" in u or "+" in u or "${" in u:
                continue
            dec = unquote(u.split("#")[0])
            if not dec:
                continue
            abspath = os.path.normpath(os.path.join(base, dec))
            rel = os.path.relpath(abspath, ROOT).replace(os.sep, "/")
            if rel.startswith(".."):
                bad.append(("MISSING", os.path.relpath(pg, ROOT), dec))
                continue
            real = idx.get(rel.lower())
            if real is None:
                bad.append(("MISSING", os.path.relpath(pg, ROOT), rel))
    if bad:
        for kind, f, u in bad[:20]:
            print("  [{}] {} -> {}".format(kind, f, u))
        raise SystemExit("VALIDATION FAILED: {} broken".format(len(bad)))
    print("  validate: {} pages ok".format(len(pages)))


def main():
    print("building mcm-archive:")
    built = render_docs()
    print("  docs: {} pages".format(len(built)))
    render_index(built)
    print("  index.html")
    gen_global_ui()
    gen_data()
    validate()
    print("build complete")


if __name__ == "__main__":
    main()
