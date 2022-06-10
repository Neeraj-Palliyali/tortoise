from datetime import timedelta

DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'tortoise',
            'USER': 'postgres',
            'PASSWORD': 'ironman789',
            'HOST': 'localhost',
            'PORT': '5432',
       }
   }

ALLOWED_HOSTS = ["127.0.0.1",]

SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
    'ROTATE_REFRESH_TOKENS': True,
}