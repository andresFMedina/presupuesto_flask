from .. import db


class Capitulo(db.Model):
    __tablename__ = "capitulo"

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    items = db.relationship('Item', backref='capitulo', lazy=True)
