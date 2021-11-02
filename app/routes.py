from flask import render_template, redirect, flash
from flask.helpers import url_for
from app import db
from app.forms import RegisterForm
from app.models import Cliente, Pet
from app.model import Model

def init_app(app):
    @app.route("/")
    @app.route("/login")
    def login():
        return render_template("login.html", title="Login")
    
    @app.route("/registro", methods=["GET", "POST"])
    def registro():
        form = RegisterForm()
        if form.validate_on_submit():
            cliente = Cliente(
                nome=form.owner.data,
                telefone=form.phone.data,
                cpf=form.cpf.data,
                cep=form.zip_code.data,
                endereco=form.address.data,
                email=form.email.data,
            )
            db.session.add(cliente)
            db.session.commit()
            pet = Pet(
                nome=form.dog.data,
                raca=form.breed.data,
                idade=form.age.data,
                pelagem=form.fur.data,
                obito=False,
                dono_id=cliente.id
            )
            db.session.add(pet)
            db.session.commit()
            flash('Cadastro realizado com sucesso!')
            return redirect(url_for('registro'))
        return render_template('registro.html', form=form, title="Novo Atendimento")
    
    @app.route("/fila")
    def fila():
        data = Model.read()
        return render_template("queue.html", data=data, title="Fila de Atendimentos")
