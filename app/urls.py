from django.urls import path
from .views import home, galeria, contacto, galeria2, agregar_producto, agregar_trabajador, \
    listar_productos, modificar_producto, eliminar_producto, registro, eliminar_producto_c ,carrito, \
    restar_producto, limpiar_carrito, agregara , webpay , usuario

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('trabajadores/', galeria, name="galeria"),
    path('galeria/', galeria2, name="galeria2"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('agregar_trabajador/', agregar_trabajador, name="agregar_trabajador"),
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('modificar_producto/<int:id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<int:id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('usuario/', usuario, name="usuario"),
    path('webpay/', webpay, name="webpay"),
    path('carrito/', carrito, name="carrito"),
    path('agregar/<int:producto_id>/', agregara, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto_c, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]
