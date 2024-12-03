from django.urls import path
from proveedores_app import views

urlpatterns = [
    path('proveedor/', views.inicio_vistaProveedor, name="inicio_vistaProveedor"),  # Ruta para mostrar los proveedores
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),  # Ruta para registrar un proveedor
    path("proveedor/seleccionarProveedor/<int:id_proveedor>/", views.seleccionarProveedor, name="seleccionarProveedor"),  # Ruta para seleccionar un proveedor
    path("editarProveedor/", views.editarProveedor, name="editarProveedor"),  # Ruta para editar un proveedor
    path("proveedor/borrarProveedor/<int:id_proveedor>/", views.borrarProveedor, name="borrarProveedor"),  # Ruta para borrar un proveedor
]
