
"""
Django settings for _main project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k+1xh&^ueh1^pls5+b2%pdhl*meed_7b=7scycdrh985hcwrr5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['humraahi.herokuapp.com' ,'127.0.0.1','http://127.0.0.1:8000','0.0.0.0','localhost']

# 640857218379-3qjvelmqgnpvd8k4k868s66mtrrbr2u8.apps.googleusercontent.com


# Application definition

INSTALLED_APPS = [
    'channels',
    'channels_redis' ,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


     'Humrahi',
     'user',
     'chatService',
     'Notifications',
    
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken', 
    'social_django',
    'rest_social_auth',

    'oauth2_provider', 





    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',


    'whitenoise.runserver_nostatic'
    # 'rest_framework_social_oauth2',
    

   
]

#keys
SOCIAL_AUTH_RAISE_EXCEPTIONS = True

SOCIAL_AUTH_GITHUB_KEY='ba6fbdc2d5def8fd295a'
SOCIAL_AUTH_GITHUB_SECRET='031ee224412d0b357eb83d57c1f757bf948a4b51'
SOCIAL_AUTH_FACEBOOK_KEY='203842777356572'
SOCIAL_AUTH_FACEBOOK_SECRET='5f93dd0a6793a9fab24a011ad1fc7ebf'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='252174418134-a7f85qr6iim7tg8be64st5vak0n0gjk4.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='cl13j9uRPzTR4t_LKaU9BbRO'


SOCIAL_AUTH_URL_NAMESPACE = '/'


#cors

CSRF_COOKIE_SECURE = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
DRFSO2_URL_NAMESPACE = 'social'
SOCIAL_AUTH_REDIRECT_IS_HTTPS= True


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
   
    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
  
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Cabsharing.urls'



# template serttings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'build')],
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


# this is wsgi application for our main appservice 

WSGI_APPLICATION = 'Cabsharing.wsgi.application'



# mysite/settings.py
# Channels
ASGI_APPLICATION = 'Cabsharing.routing.application'
CHANNEL_LAYERS = {
    'default': {

        # the chat messages will stored in the redis server 
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
               #localhost,port
        },
    },
}
REDIS_HOST = 'localhost'
REDIS_PORT = 6379





SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD ='username'
ACCOUNT_EMAIL_REQUIRED =False
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_EMAIL_VERIFICATION = 'none'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# setting my backend as postgres

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cabsharing',
        'USER' : 'djtvozkterzhhl' ,
        'PASSWORD': '2b6b464e18876bb123417b2108ffd82bfac9741fb8d4c8d09eb76da06d8aa478' ,
        # 'TEST': {
        #     'NAME': 'chattests'
        # },
        'HOST':'localhost'
    }
}


db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

 




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

AUTH_USER_MODEL='Humrahi.User'
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'build/static')
]
STATIC_ROOT =os.path.join(BASE_DIR,'assets')
#MEDIA  FILES 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,'media')



REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
    #     # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.TokenAuthentication',
         'rest_framework.authentication.SessionAuthentication',
         'rest_framework.authentication.BasicAuthentication'
        #  'rest_framework_social_oauth2.authentication.SocialAuthentication '
    )
}




