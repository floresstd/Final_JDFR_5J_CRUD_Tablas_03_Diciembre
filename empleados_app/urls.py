from django.urls import path
from empleados_app import views
urlpatterns = [
    path('empleado/', views.inicio_vistaEmpleado, name="inicio_vistaEmpleado"),  # Vista inicial para listar empleados
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),  # Ruta para registrar un nuevo empleado
    path("empleado/seleccionarEmpleado/<int:id_empleado>/", views.seleccionarEmpleado, name="seleccionarEmpleado"),  # Ruta para seleccionar un empleado
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),  # Ruta para editar un empleado existente
    path("empleado/borrarEmpleado/<int:id_empleado>/", views.borrarEmpleado, name="borrarEmpleado"),  # Ruta para borrar un empleado
]