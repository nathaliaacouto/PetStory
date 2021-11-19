# flake8: noqa
from flask import render_template, redirect, flash, url_for, jsonify, request
from app.forms import ClienteRegisterForm, AtendimentoForm
from app.models import Gaiola, Pet
from app.controllers import AtendimentoController, ClienteController, PetController, ServicoController, FuncionarioController
import app.integration as integration


def init_app(app):
    cliente_controller = ClienteController()
    pet_controller = PetController()
    servico_controller = ServicoController()
    atendimento_controller = AtendimentoController()
    funcionario_controller = FuncionarioController()

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
            cliente = cliente_controller.create_cliente({
                'nome': form.owner.data,
                'instagram': form.instagram.data,
                'telefone': form.phone.data,
                'cep': form.zip_code.data,
                'endereco': form.address.data,
                'email': form.email.data
            })
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

    @app.route("/servicos")
    def servicos():
        atend_pendentes = []
        atend_andamento = []
        atend_concluido = []
        pendentes = atendimento_controller.list_atendimentos_by_status("pendente")
        em_andamento = atendimento_controller.list_atendimentos_by_status("em andamento")
        concluidos = atendimento_controller.list_atendimentos_by_status("concluido")
        for p in pendentes:
            servico = {}
            pet_info = pet_controller.get_pet_by_id(p.pet_id)
            cliente_info = cliente_controller.get_cliente_by_id(pet_info.dono_id)
            servico['id'] = p.id
            servico['gaiola'] = p.gaiola
            servico['nome_pet'] = pet_info.nome
            servico['raca_pet'] = pet_info.raca
            servico['tutor'] = cliente_info.nome
            servico['servicos'] = [serv.descricao for serv in p.servicos]
            servico['obs'] = p.obs or "Sem observações"
            atend_pendentes.append(servico)

        for a in em_andamento:
            servico = {}
            pet_info = pet_controller.get_pet_by_id(a.pet_id)
            cliente_info = cliente_controller.get_cliente_by_id(pet_info.dono_id)
            funcionario_info = funcionario_controller.get_funcionario_by_codigo(a.codigo_func)
            servico['id'] = a.id
            servico['gaiola'] = a.gaiola
            servico['nome_pet'] = pet_info.nome
            servico['raca_pet'] = pet_info.raca
            servico['tutor'] = cliente_info.nome
            servico['funcionario'] = funcionario_info.nome
            servico['servicos'] = [serv.descricao for serv in a.servicos]
            servico['obs'] = a.obs or "Sem observações"
            atend_andamento.append(servico)

        for c in concluidos:
            servico = {}
            pet_info = pet_controller.get_pet_by_id(c.pet_id)
            cliente_info = cliente_controller.get_cliente_by_id(pet_info.dono_id)
            funcionario_info = funcionario_controller.get_funcionario_by_codigo(c.codigo_func)
            servico['id'] = c.id
            servico['gaiola'] = c.gaiola
            servico['nome_pet'] = pet_info.nome
            servico['raca_pet'] = pet_info.raca
            servico['tutor'] = cliente_info.nome
            servico['funcionario'] = funcionario_info.nome
            servico['servicos'] = [serv.descricao for serv in c.servicos]
            servico['obs'] = c.obs or "Sem observações"
            atend_concluido.append(servico)
        return render_template(
            "servicos.html",
            title="Serviços",
            atend_pendentes=atend_pendentes,
            atend_andamento=atend_andamento,
            atend_concluido=atend_concluido
        )

    @app.route("/process-atendimento", methods=["POST"])
    def process_atendimento():
        atend_id = request.form["id"]
        atendimento = atendimento_controller.get_atendimento_by_id(atend_id)
        if request.form["code"]:
            staff_code = int(request.form["code"])
            funcionario = funcionario_controller.get_funcionario_by_codigo(staff_code)
            atendimento_controller.add_funcionario(atendimento, funcionario)
        atendimento_controller.update_status(atendimento)
        return jsonify({"message": "success"})

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
                    servicos_options = [(0, "---")]
                    servicos_options += [(s.id, s.descricao) for s in servicos]
                    for i in range(MAX_ENTRIES):
                        form.servicos_data.append_entry()
                        form.servicos_data.entries[i].servico.choices = servicos_options
                    form.cages_data.append_entry()
                    gaiolas = Gaiola.query.filter_by(disponivel=True).all()

                    form.cages_data.entries[0].available_cages.choices = [(g.id, str(g.numero)) for g in gaiolas]
                    return render_template("novo_atendimento.html", title="Novo Atendimento", form=form)
                flash('Cliente não encontrado')

        elif form.is_submitted():
            atendimento = atendimento_controller.create_atendimento("pendente")
            pet = pet_controller.get_pet_by_id(form.pet_data[0].dog.data)
            obs = form.obs_text_area.data
            gaiola = form.cages_data[0].available_cages.data
            servicos = []
            servicos_ctypes = []
            for s in form.servicos_data:
                if s.servico.data != 0:
                    servico = servico_controller.get_servico_by_id(s.servico.data)
                    servicos.append(servico)
                    servicos_ctypes.append(servico.descricao.encode('utf-8'))
                    servicos_ctypes.append(str(int(servico.valor)).encode())
            atendimento_controller.add_atendimento(atendimento, pet, servicos, gaiola, obs)
            # CODIGO P/ CHAMAR O CTYPES
            integration.gerar_nfe(len(servicos_ctypes), servicos_ctypes)
            flash("atendimento marcado")
            return redirect(url_for('novo_atendimento'))
        print(form.errors)
        return render_template("novo_atendimento.html", title="Novo Atendimento", form=form)

    @app.route('/clientes')
    def clientes():
        return render_template('busca_clientes.html')
