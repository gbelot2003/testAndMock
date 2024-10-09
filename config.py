import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-muy-secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///dev_database.db'

class DeployConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///deploy_database.db'

class DefaultConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///default_database.db'

config = {
    'development': DevelopmentConfig,
    'deploy': DeployConfig,
    'default': DefaultConfig
}