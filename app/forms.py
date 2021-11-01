from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    dog = StringField('Nome do pet', validators=[DataRequired()])
    breed = StringField('Raça', validators=[DataRequired()])
    fur = StringField('Pelagem')
    age = IntegerField('Idade', validators=[DataRequired()])
    owner = StringField('Nome do tutor', validators=[DataRequired()])
    cpf = StringField('CPF')
    zip_code = StringField('CEP')
    address = StringField('Endereço')
    phone = StringField('Telefone', validators=[DataRequired()])
    email = StringField('E-mail')
    submit = SubmitField('Cadastrar')
