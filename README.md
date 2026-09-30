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

- **Projects** – add/edit from the admin. Each project has a title, slug
  (auto-filled), description, link, order, and a published toggle.
  Upload a thumbnail, or leave it empty to fall back to a bundled
  `static_image` path.
- **Skills** – the icons shown in the "Primary Skills on" strip. Upload an
  icon or keep the static fallback.

## Project layout

```
config/        Django project (settings, urls)
portfolio/     App: models, admin, views, migrations
templates/     index.html (rendered view)
static/        assets/ and images/ moved here
media/         Admin uploads (gitignored)
```
