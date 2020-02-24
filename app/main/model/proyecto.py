from .. import db


class Proyecto(db.Model):
    __tablename__ = "proyecto"

    id = db.Column(db.Integer, primary_key=True)
    nombre_Obra = db.Column(db.String(100), nullable=False)
    contratante = db.Column(db.String(100), nullable=False)
    proponente = db.Column(db.String(100), nullable=False)
    fecha_Presentacion = db.Column(db.Date, nullable=False)
    fecha_Modificacion = db.Column(db.Date, nullable=False)
    comentarios = db.Column(db.String(255), nullable=False)
    capitulos = db.relationship('Capitulo', backref='proyecto', lazy=True)
    costos_indirectos = db.relationship('CostoIndirecto', backref='proyecto', lazy=True)
    items = db.relationship('Item', backref='proyecto', lazy=True)
