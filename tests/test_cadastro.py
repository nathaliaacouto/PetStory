from app.models import Cliente, Pet
from app import db
from app.controllers import ClienteController, PetController

def test_app_is_created(app):
    assert app.name == 'app'  

def test_request_returns_200(client):
    assert client.get("/registro").status_code == 200

def test_registro_cliente(app):
    cliente_controller = ClienteController()
    cliente = Cliente(
        nome="Alberto Silva",
        telefone="12340987",
        cpf="89874102147",
        cep="32147452", 
        endereco="Rua Exemplo, 854",
        email="alberto@gmail.com"
    )
    cliente_controller.add_cliente(cliente)
    cliente_db = cliente_controller.get_cliente_by_nome("Alberto Silva")
    assert cliente_db.nome == cliente.nome

def test_registro_pet(app):
    pet_controller = PetController()
    cliente_controller = ClienteController()
    cliente = Cliente(
        nome="Lucas",
        telefone="12345678",
        cpf="14785236987",
        cep="32147896", 
        endereco="Rua Exemplo, 123",
        email="lucas@gmail.com"
    )
    cliente_controller.add_cliente(cliente)
    pet = Pet(
        nome="Aylla",
        raca="Shihtzu",
        pelagem="Branca com marrom",
        obito=False,
    )
    pet_controller.add_pet(pet, cliente)
    pet_db = pet_controller.get_pet_by_nome("Aylla")
    assert pet_db.nome == pet.nome and pet_db.dono_id == cliente.id
