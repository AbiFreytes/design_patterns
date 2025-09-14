from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


# ===================== PRODUCTOS (interfaces) =====================

class InterfazUI(ABC):
    """Contrato para las UIs según tipo de usuario."""

    @abstractmethod
    def nombre(self) -> str: ...

    @abstractmethod
    def render_home(self) -> str: ...

    @abstractmethod
    def permisos(self) -> list[str]: ...


class MetodoEnvio(ABC):
    """Contrato para los métodos de envío asociados a cada familia."""

    @abstractmethod
    def nombre(self) -> str: ...

    @abstractmethod
    def calcular_costo(self, peso_kg: float, distancia_km: int) -> float: ...

    @abstractmethod
    def tiempo_estimado(self, distancia_km: int) -> str: ...


# ===================== PRODUCTOS CONCRETOS =====================

@dataclass(frozen=True)
class AdminUI(InterfazUI):
    tema: str = "oscuro"

    def nombre(self) -> str:
        return "AdminUI"

    def render_home(self) -> str:
        return f"[{self.nombre()}] Dashboard con métricas y gestión — tema {self.tema}"

    def permisos(self) -> list[str]:
        return ["USUARIOS_CRUD", "CATALOGO_CRUD", "REPORTES_VER", "CONFIG_SISTEMA"]


@dataclass(frozen=True)
class UsuarioUI(InterfazUI):
    tema: str = "claro"

    def nombre(self) -> str:
        return "UsuarioUI"

    def render_home(self) -> str:
        return f"[{self.nombre()}] Inicio con recomendaciones — tema {self.tema}"

    def permisos(self) -> list[str]:
        return ["CATALOGO_VER", "COMPRAR", "HISTORIAL_VER"]


@dataclass(frozen=True)
class EnvioNormal(MetodoEnvio):
    base: float = 3.0
    por_km: float = 0.5
    por_kg: float = 1.0

    def nombre(self) -> str:
        return "EnvioNormal"

    def calcular_costo(self, peso_kg: float, distancia_km: int) -> float:
        return round(self.base + self.por_km * distancia_km + self.por_kg * peso_kg, 2)

    def tiempo_estimado(self, distancia_km: int) -> str:
        # ~60 km/día como referencia simple
        dias = max(1, (distancia_km + 59) // 60)
        return f"{dias} día(s) hábiles"


@dataclass(frozen=True)
class EnvioExpress(MetodoEnvio):
    base: float = 7.0
    por_km: float = 0.9
    por_kg: float = 1.2
    aceleracion: float = 2.5  # más rápido

    def nombre(self) -> str:
        return "EnvioExpress"

    def calcular_costo(self, peso_kg: float, distancia_km: int) -> float:
        return round(self.base + self.por_km * distancia_km + self.por_kg * peso_kg, 2)

    def tiempo_estimado(self, distancia_km: int) -> str:
        # Express: más rápido que normal
        horas = max(6, int(distancia_km / (60 * self.aceleracion) * 24))
        return f"{horas} h aprox."


# ===================== FABRICAS (abstracta y concretas) =====================

class TipoUsuario(str, Enum):
    ADMIN = "admin"
    USUARIO = "usuario"


class AbstractFactory(ABC):
    """Crea familias de objetos compatibles (UI + Envío) para cada tipo de usuario."""

    @abstractmethod
    def crear_ui(self) -> InterfazUI: ...

    @abstractmethod
    def crear_envio(self) -> MetodoEnvio: ...

    @staticmethod
    def desde_tipo(tipo: str | TipoUsuario) -> "AbstractFactory":
        t = TipoUsuario(tipo)
        if t is TipoUsuario.ADMIN:
            return AdminFactory()
        if t is TipoUsuario.USUARIO:
            return UsuarioFactory()
        raise ValueError(f"Tipo de usuario no soportado: {tipo!r}")


class AdminFactory(AbstractFactory):
    """Familia 'Admin': UI administrativa + envío express (ej. urgencias operativas)."""

    def crear_ui(self) -> InterfazUI:
        return AdminUI()

    def crear_envio(self) -> MetodoEnvio:
        return EnvioExpress()


class UsuarioFactory(AbstractFactory):
    """Familia 'Usuario': UI de cliente final + envío normal."""

    def crear_ui(self) -> InterfazUI:
        return UsuarioUI()

    def crear_envio(self) -> MetodoEnvio:
        return EnvioNormal()
