from flask import render_template, redirect, flash, url_for
from app.forms import ClienteRegisterForm, AtendimentoForm
from app.models import Cliente, Pet
from app.controllers import AtendimentoController, ClienteController, PetController, ServicoController
import app.integration as integration

def init_app(app):
    cliente_controller = ClienteController()
    pet_controller = PetController()
    servico_controller = ServicoController()
    atendimento_controller = AtendimentoController()

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
        form = AtendimentoForm()

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
        
        elif form.is_submitted():
            atendimento = atendimento_controller.create_atendimento("pendente")

            print(form.pet_data[0].dog.data)
            pet = pet_controller.get_pet_by_id(form.pet_data[0].dog.data)
            obs = form.obs_text_area.data
            print(obs)
            print(pet.dono)
            servicos = []
            servicos_ctypes = []
            for s in form.servicos_data:
                if s.servico.data != 0:
                    print(s.servico.data)
                    servico = servico_controller.get_servico_by_id(s.servico.data)
                    print(servico)
                    servicos.append(servico)
                    # CODIGO P/ CHAMAR O CTYPES
                    servicos_ctypes.append(servico.descricao.encode('utf-8'))
                    servicos_ctypes.append(str(int(servico.valor)).encode())
            atendimento_controller.add_atendimento(atendimento, pet, servicos, obs)
            integration.gerar_nfe(len(servicos_ctypes), servicos_ctypes)
            flash("atendimento marcado")
            return redirect(url_for('novo_atendimento'))
        print(form.errors)
        return render_template("novo_atendimento.html", title="Novo Atendimento", form=form)

# curr_dir = os.path.abspath(os.path.dirname(__file__))
# temp_dir = os.path.join(curr_dir, "temp.txt")
# with open(temp_dir, "w") as f:
#     f.write("{}\n".format(str(len(servicos_ctypes))))
#     i = 0
#     while i < len(servicos_ctypes):
#         f.write("{}\n".format(servicos_ctypes[i]))
#         f.write("{}\n".format(servicos_ctypes[i + 1]))
#         i += 2
# gerar_nfe()
