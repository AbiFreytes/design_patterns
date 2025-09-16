from paprika import *
from articulo import Articulo
from typing import Set
from articulo_manufacturado_detalle import ArticuloDetalle
from unidad_medida import UnidadMedida
from imagen import Imagen

@data
class ArticuloManufacturado(Articulo):
    denominacion: str
    precioVenta: float
    id: int
    imagen: Set[Imagen]
    unidad_medida: UnidadMedida

    # atributos propios
    descripcion: str
    tiempoEstimadoMinutos: int
    preparacion: str
    detalles: Set[ArticuloDetalle]

    def calcular_precio_final(self):
        pass
