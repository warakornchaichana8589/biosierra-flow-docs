"""Bundle every flow page in pages/ into one self-contained index.html with a tab menu.

Each page keeps its own styles: it is rendered inside an iframe (srcdoc), so the
pages' CSS never collides. Edit a page in pages/, then run:  python build.py
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent

# Menu order = order of the real process: weighing -> QC fail / Disposition -> supplier claim.
PAGES = [
    ("weighing", "ใบตวงสาร", "pages/weighing.html"),
    ("disposition", "Disposition (Lot ไม่ผ่าน)", "pages/disposition.html"),
    ("supplier-claim", "เคลมผู้ขาย", "pages/supplier-claim.html"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BioSierra ERP — Flow</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%231f2933'/%3E%3Cpath d='M20 20h12a6 6 0 0 1 6 6v12a6 6 0 0 0 6 6' fill='none' stroke='%23f08c00' stroke-width='5' stroke-linecap='round'/%3E%3Ccircle cx='18' cy='20' r='7' fill='%23f08c00'/%3E%3Ccircle cx='46' cy='44' r='7' fill='%23fff'/%3E%3C/svg%3E">
<style>
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;background:#f6f7f9;font-family:"Sarabun","Noto Sans Thai","Leelawadee UI",system-ui,sans-serif}
  body{display:flex;flex-direction:column}
  header{display:flex;align-items:center;gap:18px;flex-wrap:wrap;padding:10px 20px;background:#1f2933;color:#fff}
  header .brand{font-weight:700;font-size:16px;white-space:nowrap}
  nav{display:flex;gap:6px;flex-wrap:wrap}
  nav a{color:#cbd2d9;text-decoration:none;font-size:14px;font-weight:600;padding:6px 14px;border-radius:999px}
  nav a:hover{background:#323f4b;color:#fff}
  nav a[aria-current="page"]{background:#f08c00;color:#fff}
  iframe{flex:1;width:100%;border:0;background:#fff}
</style>
</head>
<body>
<header>
  <span class="brand">BioSierra ERP · Flow</span>
  <nav>__NAV__</nav>
</header>
<iframe id="view" title="flow"></iframe>
<script>
const PAGES = __DATA__;
const view = document.getElementById('view');
function show() {
  const id = location.hash.slice(1);
  const page = PAGES.find(p => p.id === id) || PAGES[0];
  view.srcdoc = page.html;
  document.title = page.label + ' — BioSierra ERP Flow';
  document.querySelectorAll('nav a').forEach(a => {
    if (a.dataset.id === page.id) a.setAttribute('aria-current', 'page');
    else a.removeAttribute('aria-current');
  });
}
window.addEventListener('hashchange', show);
show();
</script>
</body>
</html>
"""


def main():
    data = []
    nav = []
    for pid, label, rel in PAGES:
        src = (ROOT / rel).read_text(encoding="utf-8")
        data.append({"id": pid, "label": label, "html": src})
        nav.append(f'<a href="#{pid}" data-id="{pid}">{html.escape(label)}</a>')
    # "</" must not appear inside the inline <script> block.
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = TEMPLATE.replace("__NAV__", "".join(nav)).replace("__DATA__", blob)
    (ROOT / "index.html").write_text(out, encoding="utf-8", newline="\n")
    print(f"index.html written: {len(PAGES)} pages, {len(out.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
