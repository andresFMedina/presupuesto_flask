import datetime

from app.main import db
from app.main.model.proyecto import Proyecto


def save_new_project(data):
    nuevo_proyecto = Proyecto(
        nombre_Obra=data['nombre_Obra'],
        contratante=data['contratante'],
        proponente=data['proponente'],
        fecha_Presentacion=['fecha_Presentacion'],
        fecha_Modificacion=data['fecha_Modificacion'],
        comentarios=data['comentarios']
    )

    save_changes(nuevo_proyecto)
    response_object = {
        'status': 'success',
        'message': 'Creado',
        'model': nuevo_proyecto
    }

    return response_object, 201


def get_all_projects():
    return Proyecto.query.all()


def get_project_by_id(id):
    return Proyecto.query.filter_by(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
