# SweetSupply

A confectionary store web application built with Django and Bulma CSS. Users can browse products, register/login, and submit contact enquiries.

## Features

- Product catalogue with Indian sweets and gift hampers
- User registration, login, and profile pages
- Contact/enquiry form with database storage
- Responsive UI using Bulma CSS
- Django admin panel for managing products and enquiries

## Tech Stack

- **Backend:** Python 3, Django 4.1
- **Frontend:** Bulma CSS, Django Templates
- **Database:** SQLite
- **Forms:** django-crispy-forms with crispy-bulma

## Screenshots

> _Add screenshots here_

## Getting Started

```bash
# Clone the repo
git clone https://github.com/GagandeepSM/Urban-Cloth.git
cd Urban-Cloth

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

## Project Structure

```
SweetSupply/
├── SweetSupply/       # Project config (settings, urls, wsgi)
├── sweets/            # Main app — views, models, templates
│   └── templates/sweets/
│       ├── base.html
│       ├── sweets.html    # Homepage
│       ├── products.html  # Product catalogue
│       └── contact.html   # Contact form
├── users/             # Auth app — register, login, profile
├── manage.py
└── requirements.txt
```
