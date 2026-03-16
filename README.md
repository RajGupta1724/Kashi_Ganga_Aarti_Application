# Kashi Ganga — Divine Aarti & Spiritual Event Services

A Django web application for booking sacred Ganga Aarti ceremonies in Varanasi.

---

## Project Structure

```
Kashi_Ganga/
├── kashi_ganga/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                 # Main Django app
│   ├── models.py         # Booking, Testimonial, GalleryImage models
│   ├── views.py          # Page views
│   ├── urls.py           # URL patterns
│   ├── forms.py          # BookingForm
│   ├── admin.py          # Admin panel config
│   └── migrations/
├── templates/            # HTML templates
│   ├── base.html         # Base layout (nav, footer, WhatsApp FAB)
│   ├── index.html        # Main landing page (hero, services, gallery, map)
│   ├── home.html         # Backward-compatible template (legacy)
│   ├── services.html     # Services detail page
│   ├── gallery.html      # Gallery with lightbox
│   ├── about.html        # About us page
│   ├── booking.html      # Booking form
│   └── booking_success.html
├── static/
│   ├── css/style.css     # All styles (saffron/golden theme)
│   ├── js/main.js        # Interactivity (scroll, lightbox, counters)
│   └── images/           # ← Place hero-aarti.jpg here
├── media/                # User-uploaded files (gallery, testimonials)
├── manage.py
├── requirements.txt
└── .env.example
```

---

## Quick Setup

### 1. Prerequisites
- Python 3.10+
- (Optional) PostgreSQL, if you want PostgreSQL instead of SQLite
- (Optional) Git

### 2. Open the project
```bash
cd d:\Kashi_Ganga
```

### 3. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up environment variables
```bash
copy .env.example .env
```
Edit `.env` and fill in:
- `SECRET_KEY` — generate one at https://djecrety.ir/
- `DB_NAME`, `DB_USER`, `DB_PASSWORD` — only if using PostgreSQL

If `DB_NAME` is not set, the project uses SQLite automatically (`db.sqlite3`).

### 6. (Optional) Create PostgreSQL database
```sql
-- In psql or pgAdmin:
CREATE DATABASE kashi_ganga_db;
```

### 7. Place the hero image
Save your Ganga Aarti ceremony image as:
```
static/images/hero-aarti.jpg
```
This is the image used as the hero section background (matching the screenshot).

### 8. Run migrations
```bash
python manage.py migrate
```

### 9. Create admin superuser
```bash
python manage.py createsuperuser
```
Enter a username, email, and password when prompted.

### 10. Collect static files (for production)
```bash
python manage.py collectstatic
```

### 11. Start the development server
```bash
python manage.py runserver
```

Open your browser at: **http://127.0.0.1:8000/**

---

## Admin Panel

Access at: **http://127.0.0.1:8000/admin/**

Log in with the superuser credentials you created. You can:
- View and manage all **Booking Inquiries** (with status: Pending / Confirmed / Completed / Cancelled)
- Add **Testimonials** (shown on home page)
- Upload **Gallery Images** (categorized, with ordering)
- Use bulk actions to confirm/complete/cancel bookings

---

## Page Overview

| URL             | Page            | Description                                  |
|-----------------|-----------------|----------------------------------------------|
| `/`             | Index           | Hero, services preview, gallery, testimonials, map |
| `/services/`    | Services        | All services with detailed descriptions       |
| `/gallery/`     | Gallery         | Photo gallery with filter + lightbox          |
| `/about/`       | About Us        | Team, mission, Varanasi heritage              |
| `/booking/`     | Book Now        | Booking inquiry form                          |
| `/booking/success/` | Success     | Confirmation page after form submission       |
| `/admin/`       | Admin Panel     | Manage bookings, gallery, testimonials        |

---

## WhatsApp Integration

Update the WhatsApp number in `.env`:
```
WHATSAPP_NUMBER=919235054005
```
(Country code + number, no `+` sign or spaces)

The floating WhatsApp button appears on every page with a pre-filled booking inquiry message.

---

## Google Maps

The home page already embeds **Dashashwamedh Ghat, Varanasi** via Google Maps iframe.
To use the Maps JavaScript API (for advanced features), add your key in `.env`:
```
GOOGLE_MAPS_API_KEY=your_key_here
```

---

## Color Theme

| Variable         | Color       | Usage                         |
|------------------|-------------|-------------------------------|
| `--primary`      | `#e65c00`   | Buttons, accents, links       |
| `--secondary`    | `#f9b733`   | Golden highlights, "Spiritual"|
| `--dark`         | `#1a0800`   | Navbar, footer background     |
| Hero overlay     | warm amber  | Semi-transparent image overlay|

---

## Production Deployment

For production:
1. Set `DEBUG=False` in `.env`
2. Set `SECRET_KEY` to a strong random value
3. Set `ALLOWED_HOSTS` to your domain
4. Run `python manage.py collectstatic`
5. Use Gunicorn + Nginx (or any WSGI server)

---

## Deploy On Render

This repository is ready for Render deployment using the included `render.yaml`.

### Option A: One-click Blueprint Deploy (recommended)
1. Push latest code to GitHub.
2. In Render dashboard, click `New` -> `Blueprint`.
3. Select this repository.
4. Render will detect `render.yaml` and create:
	- Web service: `kashi-ganga-aarti-app`
	- PostgreSQL database: `kashi-ganga-db`
5. Click `Apply` to deploy.

### Option B: Manual Web Service
1. Create a new `Web Service` in Render from this repo.
2. Use:
	- Build Command:
	  `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
	- Start Command:
	  `gunicorn kashi_ganga.wsgi:application`
3. Add environment variables:
	- `DEBUG=False`
	- `SECRET_KEY=<secure-random-string>`
	- `ALLOWED_HOSTS=<your-render-domain>`
	- `WHATSAPP_NUMBER=919235054005`
	- `DATABASE_URL=<render-postgres-connection-string>`

### After First Deploy
1. Open service shell and run:
	`python manage.py createsuperuser`
2. Log in at `/admin/`.

---

## GitHub Push Checklist

Before pushing to GitHub:
- Ensure `.env` is not committed (it is ignored by `.gitignore`)
- Ensure `venv/`, `media/`, `staticfiles/`, and `db.sqlite3` are not committed
- Keep `.env.example` committed with placeholder values

---

## Optional Enhancements

- **Online Payments**: Integrate Razorpay or PayPal for advance booking
- **SMS Notifications**: Use Twilio to auto-notify admin on new bookings
- **Email Confirmation**: Configure Django's email backend to send confirmation emails
- **Hindi Language**: Django's i18n framework supports multi-language
- **Blog**: Add a `Blog` model and template for SEO content about Ganga Aarti traditions

---

*Built with Django · PostgreSQL · Bootstrap 5 · Saffron & Gold Theme*
