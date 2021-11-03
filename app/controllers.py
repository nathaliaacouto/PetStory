from app import db
from app.models import Cliente, Pet

class ClienteController():
    def add_cliente(self, cliente):
        db.session.add(cliente)
        db.session.commit()

    def get_cliente_by_nome(self, nome):
        cliente1 = Cliente.query.filter_by(nome=nome).first()
        return cliente1

class PetController():
    def add_pet(self, pet, cliente):
        pet.dono = cliente
        db.session.add(pet)
        db.session.commit()
    
    def list_pet_from_cliente(self, cliente):
        # Pet.query.filter_by()...
        pass

    def get_pet_by_nome(self, nome):
        pet = Pet.query.filter_by(nome=nome).first()
        return pet

class AtendimentoController():
    pass