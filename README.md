# blog-api

A blog's RESTful API...

## Getting Started

```bash
python -m virtualenv venv
./venv/Scripts/activate
pip install Django
mkdir src && cd src
django-admin startproject config .
python manage.py startapp posts
python manage.py migrate
python manage.py createsuperuser
pip install djangorestframework
pip install dj-rest-auth
pip install django-allauth
```