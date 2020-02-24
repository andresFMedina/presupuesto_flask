from app.main import db
from app.main.model.capitulo import Capitulo


def create_capitulo(data):
    capitulo = Capitulo(
        numero=data['numero'],
        descripcion=data['descripcion'],
        proyecto_id=data['proyecto_id'],
        subtotal=data['subtotal'],
        items=data['items']
    )

    save_changes(capitulo)

    response_object = {
        'status': 'success',
        'message': 'Created',
        'model': capitulo
    }
    return response_object

def get_capitulo_list():
    return Capitulo.query.all()


def get_capitulo_by_id(id):
    return Capitulo.query.filter(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()