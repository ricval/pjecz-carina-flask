"""
Exh Areas, vistas
"""

import json
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from lib.datatables import get_datatable_parameters, output_datatable_json
from lib.safe_string import safe_string, safe_message

from carina.blueprints.bitacoras.models import Bitacora
from carina.blueprints.modulos.models import Modulo
from carina.blueprints.permisos.models import Permiso
from carina.blueprints.usuarios.decorators import permission_required
from carina.blueprints.exh_areas.models import ExhArea

MODULO = "EXH AREAS"

exh_areas = Blueprint("exh_areas", __name__, template_folder="templates")


@exh_areas.before_request
@login_required
@permission_required(MODULO, Permiso.VER)
def before_request():
    """Permiso por defecto"""


@exh_areas.route("/exh_areas/datatable_json", methods=["GET", "POST"])
def datatable_json():
    """DataTable JSON para listado de Areas"""
    # Tomar parámetros de Datatables
    draw, start, rows_per_page = get_datatable_parameters()
    # Consultar
    consulta = ExhArea.query
    # Primero filtrar por columnas propias
    if "estatus" in request.form:
        consulta = consulta.filter_by(estatus=request.form["estatus"])
    else:
        consulta = consulta.filter_by(estatus="A")
    # Ordenar y paginar
    registros = consulta.order_by(ExhArea.clave).offset(start).limit(rows_per_page).all()
    total = consulta.count()
    # Elaborar datos para DataTable
    data = []
    for resultado in registros:
        data.append(
            {
                "detalle": {
                    "clave": resultado.clave,
                    "url": url_for("exh_areas.detail", exh_area_id=resultado.id),
                },
                "nombre": resultado.nombre,
            }
        )
    # Entregar JSON
    return output_datatable_json(draw, total, data)


@exh_areas.route("/exh_areas")
def list_active():
    """Listado de Areas activos"""
    return render_template(
        "exh_areas/list.jinja2",
        filtros=json.dumps({"estatus": "A"}),
        titulo="Áreas",
        estatus="A",
    )


@exh_areas.route("/exh_areas/inactivos")
@permission_required(MODULO, Permiso.ADMINISTRAR)
def list_inactive():
    """Listado de Areas inactivos"""
    return render_template(
        "exh_areas/list.jinja2",
        filtros=json.dumps({"estatus": "B"}),
        titulo="Áreas inactivas",
        estatus="B",
    )


@exh_areas.route("/exh_areas/<int:exh_area_id>")
def detail(exh_area_id):
    """Detalle de un Area"""
    exh_area = ExhArea.query.get_or_404(exh_area_id)
    return render_template("exh_areas/detail.jinja2", exh_area=exh_area)
