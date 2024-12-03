from django.urls import path
from ordenes_app import views
urlpatterns = [
    path('orden/', views.inicio_vistaOrden, name="inicio_vistaOrden"),  # Vista inicial para listar órdenes
    path("registrarOrden/", views.registrarOrden, name="registrarOrden"),  # Ruta para registrar una nueva orden
    path("orden/seleccionarOrden/<int:id_orden>/", views.seleccionarOrden, name="seleccionarOrden"),  # Ruta para seleccionar una orden
    path("editarOrden/", views.editarOrden, name="editarOrden"),  # Ruta para editar una orden existente
    path("orden/borrarOrden/<int:id_orden>/", views.borrarOrden, name="borrarOrden"),  # Ruta para borrar una orden
]
