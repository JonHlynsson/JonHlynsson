# jonhlynsson.com — self-hosted static site

This replaces your WordPress + Elementor site with a static site built with [Eleventy](https://www.11ty.dev/) and hosted **free** on GitHub Pages. After launch, your only recurring cost is the domain name itself.

**How it works:** your content lives as plain text files in a GitHub repository. Every time you change a file, GitHub automatically rebuilds the site and publishes it (via the workflow in `.github/workflows/deploy.yml`). You never touch a server, never update a plugin, never install anything on your computer unless you want to preview locally.

---

## What's in the box

```
├── src/
│   ├── index.njk            Homepage (hero + latest posts)
│   ├── blog.njk             Blog index (auto-generated from posts)
│   ├── posts/               ← Blog posts live here, one Markdown file each
│   ├── about.md             About page
│   ├── publications.md      Publications page
│   ├── conferences.md       Conferences page
│   ├── teaching.md          Teaching page
│   ├── cv.md                CV page
│   ├── assets/              Images, PDFs (your CV, photos, slides)
│   ├── css/style.css        All styling — design tokens at the top
│   ├── _data/site.json      Site-wide settings: name, tagline, nav, links
│   ├── _includes/layouts/   Page templates (rarely need editing)
│   ├── feed.njk             RSS feed → published at /feed.xml
│   └── CNAME                Tells GitHub Pages your domain
├── .github/workflows/deploy.yml   Automatic build + publish
├── eleventy.config.js       Build configuration
└── MIGRATION.md             How to bring your WordPress posts over
```

---

## Launch checklist (one time, ~30–45 minutes)

### Step 1 — Create the GitHub repository

1. Go to [github.com/new](https://github.com/new) (you already have an account — you use it for `jonhlynsson.github.io`).
2. Name it e.g. `jonhlynsson.com`. Set it to **Public** (required for free GitHub Pages). Don't add a README. Click **Create repository**.

### Step 2 — Upload this folder

**Option A — no software needed (GitHub web UI):**
1. On the new repository page, click **uploading an existing file**.
2. Drag the *contents* of this folder in (everything except `node_modules/` and `_site/` if present).
3. Commit. ⚠️ The web uploader sometimes skips dotfiles — check that `.github/workflows/deploy.yml` made it in. If not, create it via **Add file → Create new file**, type `.github/workflows/deploy.yml` as the name, and paste the file's contents.

**Option B — command line (if you have git):**
```bash
cd jonhlynsson-site
git init && git add . && git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/jonhlynsson.com.git
git push -u origin main
```

### Step 3 — Turn on GitHub Pages

1. In the repository: **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Go to the **Actions** tab. The "Build and deploy" workflow should run (green check ≈ 1 minute). If it didn't start, make a trivial edit to any file to trigger it.
4. Your site is now live at `https://YOURUSERNAME.github.io/jonhlynsson.com/` — but we want your real domain.

### Step 4 — Point your domain at GitHub Pages

1. In **Settings → Pages → Custom domain**, enter `jonhlynsson.com` and save. (The `src/CNAME` file keeps this setting from being wiped on rebuilds.)
2. Log in to wherever your domain is registered (the company you pay for jonhlynsson.com — possibly WordPress.com itself; see note below). Open the **DNS settings** and add:

   | Type  | Name/Host | Value |
   |-------|-----------|----------------------|
   | A     | @         | 185.199.108.153 |
   | A     | @         | 185.199.109.153 |
   | A     | @         | 185.199.110.153 |
   | A     | @         | 185.199.111.153 |
   | CNAME | www       | YOURUSERNAME.github.io |

   Delete any old A/CNAME records pointing at WordPress.
3. Back in **Settings → Pages**, wait for the DNS check to pass (minutes to a few hours), then tick **Enforce HTTPS**. GitHub provisions the SSL certificate automatically, for free.

> **If your domain is registered *through WordPress.com*:** before cancelling your plan, transfer the domain to a plain registrar (e.g. Cloudflare Registrar or Porkbun, both at-cost, ~$10/yr). WordPress.com → Upgrades → Domains → Transfer. This takes up to 5 days, so do it first.

### Step 5 — Migrate your content, then cancel WordPress

1. Follow **MIGRATION.md** to bring over your blog posts, images, and pages.
2. Fill in the placeholder sections in `publications.md`, `conferences.md`, `cv.md` (upload `cv.pdf` and your photo to `src/assets/`).
3. Delete `src/posts/2026-01-15-example-post-delete-me.md`.
4. Once the new site is live on jonhlynsson.com and you've spot-checked it, cancel the WordPress plan and Elementor subscription. Keep your WordPress export file (`.xml`) as a permanent backup.

---

## Day-to-day: writing a blog post

**Zero-install method (recommended):**
1. On GitHub, open `src/posts/`, click **Add file → Create new file**.
2. Name it `2026-08-01-my-post-title.md` (the part after the date becomes the URL: `/blog/my-post-title/`).
3. Paste this at the top and write below it in Markdown:

   ```
   ---
   title: My post title
   description: One sentence for listings and search engines.
   date: 2026-08-01
   postTags: [research, ocd]
   ---
   Your post text here. **Bold**, *italic*, [links](https://example.com).
   ```
4. Click **Commit changes**. The site rebuilds and publishes itself in ~1 minute.

**Images:** upload to `src/assets/` (via **Add file → Upload files**), then reference as `![Description](/assets/filename.jpg)`.

You can even do all of this from the GitHub mobile app.

---

## Editing everything else

- **Name, tagline, nav menu, social links:** `src/_data/site.json` — one file, plain JSON.
- **Static pages** (About, Publications, …): edit the corresponding `.md` file. They're plain Markdown with HTML comments (`<!-- -->`) marking where to paste your content.
- **Colors and fonts:** the top of `src/css/style.css` defines every design token (`--ink`, `--moss`, `--paper`, fonts). Change a hex value there and it updates site-wide.
- **The ridge-line motif** in the header/footer is an SVG path in `src/_includes/layouts/base.njk` — a nod to mountain-ultra elevation profiles. Delete the two `<svg class="ridge">` blocks if you ever tire of it.

## Previewing locally (optional)

Only needed if you want to see changes before publishing:

```bash
npm install        # once
npm start          # live preview at http://localhost:8080
```

Requires [Node.js](https://nodejs.org) 18+.

---

## Replacing the email subscription box

Static sites can't run WordPress's subscribe feature. Your options, easiest first:

1. **RSS only (already built in):** readers subscribe at `/feed.xml` with any feed reader. Zero setup.
2. **[Buttondown](https://buttondown.com)** (free up to 100 subscribers): it can watch your RSS feed and automatically email subscribers when you publish. Export your current subscriber list from WordPress (**Jetpack → Newsletter → Subscribers → Export**) and import it, then paste Buttondown's embed form into `src/index.njk`.
3. **[follow.it](https://follow.it)** — free RSS-to-email, similar idea.

## Troubleshooting

- **Workflow fails on Actions tab:** open the failed run, read the red step. Most common cause: `package.json` or `deploy.yml` didn't upload.
- **Domain shows an old site:** DNS caching — wait up to 24 h, or test in a private window.
- **404 on a page you added:** check the file has the `---` front matter block and a `permalink` (pages) or lives in `src/posts/` (posts).
- **Site looks unstyled:** `src/css/style.css` missing or the browser cached an old version (hard refresh: Ctrl/Cmd-Shift-R).
