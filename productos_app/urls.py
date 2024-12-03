from django.urls import path
from productos_app import views
urlpatterns = [
    path('producto/', views.inicio_vistaProducto, name="inicio_vistaProducto"),  # Ruta para mostrar los productos
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),  # Ruta para registrar un producto
    path("producto/seleccionarProducto/<int:id_producto>/", views.seleccionarProducto, name="seleccionarProducto"),  # Ruta para seleccionar un producto
    path("editarProducto/", views.editarProducto, name="editarProducto"),  # Ruta para editar un producto
    path("producto/borrarProducto/<int:id_producto>/", views.borrarProducto, name="borrarProducto"),  # Ruta para borrar un producto
  # Ruta para borrar un cliente
]
