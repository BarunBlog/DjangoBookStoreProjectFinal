"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import environ

import dj_database_url

import django_heroku



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


env = environ.Env(
    # set casting, defalut value
    DEBUG=(bool, False)
)

'''env_file = os.path.join(BASE_DIR, ".env")

# reading .env file
environ.Env.read_env(env_file)'''

# False if not in os.environ
DEBUG = env('DEBUG', default=False)


ENVIRONMENT = env('ENVIRONMENT', default='development')


# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ, So provided default value
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ALLOWED_HOSTS = ['bookstore-for-bookworms.herokuapp.com/', 'localhost', '127.0.0.1'] # Want it to run in heroku and also in localhost


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites', # adding sites framework for controling multiple sites.

    # Third-party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'debug_toolbar',

    # Local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
    'orders.apps.OrdersConfig',
]


# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4' # need to specify the CSS framework you want to use in your forms.

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware', # to add per-site caching
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Tying into middleware allows each panel to be instantiated on request and rendering to happen on response.
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', # to add per-site caching
]

ROOT_URLCONF = 'bookstore_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'bookstore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
    
}


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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# defines the location of static files in local development
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),] 

# location of static files for production 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# It is implicitly set for us and although this is an optional step, I prefer to make it explicit in all projects.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

AUTH_USER_MODEL = 'users.CustomUser' #will cause our project to use CustomUser instead of the default User model.

# django-allauth config
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'


# django-allauth config
SITE_ID = 1 # Since we have only one site

#  which is used when Django attempts to authenticate a user.
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#ACCOUNT_SESSION_REMEMBER = True 
# It will remember users session so that they don't have to log in again, and remember box will removed here   

#ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # to only ask for a password once.

# Email Only Login & Signup
'''ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True'''


DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com'


EMAIL_HOST = env('EMAIL_HOST', default='example.gmail.com')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='example@gmail.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='example')



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Stripe
STRIPE_TEST_PUBLISHABLE_KEY=env('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY=env('STRIPE_TEST_SECRET_KEY')

# Django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)


# set three additional fields to add per-site caching
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 # number of seconds to cache a page. After the period is up, the cache expires and becomes empty.
CACHE_MIDDLEWARE_KEY_PREFIX = ''



if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True # To help guard against XSS attacks

    X_FRAME_OPTIONS = 'DENY' # browser will block the resource from loading in a frame no matter which site made the request.

    SECURE_SSL_REDIRECT = True # force all non-HTTPS traffic to be redirected to HTTPS
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # otherwise your site may still be vulnerable via an insecure connection to a subdomain.
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True # to avoid transmitting the cookie over HTTP accidentally.

    SECURE_REFERRER_POLICY = 'same-origin' # This allows CSRF and internal analytics to work without leaking Referer values to other domains


    db_from_env = dj_database_url.config(conn_max_age=500) # Returns configured DATABASE dictionary from DATABASE_URL
    DATABASES['default'].update(db_from_env)


    # https://devcenter.heroku.com/articles/django-app-configuration
    # Activate Django-Heroku.
    django_heroku.settings(locals())