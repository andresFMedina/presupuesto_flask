from app.main import db
from app.main.model.item import Item


def create_item(data):
    item = Item(
        proyecto_id=data['proyecto_id'],
        codigo=data['codigo'],
        descripcion=data['descripcion'],
        unidad=data['unidad'],
        cantidad=data['cantidad'],
        aporte=data['aporte'],
        detalles=data['detalles'],
        valor_unitario=data['valor_unitario'],
        numero_capitulo=data['numero_capitulo'],
        costoManoObra=data['costoManoObra'],
        costoEquipo=data['costoEquipo'],
        costoMateriales=data['costoMateriales']
    )

    save_changes(item)

    response_object = {
        'status': 'success',
        'message': 'Created',
        'model': item
    }
    return response_object


def get_item_list():
    return Item.query.all()


def get_item_by_id(id):
    return Item.query.filter(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()