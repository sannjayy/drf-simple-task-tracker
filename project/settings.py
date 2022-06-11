from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import os, datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(find_dotenv())


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

ENV_NAME = os.environ.get("ENV_NAME")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG_VALUE'] == 'True'

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(',') 


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework', 
    'drf_yasg',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
]
LOCAL_APPS = [
    'app_accounts',
    'app_task_tracker',
]


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'app_accounts.backends.EmailORUsernameLoginBackend',
)

AUTH_USER_MODEL = 'app_accounts.User'
ROOT_URLCONF = 'project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database

# DATABASE CONFIG
ENABLE_DB = (os.environ.get('ENABLE_DB') == 'True')
if ENABLE_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# SMTP CONFIG
ENABLE_SMTP = (os.environ.get('ENABLE_SMTP') == 'True')
if ENABLE_SMTP:
    EMAIL_USE_TLS = (os.environ.get('EMAIL_USE_TLS', True) == 'True')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587)) # 587/465
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL') # Your Name <info@example.com>
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Password validation

# AUTH_PASSWORD_VALIDATORS = [
#     { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
#     { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
#     { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
#     { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
# ]


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / "static/staticfiles"
STATICFILES_DIRS = [ BASE_DIR / 'static']


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URL CONFIG
LOGIN_URL = '/admin/'
LOGOUT_URL = '/admin/logout/'

# CORS
CORS_ALLOW_ALL_ORIGINS = True # Dev Purpose Only


# DJANGO REST FRAMEWORK CONFIG
REST_FRAMEWORK = {
    # Common
    "NON_FIELD_ERRORS_KEY": "error",

    # Throttle
    "DEFAULT_THROTTLE_RATES": {
        'anon': '10/hour',
        'user': '50/hour',
    },

    'SEARCH_PARAM': 'q',

    # Auth 
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT SETTINGS
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ('Bearer', ),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

# SWAGGER SETTINGS
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer':{
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    }
}

# CELERY SETTING

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
# 
# celery -A config worker -l info -P eventlet
