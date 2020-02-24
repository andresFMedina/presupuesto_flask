from app.main import db
from app.main.model.recurso_basico import RecursoBasico


def create_recurso_basico(data):
    recurso_basico = RecursoBasico(
        codigo=data['codigo'],
        descripcion=data['descripcion'],
        unidad=data['unidad'],
        grupo=data['grupo'],
        precio=data['precio']
    )

    save_changes(recurso_basico)

    response_object = {
        'status': 'success',
        'message': 'Created',
        'model': recurso_basico
    }
    return response_object


def get_recurso_basico_list():
    return RecursoBasico.query.all()


def get_recurso_basico_by_id(id):
    return RecursoBasico.query.filter(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()