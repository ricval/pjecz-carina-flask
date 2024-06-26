"""
Exh Exhortos, formularios
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import IntegerField, RadioField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

from carina.blueprints.exh_areas.models import ExhArea
from carina.blueprints.exh_exhortos.models import ExhExhorto
from carina.blueprints.materias.models import Materia


def materias_opciones():
    """Materias: opciones para select"""
    return Materia.query.filter_by(estatus="A").order_by(Materia.clave).all()


class ExhExhortoNewForm(FlaskForm):
    """Formulario New Exhorto"""

    exhorto_origen_id = StringField("Exhorto Origen ID", validators=[DataRequired(), Length(max=128)])
    estado_destino = SelectField(
        "Estado Destino", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    municipio_destino = SelectField(
        "Municipio Destino", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    materia = SelectField("Materia", coerce=int, validators=[DataRequired()])
    estado_origen = StringField("Estado Origen")  # Las opciones se agregan con JS
    municipio_origen = SelectField(
        "Municipio Origen", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    juzgado_origen = SelectField("Juzgado Origen", coerce=int, validate_choice=False, validators=[DataRequired()])
    numero_expediente_origen = StringField("Número de Expediente Origen", validators=[DataRequired(), Length(max=256)])
    numero_oficio_origen = StringField("Número de Oficio Origen", validators=[Optional(), Length(max=256)])
    tipo_juicio_asunto_delitos = StringField("Tipo de Juicio Asunto Delitos", validators=[DataRequired(), Length(max=256)])
    juez_exhortante = StringField("Juez Exhortante", validators=[Optional(), Length(max=256)])
    fojas = IntegerField("Fojas", validators=[DataRequired()])
    dias_responder = IntegerField("Días Responder", validators=[DataRequired()])
    tipo_diligenciacion_nombre = StringField("Tipo Diligenciación Nombre", validators=[Optional(), Length(max=256)])
    fecha_origen = StringField("Fecha Origen", validators=[DataRequired()])
    observaciones = TextAreaField("Observaciones", validators=[Optional(), Length(max=1024)])
    folio_seguimiento = StringField("Folio de Seguimiento", validators=[Optional(), Length(max=256)])
    estado = StringField("Estado")
    crear = SubmitField("Crear")

    def __init__(self, *args, **kwargs):
        """Inicializar y cargar opciones para materia"""
        super().__init__(*args, **kwargs)
        self.materia.choices = [(m.id, m.nombre) for m in Materia.query.filter_by(estatus="A").order_by(Materia.nombre).all()]


class ExhExhortoEditForm(FlaskForm):
    """Formulario Edit Exhorto"""

    exhorto_origen_id = StringField("Exhorto Origen ID", validators=[DataRequired(), Length(max=128)])
    estado_destino = SelectField(
        "Estado Destino", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    municipio_destino = SelectField(
        "Municipio Destino", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    materia = SelectField("Materia", coerce=int, validators=[DataRequired()])
    estado_origen = SelectField(
        "Estado Origen", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    municipio_origen = SelectField(
        "Municipio Origen", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    juzgado_origen = SelectField("Juzgado Origen", coerce=int, validate_choice=False, validators=[DataRequired()])
    numero_expediente_origen = StringField("Número de Expediente Origen", validators=[DataRequired(), Length(max=256)])
    numero_oficio_origen = StringField("Número de Oficio Origen", validators=[Optional(), Length(max=256)])
    tipo_juicio_asunto_delitos = StringField("Tipo de Juicio Asunto Delitos", validators=[DataRequired(), Length(max=256)])
    juez_exhortante = StringField("Juez Exhortante", validators=[Optional(), Length(max=256)])
    fojas = IntegerField("Fojas", validators=[DataRequired()])
    dias_responder = IntegerField("Días Responder", validators=[DataRequired()])
    tipo_diligenciacion_nombre = StringField("Tipo Diligenciación Nombre", validators=[Optional(), Length(max=256)])
    fecha_origen = StringField("Fecha Origen", validators=[DataRequired()])
    observaciones = TextAreaField("Observaciones", validators=[Optional(), Length(max=1024)])
    remitente = StringField("Remitente")
    exh_area = SelectField("Área", coerce=int, validators=[DataRequired()])
    folio_seguimiento = StringField("Folio de Seguimiento", validators=[Optional(), Length(max=256)])
    distrito = SelectField("Distrito", choices=None, validate_choice=False)  # Las opciones se agregan con JS
    autoridad = SelectField(
        "Autoridad", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    numero_exhorto = StringField("Número de Exhorto", validators=[Optional(), Length(max=256)])
    estado = StringField("Estado")  # Read only
    guardar = SubmitField("Guardar")

    def __init__(self, *args, **kwargs):
        """Inicializar y cargar opciones para materia y exh_area"""
        super().__init__(*args, **kwargs)
        self.materia.choices = [(m.id, m.nombre) for m in Materia.query.filter_by(estatus="A").order_by(Materia.nombre).all()]
        self.exh_area.choices = [
            (m.id, m.clave + " - " + m.nombre) for m in ExhArea.query.filter_by(estatus="A").order_by(ExhArea.clave).all()
        ]


class ExhExhortoTransferForm(FlaskForm):
    """Formulario Transferir Exhorto"""

    exh_area = SelectField("Área", coerce=int, validators=[DataRequired()])
    distrito = SelectField(
        "Distrito", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    autoridad = SelectField(
        "Autoridad", choices=None, validate_choice=False, validators=[DataRequired()]
    )  # Las opciones se agregan con JS
    transferir = SubmitField("Transferir")

    def __init__(self, *args, **kwargs):
        """Inicializar y cargar opciones para materia y exh_area"""
        super().__init__(*args, **kwargs)
        self.exh_area.choices = [
            (m.id, m.clave + " - " + m.nombre) for m in ExhArea.query.filter_by(estatus="A").order_by(ExhArea.clave).all()
        ]


class ExhExhortoProcessForm(FlaskForm):
    """Formulario Procesar Exhorto"""

    numero_exhorto = StringField("Número de Exhorto", validators=[Optional(), Length(max=256)])
    procesar = SubmitField("Procesar")


class ExhExhortoRefuseForm(FlaskForm):
    """Formulario Rechazar Exhorto"""

    archivo = FileField("Archivo PDF", validators=[FileRequired()])
    rechazar = SubmitField("Rechazar")


class ExhExhortoDiligenceForm(FlaskForm):
    """Formulario Diligenciar Exhorto"""

    archivo = FileField("Archivo PDF", validators=[FileRequired()])
    diligenciar = SubmitField("Diligenciar")


class ExhExhortoResponseForm(FlaskForm):
    """Formulario Contestar Exhorto"""

    archivo = FileField("Archivo PDF", validators=[FileRequired()])
    contestar = SubmitField("Contestar")
