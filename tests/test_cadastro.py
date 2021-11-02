from app.models import Cliente, Pet
from app import db

def test_app_is_created(app):
    assert app.name == 'app'  

def test_request_returns_200(client):
    assert client.get("/registro").status_code == 200

def test_registro_cliente(app):
    c1 = Cliente(
        nome="Lucas",
        telefone="12345678",
        cpf="14785236987",
        cep="32147896", 
        endereco="Rua Exemplo, 123",
        email="lucas@gmail.com"
    )
    db.session.add(c1)
    db.session.commit()
    cliente1 = Cliente.query.filter_by(nome="Lucas").first()
    assert cliente1.nome == c1.nome

def test_registro_pet(app):
    c1 = Cliente.query.filter_by(nome="Lucas").first()
    p1 = Pet(
        nome="Aylla",
        raca="Shihtzu",
        pelagem="Branca com marrom",
        obito=False,
        dono_id = c1.id
    )
    db.session.add(p1)
    db.session.commit()
    pet1 = Pet.query.filter_by(nome="Aylla").first()
    assert pet1.nome == p1.nome and pet1.dono_id == c1.id