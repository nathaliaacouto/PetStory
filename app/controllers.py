from app import db
from app.models import Cliente, Gaiola, Pet, Servico, Atendimento, Funcionario


class ClienteController():
    def create_cliente(self, fields):
        cliente = Cliente(
            nome=fields.get('nome', None),
            instagram=fields.get('instagram', None),
            telefone=fields.get('telefone', None),
            cep=fields.get('cep', None),
            endereco=fields.get('endereco', None),
            email=fields.get('email', None)
        )
        return cliente

    def add_cliente(self, cliente):
        db.session.add(cliente)
        db.session.commit()

    def get_cliente_by_nome(self, nome):
        return Cliente.query.filter_by(nome=nome).first()

    def get_cliente_by_telefone(self, telefone):
        return Cliente.query.filter_by(telefone=telefone).first()

    def get_cliente_by_id(self, id):
        return Cliente.query.filter_by(id=id).first()


class PetController():
    def create_pet(self, fields):
        pet = Pet(
            nome=fields.get('nome', None),
            raca=fields.get('raca', None),
            idade=fields.get('idade', None),
            pelagem=fields.get('pelagem', None),
            obito=fields.get('obito', None)
        )
        return pet

    def add_pet(self, pet, cliente):
        pet.dono = cliente
        db.session.add(pet)
        db.session.commit()

    # cliente -> string
    def list_pets_from_cliente(self, cliente):
        controller = ClienteController()
        cliente_data = controller.get_cliente_by_nome(cliente)
        pets = Pet.query.filter_by(dono_id=cliente_data.id).all()
        return pets

    def get_pet_by_nome(self, nome):
        return Pet.query.filter_by(nome=nome).first()

    def get_pet_by_id(self, id):
        return Pet.query.filter_by(id=id).first()


class AtendimentoController():
    def create_atendimento(self, status):
        atendimento = Atendimento(
            status=status,
        )
        return atendimento

    def add_atendimento(self, atendimento, pet, servicos, gaiola, obs=None):
        atendimento.pet_atendido = pet
        atendimento.gaiola = gaiola
        self.lock_gaiola(gaiola)
        if obs:
            atendimento.obs = obs
        for servico in servicos:
            atendimento.servicos.append(servico)
        db.session.add(atendimento)
        db.session.commit()
        return atendimento

    def add_funcionario(self, atendimento, funcionario):
        atendimento.codigo_func = funcionario.codigo
        db.session.add(atendimento)
        db.session.commit()
        return atendimento

    def get_atendimento_by_id(self, atend_id):
        return Atendimento.query.filter_by(id=atend_id).first()

    def get_last_atendimento_by_id(self, pet_id):
        return Atendimento.query.filter_by(pet_id=pet_id).first()

    def get_atendimentos_by_cliente(self, cliente):
        cliente = Cliente.query.filter_by(id=cliente.id).first()
        pass

    def list_atendimentos_by_status(self, status):
        return Atendimento.query.filter_by(status=status).all()

    def lock_gaiola(self, gaiola_id):
        gaiola = Gaiola.query.filter_by(id=gaiola_id).first()
        gaiola.disponivel = False
        db.session.commit()

    def unlock_gaiola(self, gaiola_id):
        gaiola = Gaiola.query.filter_by(id=gaiola_id).first()
        gaiola.disponivel = True
        db.session.commit()

    def get_gaiola(self, atendimento):
        return Gaiola.query.filter_by(id=atendimento.gaiola).first()

    def update_status(self, atendimento):
        if atendimento.status == "pendente":
            atendimento.status = "em andamento"
        elif atendimento.status == "em andamento":
            atendimento.status = "concluido"
        elif atendimento.status == "concluido":
            self.unlock_gaiola(atendimento.gaiola)
            atendimento.status = "arquivado"
        db.session.commit()


class ServicoController():
    def get_servico_by_id(self, id):
        return Servico.query.filter_by(id=id).first()

    def get_servico_by_descricao(self, value):
        return Servico.query.filter_by(descricao=value).first()

    def get_servico_by_valor(self, value):
        return Servico.query.filter_by(valor=value).first()

    def get_all(self):
        return Servico.query.all()


class FuncionarioController():
    def create_funcionario(self, fields):
        funcionario = Funcionario(
            nome=fields.get('nome', None),
            email=fields.get('email', None),
            senha_hash=fields.get('senha_hash', None),
            codigo=fields.get('codigo', None),
            cargo=fields.get('cargo', None)
        )
        return funcionario

    def get_funcionario_by_codigo(self, codigo):
        return Funcionario.query.filter_by(codigo=codigo).first()
