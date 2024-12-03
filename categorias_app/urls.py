from django.urls import path
from categorias_app import views
urlpatterns = [
    path('categoria/', views.inicio_vistaCategoria, name="inicio_vistaCategoria"),  # Ruta inicial para gestionar categorías
    path("registrarCategoria/", views.registrarCategoria, name="registrarCategoria"),  # Ruta para registrar una categoría
    path("categoria/seleccionarCategoria/<int:id_categoria>/", views.seleccionarCategoria, name="seleccionarCategoria"),  # Ruta para seleccionar una categoría
    path("editarCategoria/", views.editarCategoria, name="editarCategoria"),  # Ruta para editar una categoría
    path("categoria/borrarCategoria/<int:id_categoria>/", views.borrarCategoria, name="borrarCategoria"),  # Ruta para borrar una categoría
]