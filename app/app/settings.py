import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'test')
DEBUG = True #bool(int(os.environ.get('DEBUG', 0))) # 0: False
ALLOWED_HOSTS = ['*'] # ex) ec2-123-123-123


# Application definition

DJANGO_SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core'
]

CUSTOM_USER_APPS = [
    'users.apps.UsersConfig',
    'comments.apps.CommentsConfig',
    'reactions.apps.ReactionsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'videos.apps.VideosConfig',
    'drf_spectacular',
    'rest_framework',
    'channels',
]

INSTALLED_APPS = CUSTOM_USER_APPS + DJANGO_SYSTEM_APPS

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'
# WSGI 애플리케이션 개체의 전체 Python 경로를 지정
ASGI_APPLICATION = 'app.routes.application'
# ASGI 애플리케이션 객체의 전체 Python 경로를 지정
# 'application': 파일 내에 정의된 WSGI or ASGI 애플리케이션 호출 가능 항목입니다


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}
# "BACKEND": 채널이 이 레이어에 사용할 백엔드를 지정합니다.
# "channels.layers.InMemoryChannelLayer": 서버의 메모리에 데이터를 저장하는 인메모리 백엔드입니다.


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST':os.environ.get('DB_HOST'),
        'NAME':os.environ.get('DB_NAME'),
        'USER':os.environ.get('DB_USER'),
        'PASSWORD':os.environ.get('DB_PASS'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIR = [
    BASE_DIR / 'static',
]
MEDIA_URL = 'storage/'
MEDIA_ROOT = BASE_DIR / "storage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

# STATIC_URL = '/static/'
# MEDIA_URL = '/static/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
