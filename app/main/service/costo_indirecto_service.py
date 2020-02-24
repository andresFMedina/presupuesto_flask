from app.main import db
from app.main.model.costo_indirecto import CostoIndirecto


def create_costo_indirecto(data):
    costo_indirecto = CostoIndirecto(
        numero=data['numero'],
        descripcion=data['descripcion'],
        proyecto_id=data['proyecto_id'],
        porcentaje=data['porcentaje'],
    )

    save_changes(costo_indirecto)

    response_object = {
        'status': 'success',
        'message': 'Created',
        'model': costo_indirecto
    }
    return response_object


def get_costo_indirecto_list():
    return CostoIndirecto.query.all()


def get_costo_indirecto_by_id(id):
    return CostoIndirecto.query.filter(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()