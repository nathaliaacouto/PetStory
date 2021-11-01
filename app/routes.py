from flask import render_template
from app import app
from app.forms import RegisterForm
from app.model import Model

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/atendimento", methods=["GET", "POST"])
def atendimento():
    form = RegisterForm()
    if form.validate_on_submit():
        data = {
            "dog" : form.dog.data,
            "breed" : form.breed.data,
            "owner" : form.owner.data,
            "phone" : form.phone.data,
            "email" : form.email.data
        }
        Model.create(data)
    return render_template('registro.html', form=form, title="Novo Atendimento")

@app.route("/fila")
def fila():
    data = Model.read()
    return render_template("queue.html", data=data, title="Fila de Atendimentos")
