import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from app import create_app
from app import db
from config import Config
from app.models import Servico

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

def create_servicos():
    s1 = Servico(descricao="Banho Shihtzu", valor=30.00)
    s2 = Servico(descricao="Banho Pug", valor=28.00)
    s3 = Servico(descricao="Hidratação", valor=10.00)
    s4 = Servico(descricao="Tosa higiênica", valor=15.00)
    s5 = Servico(descricao="Tosa Shihtzu", valor=35.00)
    s6 = Servico(descricao="Tosa Pug", valor=33.00)
    db.session.add_all([s1, s2, s3, s4, s5, s6])
    db.session.commit()


@pytest.fixture(scope="module")
def app():
    """instancia do app"""
    app = create_app(TestConfig)
    c = app.app_context()
    c.push()
    db.create_all()
    create_servicos()
    yield app
    db.session.remove()
    db.drop_all()
    c.pop()

@pytest.fixture(scope="module")
def browser():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser
    browser.close()
