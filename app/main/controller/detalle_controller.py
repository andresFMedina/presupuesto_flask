from flask import request
from flask_restx import Resource

from ..util.dto import DetalleDTO
from ..service.detalle_service import create_detalle, get_detalle_by_id, get_detalle_list

api = DetalleDTO.api
_detalle = DetalleDTO.detalle

@api.route('/')
class DetalleList(Resource):
    @api.doc('Lista de Detalles')
    @api.marshal_list_with(_detalle, envelope='data')
    def get(self):
        return get_detalle_list()

    @api.response(201, 'Detalle creado')
    @api.doc('Crear Detalle')
    @api.expect(_detalle, validate=True)
    def post(self):
        data = request.json
        return create_detalle(data)

@api.route('/<id>')
@api.param('id', 'Identificador del Detalle')
@api.response(404, 'Detalle no encontrado')
class Detalle(Resource):
    @api.doc('Obtener Detalle')
    @api.marshal_with(_detalle)
    def get(self, id):
        analisis = get_detalle_by_id(id)
        if not analisis:
            api.abort(404)
        else:
            return analisis
