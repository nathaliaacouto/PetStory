from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FormField, FieldList
from wtforms.validators import DataRequired

class PetRegisterForm(FlaskForm):
    class Meta:
        csrf = False
    dog = StringField('* Nome do pet', validators=[DataRequired()])
    breed = StringField('* Raça', validators=[DataRequired()])
    fur = StringField('Pelagem')
    age = IntegerField('Idade')

class ClienteRegisterForm(FlaskForm):
    owner = StringField('* Nome do tutor', validators=[DataRequired("Campo Obrigatório")])
    cpf = StringField('CPF')
    zip_code = StringField('CEP')
    address = StringField('Endereço')
    phone = StringField('* Telefone', validators=[DataRequired()])
    email = StringField('E-mail')
    pets = FieldList(FormField(PetRegisterForm), min_entries=1, max_entries=3)
    submit = SubmitField('Cadastrar')
    add_pet = SubmitField("+ Adicionar pet")

class ClienteHelperForm(FlaskForm):
    class Meta:
        csrf = False
    nome = StringField()
    phone = StringField()

class PetHelperForm(FlaskForm):
    class Meta:
        csrf = False
    dog = StringField()
    breed = StringField()
    fur = StringField()
    age = IntegerField()

class BuscaClienteForm(FlaskForm): 
    search_box = StringField('Telefone do Cliente')
    user_data = FieldList(FormField(ClienteHelperForm), min_entries=0, max_entries=1)
    pet_data = FieldList(FormField(PetHelperForm), min_entries=0, max_entries=1)
    search = SubmitField('Buscar')
    choose = SubmitField('Escolher pet')
    submit = SubmitField('Registrar Atendimento')
