import pytest

from patrones.factory_method.implementation import (
    LibroDigital,
    LibroFisico,
    LogisticaDigital,
    LogisticaFisica,
    LogisticaLibro,
    TipoLibro,
)


def test_logistica_fisica_crea_libro_fisico():
    logistica = LogisticaFisica()
    libro = logistica.crear_libro(
        titulo="Clean Architecture",
        autor="Robert C. Martin",
        peso_kg=0.75,
    )

    assert isinstance(libro, LibroFisico)
    assert libro.tipo() == "FISICO"
    assert "FISICO" in libro.descripcion()
    assert "correo" in libro.info_entrega().lower()
    assert libro.peso_kg == pytest.approx(0.75)


def test_logistica_digital_crea_libro_digital():
    logistica = LogisticaDigital()
    libro = logistica.crear_libro(
        titulo="Design Patterns",
        autor="GoF",
        formato="EPUB",
        tamanio_mb=5.2,
    )

    assert isinstance(libro, LibroDigital)
    assert libro.tipo() == "DIGITAL"
    assert "DIGITAL" in libro.descripcion()
    assert "descarga" in libro.info_entrega().lower()
    assert libro.tamanio_mb == pytest.approx(5.2)


@pytest.mark.parametrize(
    "tipo,kwargs,expected_cls",
    [
        (
                "fisico",
                {"titulo": "Refactoring", "autor": "Martin Fowler", "peso_kg": 0.7},
                LibroFisico,
        ),
        (
                TipoLibro.FISICO,
                {"titulo": "Refactoring", "autor": "Martin Fowler", "peso_kg": 0.7},
                LibroFisico,
        ),
        (
                "digital",
                {"titulo": "Effective Python", "autor": "Brett Slatkin", "formato": "PDF", "tamanio_mb": 3.8},
                LibroDigital,
        ),
        (
                TipoLibro.DIGITAL,
                {"titulo": "Effective Python", "autor": "Brett Slatkin", "formato": "PDF", "tamanio_mb": 3.8},
                LibroDigital,
        ),
    ],
)
def test_desde_tipo_seleccion_dinamica_y_creacion(tipo, kwargs, expected_cls):
    creador = LogisticaLibro.desde_tipo(tipo)
    libro = creador.crear_libro(**kwargs)
    assert isinstance(libro, expected_cls)


def test_error_falta_parametro_en_libro_fisico():
    with pytest.raises(ValueError) as exc:
        LogisticaFisica().crear_libro(
            titulo="Algo",
            autor="Alguien",
            # falta peso_kg
        )
    assert "peso_kg" in str(exc.value)


def test_error_falta_parametro_en_libro_digital():
    with pytest.raises(ValueError) as exc:
        LogisticaDigital().crear_libro(
            titulo="Algo",
            autor="Alguien",
            formato="PDF",
            # falta tamanio_mb
        )
    assert "tamanio_mb" in str(exc.value)


def test_error_tipo_invalido_en_desde_tipo():
    with pytest.raises(ValueError):
        LogisticaLibro.desde_tipo("audiolibro")  # no soportado
