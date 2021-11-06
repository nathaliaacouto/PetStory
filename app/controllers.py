from app import db
from app.models import Cliente, Pet, Servico, Atendimento

class ClienteController():
    def create_cliente(self, fields):
        cliente = Cliente(
            nome=fields['nome'],
            telefone=fields['telefone'],
            cpf=fields['cpf'],
            cep=fields['cep'],
            endereco=fields['endereco'],
            email=fields['email']
        )
        return cliente

    def add_cliente(self, cliente):
        db.session.add(cliente)
        db.session.commit()

    def get_cliente_by_nome(self, nome):
        cliente1 = Cliente.query.filter_by(nome=nome).first()
        return cliente1

class PetController():
    def create_pet(self, fields):
        pet = Pet(
            nome=fields['nome'],
            raca=fields['raca'],
            pelagem=fields['pelagem'],
            obito=fields['obito']
        )
        return pet

    def add_pet(self, pet, cliente):
        pet.dono = cliente
        db.session.add(pet)
        db.session.commit()
    
    # cliente -> string
    def list_pet_from_cliente(self, cliente):
        controller = ClienteController()
        cliente_data = controller.get_cliente_by_nome(cliente)
        pets = Pet.query.filter_by(dono_id=cliente_data.id).all()
        return pets

    def get_pet_by_nome(self, nome):
        return Pet.query.filter_by(nome=nome).first()

class AtendimentoController():
    def add_atendimento(self, atendimento, pet, servicos):
        atendimento.pet_atendido = pet
        for servico in servicos:
            atendimento.servicos.append(servico)
        db.session.add(atendimento)
        db.session.commit()
    
    def get_atendimentos_by_cliente(self, cliente):
        cliente = Cliente.query.filter_by(id=cliente.id).first()
        pass

    def get_atendimentos_by_status(self, status):
        return Atendimento.query.filter_by(status=status).all()

    def update_status(self, atendimento, novo_status):
        pass

class ServicoController():
    def get_servico_by_descricao(self, value):
        return Servico.query.filter_by(descricao=value).first()
    
    def get_servico_by_valor(self, value):
        return Servico.query.filter_by(valor=value).first()
