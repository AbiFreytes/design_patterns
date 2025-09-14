from __future__ import annotations

from typing import Any, Dict, List

from .implementation import AbstractFactory


def main() -> None:
    # "Logins" simulados con distintos tipos de usuario
    sesiones: List[Dict[str, Any]] = [
        {"usuario": "ana", "tipo": "admin"},
        {"usuario": "carlos", "tipo": "usuario"},
        {"usuario": "sofia", "tipo": "usuario"},
        {"usuario": "root", "tipo": "admin"},
    ]

    # Pedido de ejemplo para mostrar integración con MetodoEnvio
    peso_kg = 0.8
    distancia_km = 120

    for s in sesiones:
        fabrica = AbstractFactory.desde_tipo(s["tipo"])
        ui = fabrica.crear_ui()
        envio = fabrica.crear_envio()

        print(f"\n=== Sesión de {s['usuario']} ({s['tipo']}) ===")
        print(ui.render_home())
        print("Permisos:", ", ".join(ui.permisos()))
        print(f"Envío: {envio.nombre()} → costo ${envio.calcular_costo(peso_kg, distancia_km)}; ETA {envio.tiempo_estimado(distancia_km)}")

    print("\n✔ Consistencia garantizada: cada fábrica entrega UI + Envío de la MISMA familia.")


if __name__ == "__main__":
    main()
