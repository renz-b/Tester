import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change this later'
    QUICKTEST_ADMIN = os.environ.get('QUICKTEST_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SSL_REDIRECT = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_POSTGRES')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_POSTGRES')


class ProductionConfig(Config):
    DEBUG = False
    uri = os.environ.get('DATABASE_URL')
    split_uri = ''
    try:
        split_uri = uri.split(':', 1)[1]
    except:
        pass
    
    SQLALCHEMY_DATABASE_URI = "postgresql:"+ split_uri

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle reverse proxy server headers
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.DEBUG) #set to show all logs
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
    'heroku' : HerokuConfig,
    'testing' : TestingConfig,
    'default': DevelopmentConfig
    }



# TODO HEROKU CONFIG
