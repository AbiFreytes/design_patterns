from paprika import *
from articulo import Articulo
from typing import Set
from articulo_insumo import ArticuloInsumo

@data
class ArticuloDetalle(Articulo):
    id: int
    cantidad: int
    articulo_insumo: ArticuloInsumo

    def calcular_precio_final(self):
        pass