from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any


# --------- Jerarquía de PRODUCTO ---------
class Libro(ABC):
    """Interfaz del producto que crea el Factory Method."""

    titulo: str
    autor: str

    @abstractmethod
    def tipo(self) -> str:
        ...

    @abstractmethod
    def info_entrega(self) -> str:
        ...

    def descripcion(self) -> str:
        return f"{self.titulo} — {self.autor} [{self.tipo()}]"


@dataclass(frozen=True)
class LibroFisico(Libro):
    titulo: str
    autor: str
    peso_kg: float

    def tipo(self) -> str:
        return "FISICO"

    def info_entrega(self) -> str:
        return f"Enviar por correo (peso {self.peso_kg:.2f} kg)"


@dataclass(frozen=True)
class LibroDigital(Libro):
    titulo: str
    autor: str
    formato: str  # e.g., PDF/EPUB/MOBI
    tamanio_mb: float

    def tipo(self) -> str:
        return "DIGITAL"

    def info_entrega(self) -> str:
        return f"Descarga {self.formato} ({self.tamanio_mb:.1f} MB)"


# --------- Jerarquía de CREATOR ---------
class TipoLibro(str, Enum):
    FISICO = "fisico"
    DIGITAL = "digital"


class LogisticaLibro(ABC):
    """
    CREADOR ABSTRACTO.
    Define el Factory Method `crear_libro`, que las subclases implementan
    para devolver el PRODUCTO correcto (LibroFisico o LibroDigital).
    """

    @abstractmethod
    def crear_libro(self, **kwargs: Any) -> Libro:
        ...

    # Helper para selección dinámica del creador según config/entrada
    @staticmethod
    def desde_tipo(tipo: str | TipoLibro) -> "LogisticaLibro":
        t = TipoLibro(tipo)
        if t is TipoLibro.FISICO:
            return LogisticaFisica()
        if t is TipoLibro.DIGITAL:
            return LogisticaDigital()
        # Enum valida; este else no se ejecuta, pero se deja por claridad:
        raise ValueError(f"Tipo de libro no soportado: {tipo!r}")


class LogisticaFisica(LogisticaLibro):
    """CREADOR CONCRETO para libros físicos."""

    def crear_libro(self, **kwargs: Any) -> Libro:
        try:
            return LibroFisico(
                titulo=str(kwargs["titulo"]),
                autor=str(kwargs["autor"]),
                peso_kg=float(kwargs["peso_kg"]),
            )
        except KeyError as e:
            raise ValueError(f"Falta parámetro requerido para libro físico: {e.args[0]}") from e


class LogisticaDigital(LogisticaLibro):
    """CREADOR CONCRETO para libros digitales."""

    def crear_libro(self, **kwargs: Any) -> Libro:
        try:
            return LibroDigital(
                titulo=str(kwargs["titulo"]),
                autor=str(kwargs["autor"]),
                formato=str(kwargs["formato"]),
                tamanio_mb=float(kwargs["tamanio_mb"]),
            )
        except KeyError as e:
            raise ValueError(f"Falta parámetro requerido para libro digital: {e.args[0]}") from e
