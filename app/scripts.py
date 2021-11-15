from app.models import Servico
from app import db

def popular_tabelas():
    s1 = Servico(descricao="Banho Shihtzu", valor=30.00)
    s2 = Servico(descricao="Banho Pug", valor=28.00)
    s3 = Servico(descricao="Hidratação", valor=10.00)
    s4 = Servico(descricao="Tosa higiênica", valor=15.00)
    s5 = Servico(descricao="Tosa Shihtzu", valor=35.00)
    s6 = Servico(descricao="Tosa Pug", valor=33.00)
    db.session.add_all([s1, s2, s3, s4, s5, s6])
    db.session.commit()