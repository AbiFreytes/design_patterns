from __future__ import annotations

from typing import Any, Dict, List

from .implementation import LogisticaLibro


def main() -> None:
    # "Pedidos" heterogéneos: el cliente solo conoce `tipo` y los datos;
    # la elección del creador concreto se hace en tiempo de ejecución.
    pedidos: List[Dict[str, Any]] = [
        {"tipo": "fisico", "titulo": "Clean Architecture", "autor": "Robert C. Martin", "peso_kg": 0.6},
        {"tipo": "digital", "titulo": "Design Patterns", "autor": "GoF", "formato": "EPUB", "tamanio_mb": 5.2},
        {"tipo": "fisico", "titulo": "Refactoring", "autor": "Martin Fowler", "peso_kg": 0.7},
        {"tipo": "digital", "titulo": "Effective Python", "autor": "Brett Slatkin", "formato": "PDF", "tamanio_mb": 3.8},
    ]

    for p in pedidos:
        tipo = p["tipo"]
        payload = {k: v for k, v in p.items() if k != "tipo"}

        # Selección dinámica del CREATOR según 'tipo'
        logistica = LogisticaLibro.desde_tipo(tipo)

        # Factory Method: cada creador construye el PRODUCTO adecuado
        libro = logistica.crear_libro(**payload)

        # Salida "de cliente": no necesito saber si es físico o digital
        print(f"Creado: {libro.descripcion()} → {libro.info_entrega()}")


if __name__ == "__main__":
    main()
