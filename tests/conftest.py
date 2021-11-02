import pytest
from app import create_app
from app import db
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

@pytest.fixture(scope="module")
def app():
    """instancia do app"""
    app = create_app(TestConfig)
    c = app.app_context()
    c.push()
    db.create_all()
    yield app
    db.session.remove()
    db.drop_all()
    c.pop()
