from flask_restx import Namespace, fields

from ..model import detalle


class DetalleDTO():
    api = Namespace('detalle', description='Operaciones de los detalles')
    model = {
        'id': fields.Integer(),
        'analisis_unitario_id': fields.Integer(description='id del analisis unitario'),
        'item_id': fields.Integer(description='id del item'),
        'codigo': fields.String(required=True, description='codigo del detalle'),
        'descripcion': fields.String(required=True, description='descripcion del detalle'),
        'unidad': fields.String(required=True, description='unidad del detalle'),
        'precio': fields.Float(required=True, description='precio del detalle'),
        'grupo': fields.String(description='grupo del detalle'),
        'rendimiento':fields.Float(required=True,description='cantidad del detalle'),
        'subTotal': fields.Float(required=True, description='valor del detalle'),
        'detalleDe': fields.String(description='detalle de'),
        'desperdicio': fields.Float(required=True, description='desperdicio del detalle'),
    }
    detalle = api.model('detalle', model=model)


class AnalisisUnitarioDTO:
    api = Namespace('analisis_unitario', description='Operaciones de los analisis unitarios')
    analisis_unitario = api.model('analisis_unitario', {
        'id': fields.Integer(),
        'proyecto_id': fields.Integer(required=True, description='id del proyecto'),
        'codigo': fields.String(required=True, description='codigo del analisis'),
        'descripcion': fields.String(required=True, description='descripcion del analisis'),
        'unidad': fields.String(required=True, description='unidad del analisis'),
        'grupo': fields.String(description='grupo del analisis'),
        'valorUnitario': fields.Float(required=True, description='valor del analisis'),
        'detalles': fields.List(fields.Nested(DetalleDTO.detalle), description='detalles del analisis'),
        'costoMateriales': fields.Float(required=True, description='costo material del analisis'),
        'costoEquipo': fields.Float(required=True, description='costo de equipo del analisis'),
        'costoManoObra': fields.Float(required=True, description='costo de mano de obra del analisis'),
    })


class ItemDTO:
    api = Namespace('item', description='Operaciones de los items')
    item = api.model('item', {
        'id': fields.Integer(),
        'proyecto_id': fields.Integer(required=True, description='id del proyecto'),
        'codigo': fields.String(required=True, description='codigo del item'),
        'descripcion': fields.String(required=True, description='descripcion del item'),
        'unidad': fields.String(required=True, description='unidad del item'),
        'grupo': fields.String(description='grupo del item'),
        'cantidad': fields.Float(required=True, description='cantidad del item'),
        'aporte': fields.Float(required=True, description='aporte del item'),
        'valor_unitario': fields.Float(required=True, description='valor del item'),
        'detalles': fields.List(fields.Nested(DetalleDTO.detalle), description='detalles del item'),
        'numero_capitulo': fields.Integer(description='numero del item dentro del capitulo'),
        'capitulo_id': fields.Integer(description='id del capitulo'),
        'costoMateriales': fields.Float(required=True, description='costo material del item'),
        'costoEquipo': fields.Float(required=True, description='costo de equipo del item'),
        'costoManoObra': fields.Float(required=True, description='costo de mano de obra del item'),
    })


class CapituloDTO:
    api = Namespace('capitulo', description='Operaciones de los capitulos')
    capitulo = api.model('capitulo', {
        'id': fields.Integer(),
        'numero': fields.Integer(required=True, description='numero del capitulo'),
        'proyecto_id': fields.Integer(required=True, description='id del proyecto'),
        'descripcion': fields.String(required=True, description='descripcion del capitulo'),
        'subtotal': fields.Float(required=True, description='subtotal del capitulo'),
        'items': fields.List(fields.Nested(ItemDTO.item), description='items del capitulo'),
    })


class CostoIndirectoDTO:
    api = Namespace('costo_indirecto', description='Operaciones de los costos indirectos')
    costo_indirecto = api.model('costo_indirecto', {
        'id': fields.Integer(),
        'proyecto_id': fields.Integer(required=True, description='id del proyecto'),
        'descripcion': fields.String(required=True, description='descripcion del costo'),
        'porcentaje': fields.Float(required=True, description='porcentaje del costo'),
    })


class ProyectoDTO:
    api = Namespace('proyecto', description='Operaciones del Proyecto')
    proyecto = api.model('proyecto', {
        'id': fields.Integer(),
        'nombre_Obra': fields.String(required=True, description='nombre de obra'),
        'contratante': fields.String(required=True, description='nombre del contratante'),
        'proponente': fields.String(required=True, description='nombre del proponente'),
        'fecha_Presentacion': fields.Date(required=True, description='fecha de presentacion'),
        'fecha_Modificacion': fields.Date(required=True, description='fecha de ultima modificacion'),
        'comentarios': fields.String(required=True, description='comentarios del proyecto'),
    })


class RecursoBasicoDTO:
    api = Namespace('recurso_basico', description='Operaciones del Recurso Basico')
    recurso_basico = api.model('recurso_basico', {
        'id': fields.Integer(),
        'codigo': fields.String(required=True, description='codigo del recurso'),
        'descripcion': fields.String(required=True, description='descripcion del recurso'),
        'unidad': fields.String(required=True, description='unidad del recurso'),
        'grupo': fields.String(description='grupo del recurso'),
        'precio': fields.Float(required=True, description='precio del recurso')
    })
