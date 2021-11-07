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
