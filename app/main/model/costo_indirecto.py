from .. import db


class CostoIndirecto(db.Model):
    __tablename__ = "costo_indirecto"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50), nullable=False)
    porcentaje = db.Column(db.Float, nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)