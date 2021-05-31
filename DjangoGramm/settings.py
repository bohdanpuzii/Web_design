"""
Django settings for DjangoGramm project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRETKEY = os.getenv('SECRET_KEY')
SECRET_KEY = SECRETKEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mydjangogramm.herokuapp.com', '*']

# Application definition

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'DjangoGramm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect',  # <-- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoGramm.wsgi.application'

DB_NAME = os.getenv('DB_NAME')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')

# use this db for deploy
'''DATABASES = {'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': DB_NAME,
    'USER': DB_USER,
    'PORT': DB_PORT,
    'HOST': DB_HOST,
    'PASSWORD': DB_PASS
}
}'''

# use this db for localhost and running tests
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'djangogramm',
    'USER': 'postgres',
    'PORT': '5432',
    'HOST': 'localhost',
    'PASSWORD': 'mirinda123'
}
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGOUT_REDIRECT_URL = '/signin/'

CLOUD_NAME = os.getenv('CLOUD_NAME')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
LOGIN_URL = '/sign_in'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/feed'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '225024915875-iimb0er7vlrd4argm48jnoinh1l64015.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '2-i-sQbYT0ZYdkh4km38IYgS'

SOCIAL_AUTH_GITHUB_KEY = '63e8751879284ea92949'
SOCIAL_AUTH_GITHUB_SECRET = 'de1517e4104541f491e391b85642a3cdb94879fb'

AUTH_USER_MODEL = 'app.Profile'
