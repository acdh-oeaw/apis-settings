"""
Django settings for apis project.

Generated by 'django-admin startproject' using Django 1.11.x
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__,'../'))))

#BASE_URI is used to generate uris for locally created objects
BASE_URI = 'https://test.at'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd3j@zlckxkw73c3*ud2-11$)d6i)^my(60*o1psh*&-u35#ayi'

# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dal',
    'dal_select2',
    'gm2m',
    'rest_framework',
    'django_extensions',
    'django_filters',
    'django_tables2',
    'reversion',
    'reversion_compare',
    'crispy_forms',
    'webpage',
    'labels',
    'entities',
    'vocabularies',
    'relations',
    'metainfo',
    #'apis_highlighter',
    'rest_framework.authtoken',
    'guardian',
    #'registration', activate this for a registration form
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'PAGE_SIZE': 50,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'entities.custom_authentication.TokenAuthSupportQueryString'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    )
}

#SPHINXDOC_BASE_TEMPLATE = 'webpage/base.html'

SPAGHETTI_SAUCE = {
    'apps': ['entities', 'relations', 'vocabularies', 'metainfo'],
    'show_fields': False,
    'exclude': {'auth': ['user']}
}

ADD_REVERSION_ADMIN = True

REGISTRATION_OPEN = False

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware'
]

CRISPY_TEMPLATE_PACK = "bootstrap3"

ROOT_URLCONF = 'apis.urls'

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
                'apis.context_processors.custom_context_processors.add_entities',
                'apis.context_processors.custom_context_processors.add_apis_settings',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)


WSGI_APPLICATION = 'apis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'de-at'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_dir/')

MEDIA_URL = '/downloads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'downloads/')

APIS_COMPONENTS = ['deep learning', 'annotator agreement']
# APIS settings

APIS_ALTERNATE_NAMES = ['Taufname', 'Ehename', 'Name laut ÖBL XML', 'alternative Namensform', 'alternative name',
                   'Künstlername', 'Mädchenname', 'Pseudonym', 'weitere Namensform']

APIS_ENTITIES = {
    'Place': {'search': ['name'],
              'list_filters': [('name', {'method': 'wildcard_filter', 'label': 'Name'})]},
    'Person': {'search': ['name', 'first_name'],
               'form_order': ['first_name', 'name'],
               'table_fields': ['name', 'first_name', 'start_date', 'end_date', 'profession'],
               'list_filters': [('name', {'method': 'name_label_filter', 'label': 'Name complete'}),
                                ('first_name', {'method': 'wildcard_filter', 'label': 'Firstname'}),
                                ('gender', {'label': 'Gender'}),
                                ('start_date', {'label': 'Date of Birth'}),
                                ('end_date', {'label': 'Date of Death'}),
                                ('profession', {'label': 'Profession'}),
                                ('collection', {'label': 'Collection'})]
               },
    'Institution': {'search': ['name'],
                    'list_filters': [('name', {'method': 'wildcard_filter', 'label': 'Name'})]},
    'Work': {'search': ['name'],
             'list_filters': [('name', {'method': 'wildcard_filter', 'label': 'Name'})]},
    'Event': {'search': ['name'],
              'list_filters': [('name', {'method': 'wildcard_filter', 'label': 'Name'})]},
}
