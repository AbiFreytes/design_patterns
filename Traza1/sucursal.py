from paprika import *
from datetime import time
from domicilio import Domicilio
from typing import Set, Dict, Iterable, Optional

@data
class Sucursal:
    nombre: str
    horarioApertura: time
    horarioCierre: time
    es_Casa_Matriz: bool
    domicilio: Domicilio




