from __future__ import annotations
from typing import Set, Iterable, Optional, Dict
from paprika import *
from sucursal import Sucursal

@data
class Empresa:
    id: int
    nombre: str
    cuil: int
    sucursales: Set["Sucursal"] = set()

