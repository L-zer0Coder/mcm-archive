# -*- coding: utf-8 -*-
"""check.py — 独立体检（不依赖构建）：断链 / docs 同步 / 孤儿页"""
import os, re, glob, json
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

idx = {}
for dp, dns, fns in os.walk(ROOT):
    rel = os.path.relpath(dp, ROOT).replace(os.sep, "/")
    if ".git" in rel.split("/") or "__pycache__" in rel.split("/") or rel == "docs" or rel.startswith("docs/"):
        if os.path.basename(dp) == "__pycache__" or ".git" == os.path.basename(dp):
            dns[:] = []
            continue
    for fn in fns:
        r = ("" if rel == "." else rel + "/") + fn
        r = r.replace(os.sep, "/")
        if r.startswith("docs/"):
            idx.setdefault(r.lower(), r)

# docs 与 md 对账
mds = set()
for d in ("01_COMAP官方", "02_知识模块", "03_题型打法", "04_语料库", "05_论文拆解", "06_赛时工具", "07_资源导航"):
    for f in glob.glob(P(d, "**", "*.md"), recursive=True):
        rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
        mds.add(rel.replace(os.sep, "/")[:-3] + ".html")
docs_html = set()
for f in glob.glob(P("docs", "**", "*.html"), recursive=True):
    docs_html.add(os.path.relpath(f, P("docs")).replace(os.sep, "/"))
orphan = docs_html - {m.replace("docs/", "") for m in mds}
missing = {m.replace("docs/", "") for m in mds} - docs_html

# 链接校验
href_re = re.compile(r'(?:href|src)="([^"]+)"')
dead_re = re.compile(r"\]\([^) ]{1,200}\)")  # 正文里残留的 ](...) 死链接痕迹
bad = []
pages = [P("index.html")] + list(glob.glob(P("docs", "**", "*.html"), recursive=True))
for pg in pages:
    base = os.path.dirname(pg)
    text = open(pg, encoding="utf-8").read()
    body = re.sub(r"<pre[\s\S]*?</pre>|<code[\s\S]*?</code>", " ", text)
    for m in dead_re.finditer(body):
        frag = body[max(0, m.start() - 60):m.start() + 60]
        if "<pre" not in frag and "<code" not in frag:
            bad.append(("DEADLINK", os.path.relpath(pg, ROOT), m.group(0)[:60]))
    for u in href_re.findall(text):
        if re.match(r"^(https?:|data:|#|mailto:|javascript:)", u) or "'" in u or "+" in u:
            continue
        dec = unquote(u.split("#")[0])
        if not dec:
            continue
        abspath = os.path.normpath(os.path.join(base, dec))
        rel = os.path.relpath(abspath, ROOT).replace(os.sep, "/")
        if rel.startswith(".."):
            bad.append(("MISSING", os.path.relpath(pg, ROOT), dec))
            continue
        if not os.path.exists(abspath):
            bad.append(("MISSING", os.path.relpath(pg, ROOT), rel))

print(json.dumps({
    "docs_html": len(docs_html),
    "md_sources": len(mds),
    "orphan_html": sorted(orphan)[:5],
    "missing_html": sorted(missing)[:5],
    "broken_links": len(bad),
}, ensure_ascii=False))
for kind, f, u in bad[:15]:
    print("  [{}] {} -> {}".format(kind, f, u))
if bad or orphan or missing:
    raise SystemExit(1)
print("check ok")
