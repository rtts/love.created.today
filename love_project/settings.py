import os
try:
    from .secret import SECRET_KEY
except ImportError:
    raise ImproperlyConfigured("Error retrieving SECRET_KEY")
try:
    from .debug import DEBUG
except ImportError:
    DEBUG = False

BASE_DIR         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS    = ['localhost', 'love_project.created.today']
ROOT_URLCONF     = 'love_project.urls'
WSGI_APPLICATION = 'love_project.wsgi.application'
LANGUAGE_CODE    = 'en-us'
TIME_ZONE        = 'UTC'
USE_I18N         = True
USE_L10N         = True
USE_TZ           = True
STATIC_URL       = '/static/'
MEDIA_URL        = '/media/'
AUTH_USER_MODEL  = 'love_engine.Bachelor'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'love_engine',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)
    try:
        import livereload.middleware
        MIDDLEWARE_CLASSES += ('livereload.middleware.LiveReloadScript',)
    except ImportError:
        pass

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'syslog': {
         'level': 'INFO',
         'class': 'logging.handlers.SysLogHandler',
         'facility': 'local7',
         'address': '/dev/log',
       },
    },
    'loggers': {
        'django':{
            'handlers': ['syslog'],
            'level': 'INFO',
            'disabled': False
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ('/tmp/love_project.sqlite3'),
    }
}
