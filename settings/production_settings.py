from settings.common_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tweetdb',
        'USER': 'tweetdbadmin',
        'PASSWORD': 'tweetdb12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}

