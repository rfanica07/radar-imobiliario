from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()

html = (ROOT / "index.html").read_text(encoding="utf-8")

# Paleta do Radar: verde -> azul, preservando cores semânticas de estados
replacements = {
    "#18352e": "#172033",  # texto principal
    "#697b73": "#64748b",  # texto secundário
    "#267b59": "#2563eb",  # cor principal
    "#f5f6f0": "#f4f7fb",  # fundo
    "#dfe5dc": "#dbe3ef",  # linhas
    "#173c30": "#0f172a",  # sidebar
    "#edf4e9": "#f8fafc",
    "#bde695": "#93c5fd",
    "#c9d8ca": "#dbeafe",
    "#315442": "#1d4ed8",
    "#53715e": "#3b82f6",
    "#b9cbbd": "#bfdbfe",
    "#e7eddc": "#dbeafe",
    "#48623c": "#1e3a8a",
    "#e4ebd9": "#dbeafe",
    "#f2f0df": "#eff6ff",
    "#acbda4": "#93c5fd",
    "#f4f6ef": "#eff6ff",
    "#0c231dc0": "#020617cc",
    "#183c30": "#0f172a",
    "#355543": "#1e40af",
    "#97a79d": "#94a3b8",
    "#e6eade": "#eaf1fb",
    "#e3efdc": "#dbeafe",
    "#e4f0ed": "#e0f2fe",
    "#2f8d76": "#2563eb",
    "#e9eedc": "#eaf2ff",
    "#203d33": "#1e3a5f",
    "#edf2e5": "#eef4ff",
    "#e8f1df": "#e0ecff",
}
for old, new in replacements.items():
    html = html.replace(old, new).replace(old.upper(), new)

head_additions = []
if 'rel="manifest"' not in html:
    head_additions.append('<link rel="manifest" href="./manifest.webmanifest">')
if 'name="theme-color"' not in html:
    head_additions.append('<meta name="theme-color" content="#0f172a">')
if 'apple-mobile-web-app-capable' not in html:
    head_additions.append('<meta name="apple-mobile-web-app-capable" content="yes">')
    head_additions.append('<meta name="apple-mobile-web-app-status-bar-style" content="default">')
    head_additions.append('<meta name="apple-mobile-web-app-title" content="Radar">')
if 'rel="icon"' not in html:
    head_additions.append('<link rel="icon" href="./radar-icon.svg" type="image/svg+xml">')

if head_additions and "</head>" in html:
    html = html.replace("</head>", "\n".join(head_additions) + "\n</head>", 1)

registration = '''<script>
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => navigator.serviceWorker.register("./service-worker.js"));
}
</script>'''
if "serviceWorker.register" not in html and "</body>" in html:
    html = html.replace("</body>", registration + "\n</body>", 1)

(DIST / "index.html").write_text(html, encoding="utf-8")

for name in [
    "manifest.webmanifest",
    "radar-icon.svg",
    "service-worker.js",
    "Cobertura-de-portas.json",
    "Moita-portas-cobertura.json",
]:
    src = ROOT / name
    if src.exists():
        shutil.copy2(src, DIST / name)

(DIST / ".nojekyll").write_text("", encoding="utf-8")
(DIST / "README.md").write_text(
    "# Radar Imobiliário\n\nVersão pública da aplicação Radar Imobiliário.\n",
    encoding="utf-8",
)

print(f"Versão pública criada em: {DIST}")
