from pais import Pais
from provincia import Provincia
from localidad import  Localidad
from domicilio import Domicilio
from sucursal import Sucursal
from empresa import Empresa
from datetime import time

# Creamos país
pais1 = Pais(nombre='Argentina')


# Creamos provincia
prov1 = Provincia(nombre="Buenos Aires",
                  pais=pais1)
prov2 = Provincia(nombre="Cordoba",
                  pais=pais1)



# Creamos localidad
loc1 = Localidad(nombre="CABA",
                 provincia=prov1)
loc2 = Localidad(nombre="La Plata",
                 provincia=prov1)
loc3 = Localidad(nombre="Cordoba capital",
                 provincia=prov2)
loc4 = Localidad(nombre="Villa Carlos Paz",
                 provincia=prov2)



# Creamos domicilio
dom1 = Domicilio(calle="calle1", numero=123, cp=1234,
                 localidad=loc1)
dom2 = Domicilio(calle="calle2", numero=124, cp=1235,
                 localidad=loc2)
dom3 = Domicilio(calle="calle3", numero=125, cp=1236,
                 localidad=loc3)
dom4 = Domicilio(calle="calle4", numero=126, cp=1237,
                 localidad=loc4)



# Creamos sucursal
suc1 = Sucursal(
    nombre="Sucursal 1",
    horarioApertura=time(9, 0),
    horarioCierre=time(18, 0),
    es_Casa_Matriz=True,
    #asignamos domicilio
    domicilio=dom1)
suc2 = Sucursal(
    nombre="Sucursal 2",
    horarioApertura=time(9, 0),
    horarioCierre=time(18, 0),
    es_Casa_Matriz=True,
    domicilio=dom2)
suc3 = Sucursal(
    nombre="Sucursal 3",
    horarioApertura=time(9, 0),
    horarioCierre=time(18, 0),
    es_Casa_Matriz=True,
    domicilio=dom3)
suc4 = Sucursal(
    nombre="Sucursal 4",
    horarioApertura=time(9, 0),
    horarioCierre=time(18, 0),
    es_Casa_Matriz=True,
    domicilio=dom4)



# Creamos la empresa
empresa1 = Empresa(
    id = 1,
    nombre="empresa 1",
    razonSocial="Mi Empresa 1 S.A.",
    cuil=20123456782,
    logo="logo.png",
    #asignamos sucursal
    sucursales={suc1, suc2}
)
empresa2 = Empresa(
    id = 2,
    nombre="empresa 2",
    razonSocial="Mi Empresa 2 S.A.",
    cuil=20234567892,
    logo="logo.png",
    sucursales={suc3, suc4}
)
empresas = [empresa1, empresa2]




#Uso
def buscar_empresa_por_id(empresas, id):
    return next((e for e in empresas if e.id == id), None)

def buscar_empresa_por_nombre(empresas, nombre):
    return [e for e in empresas if e.nombre.lower() == nombre.lower()]

def actualizar_empresa_por_id(empresas, id, nuevo_cuit):
    empresa = buscar_empresa_por_id(empresas, id)
    if empresa:
        empresa.cuit = nuevo_cuit
        return True
    return False

def eliminar_empresa_por_id(empresas, id):
    empresa = buscar_empresa_por_id(empresas, id)
    if empresa:
        empresas.remove(empresa)
        return True
    return False


# MOSTRAR INFORMACIÓN
print("\n--- MOSTRANDO TODAS LAS EMPRESAS ---")
for empresa in empresas:
    print(f"\nEmpresa: {empresa.nombre} (ID: {empresa.id}, CUIT: {empresa.cuil})")
    for s in empresa.sucursales:
        tipo = "Casa Matriz" if s.es_Casa_Matriz else "Sucursal"
        print(f"- {tipo}: {s.nombre} ({s.horarioApertura} - {s.horarioCierre})")
        d = s.domicilio
        print(f"  Domicilio: {d.calle} {d.numero}, CP {d.cp}")
        print(f"  Localidad: {d.localidad.nombre}")
        print(f"  Provincia: {d.localidad.provincia.nombre}")
        print(f"  País: {d.localidad.provincia.pais.nombre}")


# EJEMPLOS DE OPERACIONES (puntos 5.b - 5.e)
print("\n--- BÚSQUEDA POR ID (ID=1) ---")
empresa_buscada = buscar_empresa_por_id(empresas, 1)
print(empresa_buscada if empresa_buscada else "No se encontró la empresa")

print("\n--- BÚSQUEDA POR NOMBRE (empresa 2) ---")
for e in buscar_empresa_por_nombre(empresas, "empresa 2"):
    print(e)

print("\n--- ACTUALIZACIÓN DE CUIT (ID=2) ---")
if actualizar_empresa_por_id(empresas, 2, 20999999999):
    print(f"CUIT actualizado: {buscar_empresa_por_id(empresas, 2).cuit}")

print("\n--- ELIMINACIÓN DE EMPRESA (ID=1) ---")
if eliminar_empresa_por_id(empresas, 1):
    print("Empresa eliminada. Empresas restantes:")
    for e in empresas:
        print(f"- {e.nombre}")

def buscar_empresa_por_nombre(empresas, nombre):
    return [e for e in empresas if e.nombre.lower() == nombre.lower()]

def actualizar_empresa_por_id(empresas, id, nuevo_cuit):
    empresa = buscar_empresa_por_id(empresas, id)
    if empresa:
        empresa.cuit = nuevo_cuit
        return True
    return False

def eliminar_empresa_por_id(empresas, id):
    empresa = buscar_empresa_por_id(empresas, id)
    if empresa:
        empresas.remove(empresa)
        return True
    return False



# MOSTRAR INFORMACIÓN
print("\n--- MOSTRANDO TODAS LAS EMPRESAS ---")
for empresa in empresas:
    print(f"\nEmpresa: {empresa.nombre} (ID: {empresa.id}, CUIT: {empresa.cuil})")
    for s in empresa.sucursales:
        tipo = "Casa Matriz" if s.es_Casa_Matriz else "Sucursal"
        print(f"- {tipo}: {s.nombre} ({s.horarioApertura} - {s.horarioCierre})")
        d = s.domicilio
        print(f"  Domicilio: {d.calle} {d.numero}, CP {d.cp}")
        print(f"  Localidad: {d.localidad.nombre}")
        print(f"  Provincia: {d.localidad.provincia.nombre}")
        print(f"  País: {d.localidad.provincia.pais.nombre}")


# EJEMPLOS DE OPERACIONES (puntos 5.b - 5.e)
print("\n--- BÚSQUEDA POR ID (ID=1) ---")
empresa_buscada = buscar_empresa_por_id(empresas, 1)
print(empresa_buscada if empresa_buscada else "No se encontró la empresa")

print("\n--- BÚSQUEDA POR NOMBRE (empresa 2) ---")
for e in buscar_empresa_por_nombre(empresas, "empresa 2"):
    print(e)

print("\n--- ACTUALIZACIÓN DE CUIT (ID=2) ---")
if actualizar_empresa_por_id(empresas, 2, 20999999999):
    print(f"CUIT actualizado: {buscar_empresa_por_id(empresas, 2).cuit}")

print("\n--- ELIMINACIÓN DE EMPRESA (ID=1) ---")
if eliminar_empresa_por_id(empresas, 1):
    print("Empresa eliminada. Empresas restantes:")
    for e in empresas:
        print(f"- {e.nombre}")
