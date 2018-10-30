from .base import *
import os
import boto3

# 設定値リスト
keys = [
    "DEBUG",
]

# 検証環境であれば検証環境の値を使用する
if os.environ["environment"] == "dev":
    keys = ["DEV_" + key for key in keys]


# AWS System Manager パラメータストアから本番環境用設定値を取得する
def get_params():
    response = boto3.client("ssm", region_name="ap-northeast-1").get_parameters(
        Names=keys,
        WithDecryption=True
    )

    return {param["Name"]: param["Value"] for param in response["Parameters"]}


# パラメータストアから取得した値をグローバル変数に代入しSettingsから参照できるようにする
parameters = get_params()
for key in keys:
    exec("{0}='{1}'".format(key, parameters[key]))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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
#         'info': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, "log", 'exam.log'),
#             'when': 'D',
#             'interval': 1,
#             'formatter': 'default',
#         },
#     },
#     'loggers': {
#         'exam': {
#             'handlers': ['info'],
#             'level': 'INFO',
#             'propagate': True,
#         }
#     }
# }


