# Migrating your content from WordPress

> **Status (2026-07-08):** Already migrated directly from the live site: the About, Publications, Conferences, and CV pages, plus the 4 most recent blog posts (with their original URLs preserved). **Still to do:** (1) the ~46 older blog posts — use the XML export below; (2) images — the migrated posts currently load images from the old WordPress URLs, which will break when you cancel. Download them (Step 2 does this automatically) into `src/assets/` and update the image links before cancelling; (3) your photo, `cv.pdf`, and credential PDFs into `src/assets/`.


Goal: get every blog post, page, and image out of WordPress and into this site's format (one Markdown file per post) before you cancel the plan.

## Step 1 — Export from WordPress (5 minutes)

1. Log in to your WordPress dashboard.
2. **Tools → Export → All content → Download Export File.**
   You get an `.xml` file containing every post and page. **Keep this file forever** — it's your permanent backup even after WordPress is gone.
3. Also export your **media library**: on WordPress.com, **Tools → Export → Export media library** gives you a zip of all uploaded images and PDFs. (If that option is missing on your plan, see Step 3 for an alternative.)
4. If you have blog subscribers: **Jetpack → Newsletter → Subscribers → Download as CSV.** You'll want this for Buttondown/follow.it (see README).

## Step 2 — Convert posts to Markdown (10 minutes, automated)

On any computer with [Node.js](https://nodejs.org) installed, run:

```bash
npx wordpress-export-to-markdown
```

It asks a few questions interactively. Answer:

- **Path to export file:** point it at the `.xml` you downloaded
- **Output folder:** anything, e.g. `wp-output`
- **Create year folders / month folders:** No and No
- **Create a folder for each post:** No
- **Prefix post folders/files with date:** **Yes** ← important, matches this site's naming
- **Save images attached to posts / scraped from content:** Yes and Yes (it downloads them for you)

Result: a folder of files like `2025-03-14-my-post.md`, each with front matter already in place, plus an `images` folder.

## Step 3 — Drop the files into this site

1. Copy all the converted `.md` files into `src/posts/`.
2. Copy the downloaded images into `src/assets/`.
3. Open a couple of posts and fix image paths: the converter writes paths like `images/foo.jpg` — change them to `/assets/foo.jpg`. A find-and-replace across the files (`images/` → `/assets/`) handles most of it.
4. The converter's front matter uses `date: "2025-03-14"` and `title:` — that's already compatible. If a post has `categories:` or `tags:` from WordPress, rename that key to `postTags:` if you want the labels displayed (or just delete it).
5. Commit/upload everything to GitHub. Done — the blog index, homepage list, and RSS feed regenerate automatically.

*Alternative if the media export was unavailable:* the converter in Step 2 scrapes images directly from your live site as long as WordPress is still online — so run it **before** cancelling.

## Step 4 — Preserve your URLs (recommended for SEO)

Your WordPress posts most likely live at `jonhlynsson.com/some-post-slug/` while this site puts posts at `/blog/some-post-slug/`. Two options:

- **Keep old URLs exactly:** add a `permalink` line to any migrated post's front matter, e.g. `permalink: /some-post-slug/`. The converter's file slug tells you the original slug.
- **Or accept the new structure:** old links will hit the 404 page, which points visitors to the blog index. Fine if your posts don't have many inbound links.

To check what the original URL of a post was, open the post on your live WordPress site before cancelling and note the address.

## Step 5 — Pages, CV, and PDFs

- The static pages (About, Publications, Conferences, Teaching, CV) are already scaffolded in `src/` — paste your current text into them rather than converting. It's faster and cleaner than migrating Elementor markup.
- Download any PDFs currently hosted on WordPress (e.g. your psychologist licence PDF, `cv.pdf`, conference slides) from `jonhlynsson.com/wp-content/uploads/...` and put them in `src/assets/`, then link to them as `/assets/filename.pdf`.

## Step 6 — Final check before cancelling WordPress

- [ ] Every post appears at `/blog/` on the new site
- [ ] Images load inside posts
- [ ] CV PDF and licence PDF downloaded and re-linked
- [ ] Subscriber CSV exported (if applicable)
- [ ] The `.xml` export saved somewhere safe (cloud + local)
- [ ] Domain transferred away from WordPress.com **if it was registered there** (do this first — takes up to 5 days)

Then cancel the WordPress plan and the Elementor subscription.
