from categoria import Categoria
from unidad_medida import UnidadMedida
from articulo_insumo import ArticuloInsumo
from imagen import Imagen
from articulo_manufacturado_detalle import ArticuloDetalle
from articulo_manufacturado import ArticuloManufacturado

#categorias
cat_pizza = Categoria(denominacion="Pizza", id=1)
cat_lomos = Categoria(denominacion="Lomos", id=2)
cat_sandwich = Categoria(denominacion="Sandwich", id=3)
cat_insumos = Categoria(denominacion="Insumos", id=4)

#unidades
kg = UnidadMedida(denominacion='kilos', id=1)
l = UnidadMedida(denominacion='litros', id=2)
gr = UnidadMedida(denominacion='gramos', id=3)

#insumos
sal = ArticuloInsumo(denominacion="sal",precioCompra=100,stockActual=20,stockMaximo=40, esParaElaborar=True)
aceite = ArticuloInsumo(denominacion="aceite", precioCompra=500,stockActual=10,stockMaximo=55, esParaElaborar=True)
carne = ArticuloInsumo(denominacion="carne", precioCompra=10000,stockActual=20,stockMaximo=20, esParaElaborar=True)
harina = ArticuloInsumo(denominacion="harina", precioCompra=10,stockActual=15,stockMaximo=40, esParaElaborar=True)

# Imágenes (6)
hawaina_pizza1 = Imagen(denominacion='Pizza',id=1)
hawaina_pizza2 = Imagen(denominacion='Pizza',id=2)
hawaina_pizza3 = Imagen(denominacion='Pizza',id=3)
lomo_completo1 = Imagen(denominacion='Lomos',id=1)
lomo_completo2 = Imagen(denominacion='Lomos',id=2)
lomo_completo3 = Imagen(denominacion='Lomos',id=3)
img_pizzas = {hawaina_pizza1, hawaina_pizza2, hawaina_pizza3}
img_lomos = {lomo_completo1, lomo_completo2, lomo_completo3}

#detalles
detalle_pizza_hawaina1 = ArticuloDetalle(id =1, cantidad=1, articulo_insumo=sal)
detalle_pizza_hawaina2 = ArticuloDetalle(id =2, cantidad=2, articulo_insumo=harina)
detalle_pizza_hawaina3 = ArticuloDetalle(id =3, cantidad=1, articulo_insumo=aceite)
detalle_pizza_lomo1 = ArticuloDetalle(id =1, cantidad=1, articulo_insumo=sal)
detalle_pizza_lomo2 = ArticuloDetalle(id =2, cantidad=1, articulo_insumo=aceite)
detalle_pizza_lomo3 = ArticuloDetalle(id =3, cantidad=1, articulo_insumo=carne)
detalles_pizzas = {detalle_pizza_hawaina1, detalle_pizza_hawaina2, detalle_pizza_hawaina3}
detalles_lomos = {detalle_pizza_lomo1, detalle_pizza_lomo2, detalle_pizza_lomo3}


#manufacturados
pizza_hawaina = ArticuloManufacturado(
    denominacion="Pizza Hawaina",
    precioVenta=12.0,
    descripcion="Pizza con piña y jamón",
    tiempoEstimadoMinutos=20,
    preparacion="Hornear por 20 minutos",
    categoria=cat_pizza,
    unidad_medida=kg,
    imagen=img_pizzas,
    detalles=detalles_pizzas,
    id=40)


lomo_completo = ArticuloManufacturado(
    denominacion="Lomos",
    precioVenta=12.0,
    descripcion="Lomo completo",
    tiempoEstimadoMinutos=40,
    preparacion="Hornear por 40 minutos",
    categoria=cat_sandwich,
    unidad_medida=kg,
    imagen=img_lomos,
    detalles=detalles_lomos,
    id=20)

#categorias
categorias = [cat_pizza, cat_sandwich, cat_insumos]
print("Categorías:")
for cat in categorias:
    print(f"- {cat.denominacion} (ID: {cat.id})")

#articulos insumo
insumos = [sal, aceite, carne, harina]
print("\nArtículos Insumos:")
for insumo in insumos:
    print(f"- Nombre: {insumo.denominacion}, Precio Compra: {insumo.precioCompra}, Stock: {insumo.stockActual}/{insumo.stockMaximo}")

#articulos manufacturado
manufacturados = [pizza_hawaina, lomo_completo]
print("\nArtículos Manufacturados:")
for prod in manufacturados:
    print(f"- {prod.denominacion}, Descripción: {prod.descripcion}, Precio Venta: {prod.precioVenta}, Tiempo Estimado: {prod.tiempoEstimadoMinutos} min")

#articulos manufacturado por ID
def buscar_manufacturado_por_id(lista, id_buscar):
    for prod in lista:
        if prod.id == id_buscar:
            return prod
    return None

buscado = buscar_manufacturado_por_id(manufacturados, 20)
if buscado:
    print(f"\nArtículo Manufacturado encontrado por ID 20: {buscado.denominacion}")
else:
    print("\nNo se encontró el artículo con ID 101")

#actualizar articulos manufacturado ID
id_actualizar = 20
nuevo_precio = 30
prod_actualizar = buscar_manufacturado_por_id(manufacturados, id_actualizar)
if prod_actualizar:
    prod_actualizar.precioVenta = nuevo_precio
    print(f"\nPrecio actualizado de {prod_actualizar.denominacion}: {prod_actualizar.precioVenta}")

#eliminar articulos manufacturado ID

id_eliminar = 40
manufacturados = [prod for prod in manufacturados if prod.id == id_eliminar]
print("\nArtículos Manufacturados después de eliminar ID 40:")
for prod in manufacturados:
    print(f"- {prod.denominacion}")