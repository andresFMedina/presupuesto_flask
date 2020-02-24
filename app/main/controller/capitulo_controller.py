from flask import request
from flask_restx import Resource

from ..util.dto import CapituloDTO
from ..service.capitulo_service import create_capitulo, get_capitulo_by_id, get_capitulo_list

api = CapituloDTO.api
_capitulo = CapituloDTO.capitulo


@api.route('/')
class CapituloList(Resource):
    @api.doc('Lista de capitulo')
    @api.marshal_list_with(_capitulo, envelope='data')
    def get(self):
        return get_capitulo_list()

    @api.response(201, 'capitulo creado')
    @api.doc('Crear capitulo')
    @api.expect(_capitulo, validate=True)
    def post(self):
        data = request.json
        return create_capitulo(data)


@api.route('/<id>')
@api.param('id', 'Identificador del capitulo')
@api.response(404, 'capitulo no encontrado')
class Capitulo(Resource):
    @api.doc('Obtener capitulo')
    @api.marshal_with(_capitulo)
    def get(self, id):
        capitulo = get_capitulo_by_id(id)
        if not capitulo:
            api.abort(404)
        else:
            return capitulo
