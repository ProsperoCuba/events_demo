from decouple import config

if config("APP_ENVIRONMENT") == "dev":
    from .dev import *  # pylint: disable=wildcard-import

if config("APP_ENVIRONMENT") == "prod":
    from .prod import *  # pylint: disable=wildcard-import
