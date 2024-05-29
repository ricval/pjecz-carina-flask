"""
Exh Exhortos Partes, formularios
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Optional

from carina.blueprints.exh_exhortos_partes.models import ExhExhortoParte


TIPOS_PARTES = [
    (0, "NO DEFINIDO (Defina un Tipo Parte Nombre)"),
    (1, "ACTOR"),
    (2, "DEMANDADO"),
]


class ExhExhortoParteForm(FlaskForm):
    """Formulario ExhExhortoParte"""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=256)])
    apellido_paterno = StringField("Apellido Paterno", validators=[Optional(), Length(max=256)])
    apellido_materno = StringField("Apellido Materno", validators=[Optional(), Length(max=256)])
    genero = RadioField("Genero", coerce=str, choices=ExhExhortoParte.GENEROS.items(), validators=[Optional()], default="M")
    es_persona_moral = BooleanField("Es Persona Moral")
    tipo_parte = SelectField("Tipo de Parte", coerce=int, choices=TIPOS_PARTES, validators=[Optional()])
    tipo_parte_nombre = StringField("Tipo Parte Nombre")
    guardar = SubmitField("Guardar")
