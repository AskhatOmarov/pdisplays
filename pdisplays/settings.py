"""
Django settings for pdisplays project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from configurations import Configuration
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def rel(*x):
    return os.path.join(BASE_DIR, *x)


class BaseConfiguration(Configuration):
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'i-++#kh!%4a2p)&3s9^f!ed62b_zd7gvu0pgp3kl)*h61&#be^'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'tastypie',
        'tastypie_swagger',
        'bootstrap3',
        'form_utils',
        'widget_tweaks',
        'geoposition',
        'pdisplays',
        'users',
    )

    TASTYPIE_SWAGGER_API_MODULE = 'pdisplays.urls.v1_api'

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'pdisplays.urls'

    WSGI_APPLICATION = 'pdisplays.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'heroku_31a7e683faba4b1',
            'USER': 'b44ba429f7e32e',
            'PASSWORD': '3ae77e10',
            'HOST': 'us-cdbr-iron-east-02.cleardb.net',
            'PORT': '',
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    TEMPLATE_DIRS = (
        rel('templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    MEDIA_ROOT = rel('..', 'media')
    MEDIA_URL = '/media/'

    STATIC_URL = '/static/'
    STATIC_ROOT = rel('..', 'static')
    STATICFILES_DIRS = (
        rel('static'),
    )
    LOCALE_PATHS = (
        rel('locale'),
    )
    # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

    AWS_ACCESS_KEY_ID = 'AKIAJJW6HILACLZYNQ7Q'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'pdisplays'

    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    TASTYPIE_DEFAULT_FORMATS = ['json']

class DevConfiguration(BaseConfiguration):
    pass