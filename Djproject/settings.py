"""
Django settings for Djproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import pymongo
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'myapp/html_templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ijk@3)*123456789ijhkdkhdgsta&*()$>/k12309545%fFsop' #i+ypsvjxaifwh26&e#@l=_t5x)155&rse7)hno7cry$m&#vpht

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #added by lijin for deploying in server

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#DBNAME = "restaurants"

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware','corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
'x-requested-with',
'content-type',
'accept',
'origin',
'authorization',
'X-CSRFToken',
'Access-Control-Allow-Origin',
'Access-Control-Allow-Headers',
'Access-Control-Allow-Methods'
)


ROOT_URLCONF = 'Djproject.urls'

WSGI_APPLICATION = 'Djproject.wsgi.application'


# MONGO_SERVER_ADDR = 'localhost' #Mongodb address 
# MONGO_SERVER_ADDR = '117.240.93.254' #Mongodb address outside
MONGO_SERVER_ADDR = '192.168.2.20' #Mongodb address
MONGO_PORT = 27017 #Mongodb port

MONGO_DB = 'baabtra_db'  #Database name

FILEUPLOAD_PATH="uploaded" #path for uploading the files
RESUME_PATH='http://localhost:8000/files/resume/' #path for mailing the resume link
LOGO_PATH='http://localhost:8000/files/companyLogo/' #path for mailing the resume link
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testbaabtra@gmail.com'
EMAIL_HOST_PASSWORD = 'baabtra_test'
EMAIL_PORT = 587

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = 'http://localhost:8000/static/'

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PERMISSION_CLASSES':(
    'rest_framework.permissions.AllowAny',
    )
    
}

# USE_X_FORWARDED_HOST This should only be enabled if a proxy which sets this header is in useself.
USE_X_FORWARDED_HOST = True
# HTTP_X_FORWARDED_FOR = True

# FORWARDED_FOR_FIELDS = (
# 'HTTP_X_FORWARDED_FOR',
# 'HTTP_X_FORWARDED_HOST',
# 'HTTP_X_FORWARDED_SERVER',        
# )

#LOGGING_CONFIG = None #added by Lijin for server seting up purpose
#LOGGING = {'django.security.DisallowedHost': {
#        'handlers': ['mail_admins'],
#        'level': 'CRITICAL',
#        'propagate': False,
#    }}  # whatever you want, as you already have

#import logging.config
#logging.config.dictConfig(LOGGING)
 