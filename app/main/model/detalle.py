from .. import db


class Detalle(db.Model):
    __tablename__ = "detalle"

    id = db.Column(db.Integer, primary_key=True)
    analisis_unitario_id = db.Column(db.Integer, db.ForeignKey('analisis_unitario.id'), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)
    rendimiento = db.Column(db.Float, nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    unidad = db.Column(db.String(5), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    grupo = db.Column(db.String(5), nullable=True)
    desperdicio = db.Column(db.Float, nullable=False)
    detalleDe = db.Column(db.String(10), nullable=False)
    subTotal = db.Column(db.Float, nullable=False)