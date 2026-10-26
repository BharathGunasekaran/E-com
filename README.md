E-com: E-Commerce Website
An online shopping platform that allows users to browse products, manage their shopping cart, and complete the checkout process.

Features
User login/signup

Product catalog

Shopping cart management

Checkout process

## 🔐 Environment variables

Secrets are read from environment variables instead of being stored in the code:

```bash
export DB_PASSWORD=your_mysql_password
export DJANGO_SECRET_KEY=your_django_secret_key   # optional for local development
```

## 🚀 Getting started

```bash
pip install -r requirements.txt pymysql
python manage.py migrate
python manage.py runserver
```
Create a MySQL database called `Ecom` first, then open http://127.0.0.1:8000.
