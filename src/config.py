import os


class Config(object):
    DEBUG = False
    TESTING = False
    PORT = os.getenv('PORT', '4000')
    HOST = '127.0.0.1'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_list = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

config = config_list[os.getenv('FLASK_ENV', 'default')]
