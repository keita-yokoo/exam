from .base import *
import os
import boto3

# 設定値リスト
keys = [
    "DEBUG",
]

# 辞書構造の設置値リスト
dict_keys = [
    "DB_ENGINE",
    "DB_NAME",
    "DB_HOST",
    "DB_USER",
    "DB_PASSWORD"
]

# 検証環境か
is_dev = os.environ.get("environment", "dev") == "dev"

# 検証環境であれば検証環境の値を使用する
if is_dev:
    keys = ["DEV_" + key for key in keys]
    dict_keys = ["DEV_" + dict_key for dict_key in dict_keys]


# AWS System Manager パラメータストアから本番環境用設定値を取得する
def get_params():
    response = boto3.client("ssm", region_name="ap-northeast-1").get_parameters(
        Names=keys+dict_keys,
        WithDecryption=True
    )

    return {param["Name"]: param["Value"] for param in response["Parameters"]}


# パラメータストアから取得した値をグローバル変数に代入しSettingsから参照できるようにする
parameters = get_params()
for key in keys:
    exec("{0}='{1}'".format(key, parameters[key]))


# 検証環境であれば検証環境の値を使用する
def convert_key(key, is_develop):
    return "DEV_" + key if is_develop else key


DATABASES = {
    'default': {
        'ENGINE': parameters[convert_key("DB_ENGINE", is_dev)],
        'NAME': parameters[convert_key("DB_NAME", is_dev)],
        'HOST': parameters[convert_key("DB_HOST", is_dev)],
        'USER': parameters[convert_key("DB_USER", is_dev)],
        'PASSWORD': parameters[convert_key("DB_PASSWORD", is_dev)]
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


