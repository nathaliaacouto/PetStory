from flask import render_template, redirect, flash, url_for
from app.forms import ClienteRegisterForm, BuscaClienteForm
from app.models import Cliente, Pet
from app.controllers import ClienteController, PetController, ServicoController

def init_app(app):
    cliente_controller = ClienteController()
    pet_controller = PetController()
    servico_controller = ServicoController()

    @app.route("/")
    @app.route("/login")
    def login():
        return render_template("login.html", title="Login")
    
    @app.route("/registro", methods=["GET", "POST"])
    def registro():
        form = ClienteRegisterForm()
        if form.add_pet.data:
            form.pets.append_entry()
            return render_template('registro.html', form=form)

        if form.validate_on_submit():
            cliente = Cliente(
                nome=form.owner.data,
                telefone=form.phone.data,
                cpf=form.cpf.data,
                cep=form.zip_code.data,
                endereco=form.address.data,
                email=form.email.data,
            )
            cliente_controller.add_cliente(cliente)
            for pet in form.pets:
               if pet.dog.data:
                    new = Pet(
                        nome=pet.dog.data,
                        raca=pet.breed.data,
                        idade=pet.age.data,
                        pelagem=pet.fur.data,
                        obito=False,
                    )
                    pet_controller.add_pet(new, cliente)
            flash('Cadastro realizado com sucesso!')
            return redirect(url_for('registro'))
        return render_template('registro.html', form=form, title="Registro")
    
    @app.route("/fila")
    def fila():
        # (alert): because i remove "from app.model import Model", 
        #          so this function/endpoint has server error. att@silvamva

        # data = Model.read()
        # return render_template("queue.html", data=data, title="Fila de Atendimentos")

        return "<h2>Em desenvolvimento</h2>"
    
    @app.route("/novo-atendimento", methods=["GET", "POST"])
    def novo_atendimento():
        form = BuscaClienteForm()

        if form.search.data:
            if not form.user_data.entries:
                cliente = cliente_controller.get_cliente_by_telefone(form.search_box.data)
                if cliente:
                    MAX_ENTRIES = 3
                    pets = pet_controller.list_pets_from_cliente(cliente.nome)
                    pet_options = [(p.id, p.nome) for p in pets]
                    form.user_data.append_entry(data=cliente)
                    form.pet_data.append_entry()
                    form.pet_data.entries[0].dog.choices = pet_options
                    servicos = servico_controller.get_all()
                    servicos_options = [(0 , "---")]
                    servicos_options += [(s.id, s.descricao) for s in servicos]
                    for i in range(MAX_ENTRIES):
                        form.servicos_data.append_entry()
                        form.servicos_data.entries[i].servico.choices = servicos_options
                    return render_template("novo_atendimento.html", title="Novo Atendimento", form=form)
                flash('Cliente não encontrado')
        
        if form.is_submitted():
            for pet in form.pet_data:
                print(type(pet.dog.data))
            for s in form.servicos_data:
                print(type(s.servico.data))
            flash("atendimento marcado")
            return redirect(url_for('novo_atendimento'))
        print(form.errors)
        return render_template("novo_atendimento.html", title="Novo Atendimento", form=form)
