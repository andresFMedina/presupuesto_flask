from .. import db


class AnalisisUnitario(db.Model):
    __tablename_ = "analisis_unitario"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    unidad = db.Column(db.String(5), nullable=False)
    grupo = db.Column(db.String(10), nullable=True)
    clasificacion = db.Column(db.String(20), nullable=True)
    valorUnitario = db.Column(db.Float, nullable=False)
    detalles = db.relationship('Detalle', backref='analisis_unitario', lazy=True)
    costoMateriales = db.Column(db.Float, nullable=False)
    costoEquipo = db.Column(db.Float, nullable=False)
    costoManoObra = db.Column(db.Float, nullable=False)
