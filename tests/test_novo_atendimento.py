from app.models import Pet, Atendimento, Servico
from app.controllers import ClienteController, PetController, AtendimentoController, ServicoController

# funcionario acessa a pagina de novo atendimento
def test_request_returns_200(client):
    assert client.get("/novo-atendimento").status_code == 200

def test_servicos_are_created():
    servicos = []
    servicos.append(Servico.query.filter_by(descricao="Banho Shihtzu").first())
    servicos.append(Servico.query.filter_by(descricao="Hidratacao").first())
    assert servicos[0].valor == 30.00 and servicos[1].valor == 10.00


# funcionario registra o atendimento de banho e hidratacao para um pet
def test_registro_atendimento():
    cliente_controller = ClienteController()
    pet_controller = PetController()
    atendimento_controller = AtendimentoController()
    servico_controller = ServicoController()
    cliente = cliente_controller.create_cliente({
        "nome": "Lucas",
        "telefone": "12345678",
        "cpf": "14785236987",
        "cep": "32147896", 
        "endereco": "Rua Exemplo, 123",
        "email": "lucas@gmail.com"
    })
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
    servicos = []
    servicos.append(servico_controller.get_servico_by_descricao("Banho Shihtzu"))
    servicos.append(servico_controller.get_servico_by_descricao("Hidratacao"))
    atendimento_controller.add_atendimento(atendimento, pet, servicos)
    novo_atendimento = Atendimento.query.filter_by(pet_id=pet.id).first()
    lista_servicos = []
    for atendimento in novo_atendimento.servicos.all():
        lista_servicos.append(atendimento.descricao)
    assert lista_servicos[0] == "Banho Shihtzu" and lista_servicos[1] == "Hidratacao"
