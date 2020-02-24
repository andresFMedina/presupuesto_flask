from flask import request
from flask_restx import Resource

from ..util.dto import ProyectoDTO
from ..service.proyecto_service import save_new_project, get_all_projects, get_project_by_id

api = ProyectoDTO.api
_proyecto = ProyectoDTO.proyecto


@api.route('/')
class ProyectoList(Resource):
    @api.doc('Lista de proyectos')
    @api.marshal_list_with(_proyecto, envelope='data')
    def get(self):
        return get_all_projects()

    @api.response(201, 'Proyecto creado')
    @api.doc('Crear Proyecto')
    @api.expect(_proyecto, validate=True)
    @api.marshal_with(_proyecto, envelope='data')
    def post(self):
        data = request.json
        return save_new_project(data)

@api.route('/<id>')
@api.param('id', 'Identificador del proyecto')
@api.response(404, 'Proyecto no encontrado')
class Proyecto(Resource):
    @api.doc('Obtener proyecto')
    @api.marshal_with(_proyecto)
    def get(self, id):
        proyecto = get_project_by_id(id)
        if not proyecto:
            api.abort(404)
        else:
            return proyecto