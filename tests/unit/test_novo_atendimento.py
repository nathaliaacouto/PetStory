from app.controllers import AtendimentoController, ClienteController, ServicoController, FuncionarioController
from tests.helpers import cadastrar_cliente_pet

def test_request_returns_200_on_novo_atendimento(client):
    assert client.get('/novo-atendimento').status_code == 200

def test_servicos_are_created(app):
    s_control = ServicoController()
    servicos = []
    servicos.append(s_control.get_servico_by_descricao("Banho Shihtzu"))
    servicos.append(s_control.get_servico_by_descricao("Hidratação"))
    assert servicos[0].valor == 30.00 and servicos[1].valor == 10.00

# funcionario registra o atendimento de banho e hidratacao para um pet
def test_registro_atendimento():
    a_controller = AtendimentoController()
    s_controller = ServicoController()
    f_controller = FuncionarioController()
    carlos = f_controller.create_funcionario({
        "nome": "Carlos",
        "email": "carlos@carlos.com",
        "senha_hash": "1234",
        "codigo": 56147,
        "cargo": "OPERACOES"
    })
    cliente, pet = cadastrar_cliente_pet()

    # funcionario cria um novo atendimento para o cliente, que solicita
    # serviços de banho e hidratação para o seu pet 
    atendimento = a_controller.create_atendimento("pendente")
    servicos = []
    servicos.append(s_controller.get_servico_by_descricao("Banho Shihtzu"))
    servicos.append(s_controller.get_servico_by_descricao("Hidratação"))
    gaiola = 2
    print(atendimento)
    print(pet)
    for s in servicos:
        print(s)
    a_controller.add_atendimento(atendimento, pet, servicos, gaiola)
    novo_atendimento = a_controller.get_last_atendimento_by_id(pet.id)
    a_controller.add_funcionario(novo_atendimento, carlos)
    lista_servicos = []
    for servico in novo_atendimento.servicos.all():
        lista_servicos.append(servico.descricao +' '+ str(servico.valor))
    gaiola_atual = a_controller.get_gaiola(novo_atendimento)
    assert lista_servicos[0] == "Banho Shihtzu 30.0" and lista_servicos[1] == "Hidratação 10.0"
    assert novo_atendimento.codigo_func == carlos.codigo
    assert gaiola_atual.id == 2 and gaiola_atual.disponivel == False
