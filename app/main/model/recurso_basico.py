from .. import db


class RecursoBasico(db.Model):
    __tablename__ = "recurso_basico"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True)
    descripcion = db.Column(db.String(100))
    unidad = db.Column(db.String(5))
    grupo = db.Column(db.String(5))
    precio = db.Column(db.Float)
    fecha = db.Column(db.Date, nullable=True)