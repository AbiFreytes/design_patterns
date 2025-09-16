from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping, Dict, Optional


@dataclass(frozen=True, slots=True)
class Usuario:
    """
    Objeto inmutable construido vía Builder.
    - `preferencias` se expone como un mapeo de solo lectura (una vista inmutable) aun cuando internamente se haya construido con un dict mutable durante el armado con el builder.
    """
    username: str
    email: Optional[str] = None
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    preferencias: Mapping[str, Any] = field(default_factory=lambda: MappingProxyType({}))

    def __post_init__(self) -> None:
        # Aseguramos inmutabilidad de `preferencias` aunque se pase un dict.
        object.__setattr__(self, "preferencias", MappingProxyType(dict(self.preferencias)))

    # Fábrica estática para iniciar el builder
    @staticmethod
    def builder(username: str) -> "Usuario.Builder":
        return Usuario.Builder(username)

    # ----------------------- BUILDER -----------------------
    class Builder:
        """
        Builder encadenable:
            (Usuario.builder("celi")
                    .email("celi@example.com")
                    .nombre("Celina")
                    .preferencia("tema", "oscuro")
                    .build())
        """
        def __init__(self, username: str) -> None:
            self._username = username.strip()
            self._email = None
            self._nombre = None
            self._telefono = None
            self._direccion = None
            self._preferencias: dict[str, Any] = {}   # <- existe el dict interno

        # ----- setters encadenables -----
        def email(self, email: str) -> "Usuario.Builder":
            self._email = email.strip()
            return self

        def nombre(self, nombre: str) -> "Usuario.Builder":
            self._nombre = nombre.strip()
            return self

        def telefono(self, telefono: str) -> "Usuario.Builder":
            self._telefono = telefono.strip()
            return self

        def direccion(self, direccion: str) -> "Usuario.Builder":
            self._direccion = direccion.strip()
            return self

        def preferencia(self, clave: str, valor: Any) -> "Usuario.Builder":
            self._preferencias[clave] = valor
            return self

        def preferencias(self, prefs: Mapping[str, Any]) -> "Usuario.Builder":
            self._preferencias.update(dict(prefs))
            return self

        def build(self) -> "Usuario":
            if not self._username:
                raise ValueError("username es obligatorio")

            if self._email is not None:
                e = self._email
                if "@" not in e or e.startswith("@") or e.endswith("@"):
                    raise ValueError(f"email inválido: {e!r}")

            if self._telefono is not None:
                digits = "".join(ch for ch in self._telefono if ch.isdigit())
                if len(digits) < 7:
                    raise ValueError("telefono inválido (se requieren al menos 7 dígitos)")
                self._telefono = digits

            from types import MappingProxyType
            return Usuario(
                username=self._username,
                email=self._email,
                nombre=self._nombre,
                telefono=self._telefono,
                direccion=self._direccion,
                preferencias=MappingProxyType(dict(self._preferencias)),
    )
