from paprika import data
from localidad import Localidad

@data
class Domicilio:
    calle: str
    numero: str
    cp: int
    localidad: Localidad
