import os

ENV = "testing"
TESTING = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_FOR_TESTING")