from datetime import datetime
from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), index=True)
    telefone = db.Column(db.String(15))
    cpf = db.Column(db.String(20))
    cep = db.Column(db.String(20))
    endereco = db.Column(db.String(100))
    email = db.Column(db.String(100), index=True)
    pets = db.relationship('Pet', backref='dono', lazy='dynamic')

    def __repr__(self):
        return '<Cliente {}>'.format(self.nome)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), index=True)
    raca = db.Column(db.String(50))
    pelagem = db.Column(db.String(50))
    obito = db.Column(db.Boolean, default=False)
    dono_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    atendimentos = db.relationship('Atendimento', backref='pet_atendido', lazy='dynamic')

    def __repr__(self):
        return '<Pet {}>'.format(self.nome)

atendimento_servico = db.Table('atendimento_servico',
    db.Column('atendimento_id', db.Integer, db.ForeignKey('atendimento.id')),
    db.Column('servico_id', db.Integer, db.ForeignKey('servico.id'))
)
class Atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status = db.Column(db.String, index=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    servicos = db.relationship(
        'Servico',
        backref="atendimentos",
        secondary=atendimento_servico,
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Atendimento {}>'.format(self.pet_atendido)

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(150))
    valor = db.Column(db.Float(precision=2))

    def __repr__(self):
        return '<Servico {} | R${}>'.format(self.descricao, self.valor)
