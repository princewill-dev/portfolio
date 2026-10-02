# Portfolio

Personal portfolio site for Chibuike Princewill Ezekude, powered by Django.
Projects and skills are managed from the Django admin and rendered on the
landing page. The original static design is preserved.

## Stack

- Django 6
- PostgreSQL (production) / SQLite (local default)
- Pillow for image uploads

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env        # then edit SECRET_KEY / database values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then visit:

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

No database variables set means Django uses the local `db.sqlite3` file.

## Switching to PostgreSQL

Set `DATABASE_URL` in `.env` (preferred):

```
DATABASE_URL=postgres://USER:PASSWORD@HOST:5432/DBNAME
```

or the individual variables (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`,
`DB_PORT`). Then run `python manage.py migrate` against the new database.

## Seeding the original projects

The original projects and skills are seeded automatically by the
`portfolio.0002_seed_content` migration. To (re)seed them on demand — safe to
run repeatedly, it updates existing rows rather than duplicating:

```bash
python manage.py seed_projects          # create/update the 7 projects + 9 skills
python manage.py seed_projects --flush  # wipe Projects/Skills first, then seed
```

Run this in an environment where the database host resolves (e.g. inside the
Docker platform that hosts your Postgres).

## Managing content

- **Site Content** – a single editable row for the homepage hero: greeting,
  headline (tagline), description (rich text — bold/links/lists), contact
  heading, email, profile photo, social links, and footer text. The admin
  opens straight into the editor and cannot add/delete rows.
- **CV / Resume** – upload a PDF, DOC or DOCX (max 10 MB) under *Site
  Content → CV / Resume*. Uploading a new file replaces the current one (the
  old file is deleted). The **My Resume** button is hidden on the site until a
  file is present; PDFs open inline, Word documents download.
- **Projects** – add/edit from the admin. Each project has a title, slug
  (auto-filled), a **brief description** (shown on the home page card), and
  **full details** (rich text, shown on the project's own page). Also: link,
  order, and a published toggle. Upload a thumbnail, or leave it empty to fall
  back to a bundled `static_image` path. Clicking a card opens
  `/project/<slug>/`; unpublished projects return 404.
- **Skills** – the icons shown in the "Primary Skills on" strip. Upload an
  icon or keep the static fallback.

The rich-text description uses TinyMCE loaded from a CDN (no extra Python
package), wired up by `static/assets/js/admin/tinymce-init.js`.

## Project layout

```
config/        Django project (settings, urls)
portfolio/     App: models, admin, views, migrations
templates/     index.html + project_detail.html (rendered views)
static/        assets/ and images/ moved here
media/         Admin uploads (gitignored)
```
