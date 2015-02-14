# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#to build path for templates, static etc.,
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kphzax-xe7$iq%gs2s@8vghr%1_(_=kc+t^9vdakab8hm^zzd5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DOMAIN = 'localhost:8000'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CONTACT_EMAIL="affenity@gmail.com"


STATIC_ROOT = location('static')

MEDIA_ROOT = location('media')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'affenity.ramkin@gmail.com'
EMAIL_HOST_PASSWORD = '8lm6xpHiFd8RJjUYWpxG'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'affenity.ramkin@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'