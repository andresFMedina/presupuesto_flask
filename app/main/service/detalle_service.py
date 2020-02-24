from app.main import db
from app.main.model.detalle import Detalle


def create_detalle(data):
    detalle = Detalle(
        analisis_unitario_id=data['analisis_unitario_id'],
        item_id=data['item_id'],
        rendimiento=data['rendimiento'],
        codigo=data['codigo'],
        descripcion=data['descripcion'],
        unidad=data['unidad'],
        precio=data['precio'],
        grupo=data['grupo'],
        desperdicio=data['desperdicio'],
        detalleDe=data['detalleDe'],
        subTotal=data['subTotal'],
    )

    save_changes(detalle)
    response_object = {
        'status': 'success',
        'message': 'detalle creado',
        'model': detalle
    }
    return response_object


def get_detalle_list():
    return Detalle.query.all()


def get_detalle_by_id(id):
    return Detalle.query.filter(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
