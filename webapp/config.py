import os

DB_name = "Movies.db"


class Config:
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    SECRET_KEY = "SECRET_KEY"
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_name}'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
