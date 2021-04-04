from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']

OPENWEATHER_API_KEY = 'f326d3a2c421673e69fe5c64527a5357'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'deviare',
        'PASSWORD': 'THISISNOT A VALID A PASSWORD',
        'PORT': '',
        'USER': 'django'
    }
}