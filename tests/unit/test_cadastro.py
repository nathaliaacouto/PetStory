from app.models import Cliente
from app.controllers import ClienteController, PetController
from tests.helpers import cadastrar_cliente_pet

def test_app_is_created(app):
    assert app.name == 'app'  

def test_request_returns_200(client):
    assert client.get("/registro").status_code == 200

def test_registro_cliente():
    cliente_controller = ClienteController()
    cliente = cliente_controller.create_cliente({
        "nome": "Alberto Silva",
        "telefone": "12340987",
        "cpf": "89874102147",
        "cep": "32147452", 
        "endereco": "Rua Exemplo, 854",
        "email": "alberto@gmail.com"
    })
    cliente_controller.add_cliente(cliente)
    cliente_db = cliente_controller.get_cliente_by_nome("Alberto Silva")
    assert cliente_db.nome == cliente.nome

def test_registro_pet():
    pet_controller = PetController()
    cliente, pet = cadastrar_cliente_pet()
    pet_controller.add_pet(pet, cliente)
    pet_db = pet_controller.get_pet_by_nome("Aylla")
    assert pet_db.nome == pet.nome and pet_db.dono_id == cliente.id

def test_registro_cliente_pets():
    p_control = PetController()
    cliente, pet1 = cadastrar_cliente_pet()
    pet2 = p_control.create_pet({
        "nome": "Max",
        "raca": "Pug",
        "pelagem": "branca com manchas pretas",
        "obito": False
    })
    p_control.add_pet(pet2, cliente)
    pet3 = p_control.create_pet({
        "nome": "Tony",
        "raca": "Shihtzu",
        "pelagem": "branca com marrom claro",
        "obito": False
    })
    p_control.add_pet(pet3, cliente)
    assert pet1.dono_id == cliente.id
    assert pet2.dono_id == cliente.id
    assert pet3.dono_id == cliente.id
