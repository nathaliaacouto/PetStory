from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FormField
from wtforms import FieldList, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class PetRegisterForm(FlaskForm):
    class Meta:
        csrf = False
    dog = StringField('* Nome do pet', validators=[DataRequired()])
    breed = StringField('* Raça', validators=[DataRequired()])
    fur = StringField('Pelagem')
    age = IntegerField('Idade')


class ClienteRegisterForm(FlaskForm):
    owner = StringField(
        '* Nome do tutor',
        validators=[DataRequired("Campo Obrigatório")]
    )
    zip_code = StringField('CEP')
    instagram = StringField('Instagram')
    address = StringField('Endereço')
    phone = StringField('* Telefone', validators=[DataRequired()])
    email = StringField('E-mail')
    pets = FieldList(FormField(PetRegisterForm), min_entries=1, max_entries=3)
    submit = SubmitField('Cadastrar')
    add_pet = SubmitField("+ Adicionar pet")


class ClienteHelperForm(FlaskForm):
    class Meta:
        csrf = False
    nome = StringField('Cliente')
    telefone = StringField('Telefone')


class PetHelperForm(FlaskForm):
    class Meta:
        csrf = False
    dog = SelectField('Pet', coerce=int, choices=[(1, 'Um'), (2, 'Dois')])


class ServicosForm(FlaskForm):
    class Meta:
        csrf = False
    servico = SelectField(
        'Serviço',
        coerce=int,
        choices=[(1, 'Um'), (2, 'Dois')],
        validators=[Optional()]
    )


class GaiolasForm(FlaskForm):
    class Meta:
        csrf = False
    available_cages = SelectField(
        "Gaiola",
        coerce=int,
        choices=[(1, 'Um'), (2, 'Dois')]
    )


class AtendimentoForm(FlaskForm):
    search_box = IntegerField('Telefone do Cliente')
    user_data = FieldList(
        FormField(ClienteHelperForm),
        min_entries=0,
        max_entries=1
    )
    pet_data = FieldList(
        FormField(PetHelperForm),
        min_entries=0,
        max_entries=1
    )
    servicos_data = FieldList(
        FormField(ServicosForm),
        min_entries=0,
        max_entries=3
    )
    cages_data = FieldList(
        FormField(GaiolasForm),
        min_entries=0,
        max_entries=1
    )
    obs_text_area = TextAreaField(
        "Observações",
        validators=[Optional(), Length(max=200)]
    )
    search = SubmitField('Buscar')
    submit = SubmitField('Adicionar novo serviço')
