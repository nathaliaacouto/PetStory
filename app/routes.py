from flask import render_template
from app import app
from app.forms import AtendimentoForm
from app.models import Model

@app.route("/")
@app.route("/index")
def index():
    dogs = [
        {
            "name": "Aylla",
            "info": "Shihtzu"
        },
        {
            "name": "Stella",
            "info": "Pug"
        }
    ]
    return render_template("index.html", dogs=dogs, title="Home")

@app.route("/atendimento", methods=["GET", "POST"])
def atendimento():
    form = AtendimentoForm()
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
