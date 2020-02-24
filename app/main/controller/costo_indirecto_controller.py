from flask import request
from flask_restx import Resource

from ..util.dto import CostoIndirectoDTO
from ..service.costo_indirecto_service import create_costo_indirecto, get_costo_indirecto_by_id, \
    get_costo_indirecto_list

api = CostoIndirectoDTO.api
_costo_indirecto = CostoIndirectoDTO.costo_indirecto


@api.route('/')
class CostoIndirectoList(Resource):
    @api.doc('Lista de costo_indirecto')
    @api.marshal_list_with(_costo_indirecto, envelope='data')
    def get(self):
        return get_costo_indirecto_list()

    @api.response(201, 'costo_indirecto creado')
    @api.doc('Crear costo_indirecto ')
    @api.expect(_costo_indirecto, validate=True)
    def post(self):
        data = request.json
        return create_costo_indirecto(data)


@api.route('/<id>')
@api.param('id', 'Identificador del costo_indirecto ')
@api.response(404, 'costo_indirecto  no encontrado')
class CostoIndirecto(Resource):
    @api.doc('Obtener costo_indirecto')
    @api.marshal_with(_costo_indirecto)
    def get(self, id):
        costo_indirecto = get_costo_indirecto_by_id(id)
        if not costo_indirecto:
            api.abort(404)
        else:
            return costo_indirecto
