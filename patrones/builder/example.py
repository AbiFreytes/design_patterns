from __future__ import annotations

from dataclasses import FrozenInstanceError

# Si ejecutás como módulo ("python -m patrones.builder.example"), este import relativo funciona.
# (Si preferís 'Script path', cambiá por: from patrones.builder.implementation import Usuario)
from .implementation import Usuario


def mostrar(u: Usuario) -> None:
    print(f"\nUsuario: {u.username}")
    if u.nombre:
        print(f"  Nombre: {u.nombre}")
    if u.email:
        print(f"  Email: {u.email}")
    if u.telefono:
        print(f"  Teléfono: {u.telefono}")
    if u.direccion:
        print(f"  Dirección: {u.direccion}")
    print(f"  Preferencias: {dict(u.preferencias)}")


def main() -> None:
    # Usuario 1: con email, nombre y una preferencia
    u1 = (
        Usuario.builder("Abril")
        .email("abril@example.com")
        .nombre("Abril Freytes")
        .preferencias({"tema": "oscuro"})
        .build()
    )


    # Usuario 2: con teléfono normalizado, dirección y varias preferencias
    u2 = (
        Usuario.builder("juan")
        .telefono("(261) 5555-1212")
        .direccion("Av. Siempre Viva 742")
        .preferencias({"notificaciones": True, "idioma": "es"})
        .build()
    )


    mostrar(u1)
    mostrar(u2)

    # Demostración rápida de inmutabilidad
    try:
        setattr(u1, "email", "otro@example.com")
    except FrozenInstanceError:
        print("Inmutabilidad: no se puede modificar un Usuario ya construido.")


if __name__ == "__main__":
    main()
