import pytest
from dataclasses import FrozenInstanceError
from types import MappingProxyType

from patrones.builder.implementation import Usuario


def test_builder_minimo_valores_por_defecto():
    u = Usuario.builder("celi").build()
    assert u.username == "celi"
    assert u.email is None
    assert u.nombre is None
    assert u.telefono is None
    assert u.direccion is None
    assert isinstance(u.preferencias, MappingProxyType)
    assert dict(u.preferencias) == {}


def test_builder_completo_con_normalizacion_y_prefs():
    u = (
        Usuario.builder("juan")
        .email("  juan@example.com  ")
        .nombre(" Juan Perez ")
        .telefono("(11) 5555-1212")
        .direccion(" Calle Falsa 123 ")
        .preferencia("tema", "oscuro")
        .preferencias({"notificaciones": True, "idioma": "es"})
        .build()
    )

    assert u.username == "juan"
    assert u.email == "juan@example.com"          # strip aplicado
    assert u.nombre == "Juan Perez"               # strip aplicado
    assert u.telefono == "1155551212"             # solo dígitos
    assert u.direccion == "Calle Falsa 123"       # strip aplicado
    assert dict(u.preferencias) == {
        "tema": "oscuro",
        "notificaciones": True,
        "idioma": "es",
    }


def test_inmutabilidad_no_permite_setattr():
    u = Usuario.builder("ana").build()
    with pytest.raises(FrozenInstanceError):
        setattr(u, "email", "otro@x.com")


def test_preferencias_inmutable():
    u = Usuario.builder("sofia").preferencia("tema", "claro").build()
    with pytest.raises(TypeError):
        # MappingProxyType es de solo lectura
        u.preferencias["tema"] = "oscuro"  # type: ignore[index]


@pytest.mark.parametrize("bad", ["foo@", "@bar.com", "foobar"])
def test_email_invalido_levanta_error(bad):
    b = Usuario.builder("user").email(bad)
    with pytest.raises(ValueError):
        b.build()


def test_telefono_demasiado_corto_levanta_error():
    with pytest.raises(ValueError):
        Usuario.builder("user").telefono("123-45").build()  # < 7 dígitos


def test_encadenamiento_devuelve_el_mismo_builder():
    b = Usuario.builder("x")
    b2 = b.email("a@b.com")
    b3 = b2.nombre("X")
    assert isinstance(b2, Usuario.Builder)
    assert isinstance(b3, Usuario.Builder)


def test_prefs_no_se_ven_afectadas_si_muto_el_dict_fuente():
    fuente = {"tema": "oscuro"}
    u = Usuario.builder("leo").preferencias(fuente).build()
    fuente["tema"] = "claro"  # mutación del dict original
    assert u.preferencias["tema"] == "oscuro"  # usuario permanece igual
