from paprika import *
from abc import ABC, abstractmethod
from typing import Set
from unidad_medida import UnidadMedida

@data
class Articulo(ABC):
    denominacion: str
    precioVenta: float
    id: int

    unidad_medida: UnidadMedida


    @abstractmethod
    def calcular_precio_final(self):
        pass