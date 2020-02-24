from flask import request
from flask_restx import Resource

from ..util.dto import RecursoBasicoDTO
from ..service.recurso_basico_service import create_recurso_basico, get_recurso_basico_by_id, get_recurso_basico_list

api = RecursoBasicoDTO.api
_recurso_basico = RecursoBasicoDTO.recurso_basico

@api.route('/')
class RecursoBasicoList(Resource):
    @api.doc('Lista de recurso_basico')
    @api.marshal_list_with(_recurso_basico, envelope='data')
    def get(self):
        return get_recurso_basico_list()

    @api.response(201, 'recurso_basico Unitario creado')
    @api.doc('Crear recurso_basico Unitario')
    @api.expect(_recurso_basico, validate=True)
    def post(self):
        data = request.json
        return create_recurso_basico(data)

@api.route('/<id>')
@api.param('id', 'Identificador del recurso_basico')
@api.response(404, 'recurso_basico Unitario no encontrado')
class RecursoBasico(Resource):
    @api.doc('Obtener recurso_basico Unitario')
    @api.marshal_with(_recurso_basico)
    def get(self, id):
        recurso_basico = get_recurso_basico_by_id(id)
        if not recurso_basico:
            api.abort(404)
        else:
            return recurso_basico
