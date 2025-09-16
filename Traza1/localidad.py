# localidad.py
from paprika import *
from provincia import Provincia

@data
class Localidad:
    nombre: str
    provincia: Provincia

