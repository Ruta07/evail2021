import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import MetaData

metadata = MetaData(schema='public')
db = SQLAlchemy(metadata=metadata)

SQLALCHEMY_TRACK_MODIFICATIONS = False


class BaseConfig:
    """Base configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_USER = 'postgres'
    DB_PWD = 'root'
    DB_HOST = 'localhost' + ':' + '5432'
    DB_NAME = 'Blockchain'

    SSL_MODE = os.getenv('SSL_MODE', 'verify-ca')

    SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USER + ':' + DB_PWD + '@' + \
                              DB_HOST + '/' + DB_NAME

    print(SQLALCHEMY_DATABASE_URI)