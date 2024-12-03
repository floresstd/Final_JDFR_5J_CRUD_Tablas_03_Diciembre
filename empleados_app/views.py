from django.shortcuts import render, redirect
from .models import Empleado

# Vista inicial para mostrar todos los empleados
def inicio_vistaEmpleado(request):
    los_empleados = Empleado.objects.all()
    return render(request, "gestionarEmpleados.html", {"mis_empleados": los_empleados})

# Registrar un nuevo empleado
def registrarEmpleado(request):
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    fecha_contratacion = request.POST["datefecha_contratacion"]
    puesto = request.POST["txtpuesto"]

    Empleado.objects.create(
        Nombre=nombre,
        Telefono=telefono,
        Email=email,
        Fecha_nacimiento=fecha_nacimiento,
        Fecha_contratacion=fecha_contratacion,
        Puesto=puesto,
    )  # Guarda el nuevo registro

    return redirect("/empleado")

# Seleccionar un empleado específico para editarlo
def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarempleado.html", {"empleado": empleado})

# Editar un empleado existente
def editarEmpleado(request):
    id_empleado = request.POST["txtid_empleado"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    fecha_nacimiento = request.POST["datefecha_nacimiento"]
    fecha_contratacion = request.POST["datefecha_contratacion"]
    puesto = request.POST["txtpuesto"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.Nombre = nombre
    empleado.Telefono = telefono
    empleado.Email = email
    empleado.Fecha_nacimiento = fecha_nacimiento
    empleado.Fecha_contratacion = fecha_contratacion
    empleado.Puesto = puesto
    empleado.save()  # Guarda el registro actualizado

    return redirect("/empleado")

# Borrar un empleado
def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()  # Borra el registro

    return redirect("/empleado")
