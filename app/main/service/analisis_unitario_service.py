from app.main import db
from app.main.model.analisis_unitario import AnalisisUnitario


def create_analisis_unitario(data):
    analisis_unitario = AnalisisUnitario(
        descripcion=data['descripcion'],
        codigo=data['codigo'],
        unidad=data['unidad'],
        grupo=data['grupo'],
        valorUnitario=data['valorUnitario'],
        costoMateriales=data['costoMateriales'],
        costoEquipo=data['costoEquipo'],
        costoManoObra=data['costoManoObra']
    )
    save_changes(analisis_unitario)
    response_object = {
        'status': 'success',
        'message': 'Analisis Creado',
        'model': analisis_unitario
    }

    return response_object


def get_analisis_list():
    return AnalisisUnitario.query.all()


def get_analisis_by_id(id):
    return AnalisisUnitario.query.filter_by(id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
