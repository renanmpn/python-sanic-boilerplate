#  -*- coding: utf-8 -*-
"""
Config File for enviroment variables
"""
import os
from importlib import import_module

from dotenv import load_dotenv


class Config(object):
    """
    Base class for all config variables
    """
    # Load file from the path.
    load_dotenv()

    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    ENVIRONMENT = 'development'
    REDIS_URL = os.environ['REDIS_URL']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_DATABASE = os.environ['DB_DATABASE']
    DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'


class ProductionConfig(Config):
    """
    Production Config... this is the real thing
    """


class StagingConfig(Config):
    """
    Staging Config is for... staging things
    """
    DEBUG = False
    ENVIRONMENT = 'staging'


class DevelopmentConfig(Config):
    """
    Development Config... this is your home developer!
    """
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = True


class SandboxConfig(Config):
    """
    Development Config... this is your home developer!
    """
    DEBUG = True
    ENVIRONMENT = 'sandbox'
    SQLALCHEMY_RECORD_QUERIES = True


class TestingConfig(DevelopmentConfig):
    """
    Test Config... You should be testing right now instead reading docs!!!
    """
    TESTING = True
    KEY_ON_TEST = 'KEY ON TEST'
    ENVIRONMENT = 'test'


class ConfigClassNotFound(Exception):
    """
    Raises when the APP_SETTINGS environment variable have a value which does not point to an uninstantiable class.
    """
    pass


def get_config():
    """
    Get the Config Class instance defined in APP_SETTINGS environment variable
    :return The config class instance
    :rtype: Config
    """
    config_imports = os.environ['APP_SETTINGS'].split('.')
    config_class_name = config_imports[-1]
    config_module = import_module('.'.join(config_imports[:-1]))
    config_class = getattr(config_module, config_class_name, None)
    if not config_class:
        raise ConfigClassNotFound('Unable to find a config class in {}'.format(os.environ['APP_SETTINGS']))
    return config_class()
