from db.config import psql

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': psql.name,
        'USER': psql.user,
        'PASSWORD': psql.password,
        'HOST': psql.host,
        'PORT': psql.port,
    }
}