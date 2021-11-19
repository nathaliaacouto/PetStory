from app.models import Funcionario, Gaiola, Servico
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

    g1 = Gaiola(numero=1)
    g2 = Gaiola(numero=2)
    g3 = Gaiola(numero=3)
    g4 = Gaiola(numero=4)
    g5 = Gaiola(numero=5)
    g6 = Gaiola(numero=6)
    g7 = Gaiola(numero=7)
    g8 = Gaiola(numero=8)
    g9 = Gaiola(numero=9)
    g10 = Gaiola(numero=10)
    db.session.add_all([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10])
    db.session.commit()

    f1 = Funcionario(
        nome="A",
        email="a@gmail.com",
        senha_hash="senhafuncionarioa",
        codigo=1234,
        cargo="OPERACOES"
    )
    f2 = Funcionario(
        nome="B",
        email="b@gmail.com",
        senha_hash="senhafuncionariob",
        codigo=2345,
        cargo="BALCAO"
    )
    db.session.add_all([f1, f2])
    db.session.commit()
