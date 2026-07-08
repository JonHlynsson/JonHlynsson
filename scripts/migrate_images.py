"""One-time migration: download WordPress media referenced in Markdown,
save locally to src/assets/wp/, and rewrite all links.
Runs inside GitHub Actions (see .github/workflows/migrate-images.yml)."""
import re, glob, os, urllib.request, urllib.parse

PATTERN = re.compile(
    r'https://(?:i\d\.wp\.com/)?jonhlynsson\.com/(wp-content/uploads/[^")\s]+?)(\?[^")\s]*)?(?=[")\s]|$)'
)

os.makedirs("src/assets/wp", exist_ok=True)
mapping = {}  # uploads path -> local site path

files = glob.glob("src/**/*.md", recursive=True) + glob.glob("src/*.md")
for f in set(files):
    for m in PATTERN.finditer(open(f, encoding="utf-8").read()):
        path = m.group(1)
        if path not in mapping:
            name = "-".join(path.split("/")[2:])  # 2024/03/foo.jpg -> 2024-03-foo.jpg
            name = urllib.parse.unquote(name).replace(" ", "-")
            mapping[path] = f"/assets/wp/{name}"

print(f"{len(mapping)} unique media files to migrate")
failed = []
for path, local in mapping.items():
    dest = "src" + local
    if os.path.exists(dest):
        continue
    url = f"https://jonhlynsson.com/{urllib.parse.quote(path)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site migration)"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as out:
            out.write(r.read())
        print("ok:", path)
    except Exception as e:
        print("FAILED:", path, e)
        failed.append(path)

# Rewrite links only for files that downloaded successfully
ok = {p: l for p, l in mapping.items() if p not in failed}
def repl(m):
    return ok.get(m.group(1), m.group(0))
for f in set(files):
    s = open(f, encoding="utf-8").read()
    s2 = PATTERN.sub(repl, s)
    if s2 != s:
        open(f, "w", encoding="utf-8").write(s2)
        print("rewrote:", f)

print(f"Done. {len(ok)} migrated, {len(failed)} failed.")
if failed:
    print("Failed files keep their original URLs — re-run the workflow to retry.")
