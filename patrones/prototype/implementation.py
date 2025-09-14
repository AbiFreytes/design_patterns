from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Any


# ---------- Clases anidadas para demostrar shallow vs deep ----------
@dataclass
class Libro:
    titulo: str
    autor: str
    etiquetas: list[str] = field(default_factory=list)  # mutable a propósito


@dataclass
class Usuario:
    username: str
    preferencias: dict[str, Any] = field(default_factory=dict)  # mutable a propósito


# ------------------------------- Prototype -------------------------------
@dataclass
class Prestamo:
    libro: Libro
    usuario: Usuario
    fecha_inicio: datetime
    fecha_fin: datetime
    notas: list[str] = field(default_factory=list)  # mutable a propósito

    def clone(self, *, deep: bool = True, **overrides: Any) -> "Prestamo":
        """
        Clona el préstamo.
        - deep=True (default): clona también referencias mutables (Libro, Usuario, notas, etiquetas).
        - deep=False: copia superficial (comparte referencias anidadas).
        Podés sobrescribir atributos pasando kwargs (ej.: fecha_fin=nueva_fecha).
        """
        l = deepcopy(self.libro) if deep else self.libro
        u = deepcopy(self.usuario) if deep else self.usuario
        n = deepcopy(self.notas) if deep else self.notas

        # Unificamos todos los kwargs para no pasar dos veces la misma clave a replace()
        kwargs: dict[str, Any] = {"libro": l, "usuario": u, "notas": n}
        kwargs.update(overrides)  # si vienen libro/usuario/notas, pisan a los base

        return replace(self, **kwargs)

    # Helper de presentación
    def resumen(self) -> str:
        return (
            f"[Prestamo #{id(self)}] "
            f"Libro='{self.libro.titulo}' ({self.libro.etiquetas}) | "
            f"Usuario='{self.usuario.username}' | "
            f"{self.fecha_inicio:%Y-%m-%d} → {self.fecha_fin:%Y-%m-%d} | "
            f"Notas={self.notas}"
        )
