import pytest

from patrones.abstract_factory.implementation import (
    AbstractFactory,
    AdminFactory,
    UsuarioFactory,
    AdminUI,
    UsuarioUI,
    EnvioExpress,
    EnvioNormal,
    TipoUsuario,
    InterfazUI,
    MetodoEnvio,
)


def test_admin_factory_crea_familia_admin():
    fabrica = AdminFactory()
    ui = fabrica.crear_ui()
    envio = fabrica.crear_envio()

    assert isinstance(ui, AdminUI)
    assert isinstance(envio, EnvioExpress)
    assert isinstance(ui, InterfazUI)
    assert isinstance(envio, MetodoEnvio)

    # checks rápidos de comportamiento
    assert "AdminUI" in ui.render_home()
    assert "USUARIOS_CRUD" in ui.permisos()
    assert "EnvioExpress" == envio.nombre()


def test_usuario_factory_crea_familia_usuario():
    fabrica = UsuarioFactory()
    ui = fabrica.crear_ui()
    envio = fabrica.crear_envio()

    assert isinstance(ui, UsuarioUI)
    assert isinstance(envio, EnvioNormal)
    assert "UsuarioUI" in ui.render_home()
    assert "CATALOGO_VER" in ui.permisos()
    assert "EnvioNormal" == envio.nombre()


@pytest.mark.parametrize(
    "tipo,expected_ui,expected_envio",
    [
        ("admin", AdminUI, EnvioExpress),
        (TipoUsuario.ADMIN, AdminUI, EnvioExpress),
        ("usuario", UsuarioUI, EnvioNormal),
        (TipoUsuario.USUARIO, UsuarioUI, EnvioNormal),
    ],
)
def test_desde_tipo_devuelve_fabrica_correcta(tipo, expected_ui, expected_envio):
    fabrica = AbstractFactory.desde_tipo(tipo)
    assert isinstance(fabrica.crear_ui(), expected_ui)
    assert isinstance(fabrica.crear_envio(), expected_envio)


def test_costos_y_eta_envio_normal():
    envio = EnvioNormal()
    # base=3.0, por_km=0.5, por_kg=1.0
    costo = envio.calcular_costo(peso_kg=1.2, distancia_km=100)  # 3 + 0.5*100 + 1.2 = 54.2
    assert costo == pytest.approx(54.2)
    assert "día" in envio.tiempo_estimado(120)


def test_costos_y_eta_envio_express():
    envio = EnvioExpress()
    # base=7.0, por_km=0.9, por_kg=1.2
    costo = envio.calcular_costo(peso_kg=1.0, distancia_km=120)  # 7 + 0.9*120 + 1.2 = 116.2
    assert costo == pytest.approx(116.2)
    assert "h aprox." in envio.tiempo_estimado(120)


def test_error_tipo_invalido():
    with pytest.raises(ValueError):
        AbstractFactory.desde_tipo("invitado")
