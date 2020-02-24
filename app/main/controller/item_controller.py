from flask import request
from flask_restx import Resource

from ..util.dto import ItemDTO
from ..service.item_service import create_item, get_item_by_id, get_item_list

api = ItemDTO.api
_item = ItemDTO.item

@api.route('/')
class ItemList(Resource):
    @api.doc('Lista de item')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        return get_item_list()

    @api.response(201, 'item  creado')
    @api.doc('Crear item ')
    @api.expect(_item, validate=True)
    def post(self):
        data = request.json
        return create_item(data)

@api.route('/<id>')
@api.param('id', 'Identificador del item')
@api.response(404, 'item  no encontrado')
class Item(Resource):
    @api.doc('Obtener item ')
    @api.marshal_with(_item)
    def get(self, id):
        item = get_item_by_id(id)
        if not item:
            api.abort(404)
        else:
            return item
