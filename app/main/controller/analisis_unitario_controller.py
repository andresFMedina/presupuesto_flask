from flask import request
from flask_restx import Resource

from ..util.dto import AnalisisUnitarioDTO
from ..service.analisis_unitario_service import create_analisis_unitario, get_analisis_by_id, get_analisis_list

api = AnalisisUnitarioDTO.api
_analisis_unitario = AnalisisUnitarioDTO.analisis_unitario

@api.route('/')
class AnalisisUnitarioList(Resource):
    @api.doc('Lista de analisis unitarios')
    @api.marshal_list_with(_analisis_unitario, envelope='data')
    def get(self):
        return get_analisis_list()

    @api.response(201, 'Analisis Unitario creado')
    @api.doc('Crear Analisis Unitario')
    @api.expect(_analisis_unitario, validate=True)
    def post(self):
        data = request.json
        return create_analisis_unitario(data)

@api.route('/<id>')
@api.param('id', 'Identificador del Analisis Unitario')
@api.response(404, 'Analisis Unitario no encontrado')
class AnalisisUnitario(Resource):
    @api.doc('Obtener Analisis Unitario')
    @api.marshal_with(_analisis_unitario)
    def get(self, id):
        analisis = get_analisis_by_id(id)
        if not analisis:
            api.abort(404)
        else:
            return analisis
