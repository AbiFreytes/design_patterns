from paprika import *
from articulo import Articulo
from typing import Set

@data
class Categoria:
    denominacion: str
    id: int

    articulo: Set["Articulo"]