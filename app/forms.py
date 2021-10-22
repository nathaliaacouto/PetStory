from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AtendimentoForm(FlaskForm):
    dog = StringField('Nome do pet', validators=[DataRequired()])
    breed = StringField('Raca', validators=[DataRequired()])
    owner = StringField('Nome do dono', validators=[DataRequired()])
    phone = StringField('Telefone para contato', validators=[DataRequired()])
    email = StringField('E-mail')
    submit = SubmitField('Cadastrar')
