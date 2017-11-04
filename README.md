# Django - Product Display App v1.0

### This app displays a list of products with their images and descriptions, uploaded using a form.

##### The Product Display App is built using the following methods:

* Django template filters
* Django Forms and Model Forms
* Image Fields and image uploads
* User Authentication
* Django and AJAX to create a like button

##### The Product Display App uses the following packages:

* dj-database-url
* Django
* django-widget-tweaks
* olefile
* Pillow
* python-decouple

All pages where a user name is used will first look for first name and last name.  If those don't exist it will default to username.

You will need to create a .env file and add your secret key and database settings to it.  Take a look at the env.example file for examples of formatting.  Here's an idea of a basic .evn file:

```
SECRET_KEY = 'randomsetofnumberslettersandcharactersetc'
DEBUG=True
ALLOWED_HOSTS=.localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

To Install first create an virtual environment to work in.

```django
python3 -m venv myvenv
```
Activate the virtual environment
```django
source myvenv/bin/activate
```

Install all dependencies

```django
pip install -r requirements.txt
```

Create a superuser

```django
python manage.py createsuperuser
```

To Do:
* Create a dropdown menu to select user to view
* Rebuild user account functionality with more robust code
