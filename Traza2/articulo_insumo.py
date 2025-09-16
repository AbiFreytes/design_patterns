from paprika import *
from articulo import Articulo

@data
class ArticuloInsumo(Articulo):
    denominacion: str

    precioCompra: float
    stockActual: int
    stockMaximo: int
    esParaElaborar: bool

    def calcular_precio_final(self):
        pass