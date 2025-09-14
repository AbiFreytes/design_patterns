from __future__ import annotations

from datetime import datetime, timedelta

# Si ejecutás como módulo, este import relativo funciona:
from .implementation import Libro, Usuario, Prestamo
# (Si preferís Script path, cambiá por: from patrones.prototype.implementation import Libro, Usuario, Prestamo)


def main() -> None:
    # Prototipo base
    prot = Prestamo(
        libro=Libro("Clean Architecture", "Robert C. Martin", etiquetas=["arquitectura"]),
        usuario=Usuario("celina", preferencias={"idioma": "es"}),
        fecha_inicio=datetime(2025, 9, 13),
        fecha_fin=datetime(2025, 9, 20),
        notas=["Retiro en mostrador"],
    )
    print("PROTO  :", prot.resumen())

    # Clone #1 (deep por defecto): cambia usuario y fecha_fin; agrega nota y etiqueta
    p1 = prot.clone(
        usuario=Usuario("juan", preferencias={"idioma": "es"}),
        fecha_fin=prot.fecha_fin + timedelta(days=7),
    )
    p1.notas.append("Penalidad: 0")
    p1.libro.etiquetas.append("urgente")
    print("CLONE1 :", p1.resumen())

    # Clone #2 (deep): cambia libro y agrega preferencias
    p2 = prot.clone()
    p2.libro.titulo = "Design Patterns"
    p2.usuario.preferencias["tema"] = "oscuro"
    p2.notas.append("Recordatorio por email")
    print("CLONE2 :", p2.resumen())

    # Verificamos independencia del PROTOTIPO
    print("\nTras mutar clones, el prototipo sigue igual:")
    print("PROTO  :", prot.resumen())

    # (Opcional) Mostrar diferencia con copia superficial
    p_shallow = prot.clone(deep=False)
    p_shallow.libro.etiquetas.append("shallow-demo")
    print("\nShallow comparte referencias mutables (etiquetas del libro):")
    print("PROTO  :", prot.resumen())
    print("SHALLO :", p_shallow.resumen())


if __name__ == "__main__":
    main()
