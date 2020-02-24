from .. import db


class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)

    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    unidad = db.Column(db.String(5), nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    aporte = db.Column(db.Float, nullable=False)
    detalles = db.relationship('Detalle', backref='item', lazy=True)
    valor_unitario = db.Column(db.Float, nullable=False)
    numero_capitulo = db.Column(db.Integer, nullable=True)
    capitulo_id = db.Column(db.Integer, db.ForeignKey('capitulo.id'), nullable=True)
    costoMateriales = db.Column(db.Float, nullable=False)
    costoEquipo = db.Column(db.Float, nullable=False)
    costoManoObra = db.Column(db.Float, nullable=False)
