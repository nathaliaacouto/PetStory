from app.models import Pet, Atendimento
from app.controllers import ClienteController, PetController, AtendimentoController, ServicoController
from tests.helpers import cadastrar_cliente_pet

    
# funcionario acessa a pagina de novo atendimento
def test_request_returns_200(client):
    assert client.get("/novo-atendimento").status_code == 200

def test_servicos_are_created():
    s_control = ServicoController()
    servicos = []
    servicos.append(s_control.get_servico_by_descricao("Banho Shihtzu"))
    servicos.append(s_control.get_servico_by_descricao("Hidratacao"))
    assert servicos[0].valor == 30.00 and servicos[1].valor == 10.00

# funcionario registra o atendimento de banho e hidratacao para um pet
def test_registro_atendimento():
    atendimento_controller = AtendimentoController()
    servico_controller = ServicoController()
    cliente, pet = cadastrar_cliente_pet()

    # funcionario cria um novo atendimento para o cliente, que solicita
    # serviços de banho e hidratação para o seu pet 
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
