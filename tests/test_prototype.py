from datetime import datetime, timedelta

from patrones.prototype.implementation import Libro, Usuario, Prestamo


def make_base() -> Prestamo:
    return Prestamo(
        libro=Libro("Clean Architecture", "Robert C. Martin", etiquetas=["arquitectura"]),
        usuario=Usuario("celina", preferencias={"idioma": "es"}),
        fecha_inicio=datetime(2025, 9, 13),
        fecha_fin=datetime(2025, 9, 20),
        notas=["Retiro en mostrador"],
    )


def test_clone_returns_new_instance_and_types():
    prot = make_base()
    c = prot.clone()  # deep por defecto
    assert c is not prot
    assert isinstance(c.libro, Libro)
    assert isinstance(c.usuario, Usuario)


def test_deep_clone_independence():
    prot = make_base()
    c = prot.clone()  # deep
    # Mutaciones en el clon
    c.libro.titulo = "Design Patterns"
    c.libro.etiquetas.append("urgente")
    c.usuario.preferencias["tema"] = "oscuro"
    c.notas.append("Recordatorio por email")

    # El prototipo NO cambia
    assert prot.libro.titulo == "Clean Architecture"
    assert "urgente" not in prot.libro.etiquetas
    assert "tema" not in prot.usuario.preferencias
    assert "Recordatorio por email" not in prot.notas

    # Y las referencias internas son distintas
    assert c.libro is not prot.libro
    assert c.usuario is not prot.usuario
    assert c.notas is not prot.notas


def test_shallow_clone_shares_nested():
    prot = make_base()
    c = prot.clone(deep=False)  # shallow
    # Mutaciones en estructuras mutables
    c.libro.etiquetas.append("compartida")
    c.notas.append("shallow")

    # Se reflejan en el prototipo por compartir referencias
    assert "compartida" in prot.libro.etiquetas
    assert "shallow" in prot.notas

    # Y las referencias son exactamente las mismas
    assert c.libro is prot.libro
    assert c.usuario is prot.usuario
    assert c.notas is prot.notas


def test_overrides_apply():
    prot = make_base()
    nueva_fin = prot.fecha_fin + timedelta(days=5)
    nuevo_usuario = Usuario("juan", preferencias={"idioma": "es"})
    c = prot.clone(fecha_fin=nueva_fin, usuario=nuevo_usuario)  # deep por defecto

    assert c.fecha_fin == nueva_fin
    assert c.usuario.username == "juan"
    # El prototipo sigue intacto
    assert prot.fecha_fin != nueva_fin
    assert prot.usuario.username == "celina"
