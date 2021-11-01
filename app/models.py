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

    def __repr__(self):
        return '<Pet {}>'.format(self.nome)
