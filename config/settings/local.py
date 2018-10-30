from .base import *
import environ

root = environ.Path(__file__) - 3
env_file = str(root.path('.env'))
env = environ.Env()
env.read_env(env_file)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ['127.0.0.1', 'localhost']


def custom_show_toolbar(request):
    return True


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.logging.LoggingPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES': True,
}

# LOGGING = {
#     'version': 1,
#     'formatters': {
#         'django.server': {
#             '()': 'django.utils.log.ServerFormatter',
#             'format': '[%(asctime)s] %(message)s a',
#         },
#         'default': {
#             'format': '[%(asctime)s] %(levelname)s %(module)s '
#                       '%(process)d %(thread)d %(message)s'
#         },
#     },
#     'handlers': {
#         'debug': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, "log", 'exam.log'),
#             'when': 'D',
#             'interval': 1,
#             'formatter': 'default',
#         },
#     },
#     'loggers': {
#         'exam': {
#             'handlers': ['debug'],
#             'level': 'DEBUG',
#             'propagate': True,
#         }
#     }
# }
