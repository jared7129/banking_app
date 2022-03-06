# banking_app

## Here are the instructions to setup the app

1. Django start project

Make sure you have the folowing installed:

- Python 3
- Pip 3
- Virtualenv
- Django == 3.2.9

## Django Installation

* Make directory in your workspace:
  `mkdir banksystem_project`

* Navigate into `banksystem_project`

  `cd banksystem_project`

* Create a python virtual environment to install django and other dependecies in the future.

  `virtualenv .env`

  `.env` is the directory where we install the packages.

* Activate the virtual environment.

  `source .env/bin/activate`

* Install Django framework. We are going to use `django==3.2.9` in this tutorial.

  `pip3 install django==3.2.9`

OR 

  `pip install django==3.2.9` 

* Create django project:
  
  `django-admin startproject banksystem`


2. Create api app

Run the following command in your root folder where `manage.py` lives.

`./manage.py startapp api`


Include `api` application in django `settings.py`

```
  INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'api',
]

```

3. Install Django rest-framework

Install using `pip` ...

```
pip install djangorestframework====3.12.4
pip install Markdown==3.3.6     
pip install django-filter==21.1 
```

4. Add `'rest_framework'` to your `INSTALLED_APPS` setting in `settings.py`.

```
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```
Add the following to your root`urls.py` file. Location of **urls.py** `banksystem_project/banksystem/urls.py` 

```
urlpatterns = [
    ...
    url(r'^api-auth/', include('rest_framework.urls'))
]
```

