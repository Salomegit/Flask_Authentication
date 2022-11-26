from os import getenv, path
import os
from dotenv import load_dotenv
load_dotenv()

# Define base directory
BASE_DIR = path.abspath(path.join(path.dirname(__file__),'../'))
print("Dir ", BASE_DIR)


class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/{path.join(getenv('DB_NAME') or 'app_db')}.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY=getenv("SECRET_KEY") or 'somesecret'


class TestingConfig:
    SQLALCHEMY_DATABASE_URI="mysql://salome:password@localhost/mydatabase"
    


class ProductionConfig:
    ...


config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig
}
