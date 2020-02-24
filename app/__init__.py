from flask_restx import Api
from flask import Blueprint

from .main.controller.proyecto_controller import api as proyecto_ns
from .main.controller.analisis_unitario_controller import api as analisis_ns
from .main.controller.detalle_controller import api as detalle_ns
from .main.controller.capitulo_controller import api as capitulo_ns
from .main.controller.costo_indirecto_controller import api as costo_ns
from .main.controller.item_controller import api as item_ns
from .main.controller.recurso_basico_controller import api as recurso_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title="Rest Flask",
          version='1.0',
          description='Presupuesto'
          )

api.add_namespace(proyecto_ns, path='/proyecto')
api.add_namespace(analisis_ns, path='/analisis')
api.add_namespace(detalle_ns, path='/detalle')
api.add_namespace(capitulo_ns, path='/capitulo')
api.add_namespace(item_ns, path='/item')
api.add_namespace(costo_ns, path='/costo')
api.add_namespace(recurso_ns, path='/recurso')
