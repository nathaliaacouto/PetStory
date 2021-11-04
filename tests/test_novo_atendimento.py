from app.models import Cliente, Pet, Atendimento, Servico
from app.controllers import ClienteController, PetController, AtendimentoController

# funcionario acessa a pagina de novo atendimento
def test_request_returns_200(client):
    assert client.get("/novo-atendimento").status_code == 200

# funcionario registra o atendimento de um pet ja cadastrado
def test_registro_atendimento():
    cliente_controller = ClienteController()
    pet_controller = PetController()
    atendimento_controller = AtendimentoController()
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
    atendimento = Atendimento(
        status="Pendente",
    )
    pass
