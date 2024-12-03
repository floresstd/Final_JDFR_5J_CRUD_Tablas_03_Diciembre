from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.

def inicio_vistaProveedor(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedores.html", {"misproveedores": losproveedores})

def registrarProveedor(request):
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]

    guardarproveedor = Proveedor.objects.create(
        Nombre=nombre, Telefono=telefono, Email=email, Direccion=direccion
    )  # GUARDA EL REGISTRO

    return redirect("/proveedor")

def seleccionarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarproveedor.html", {"misproveedores": proveedor})

def editarProveedor(request):
    id_proveedor = request.POST["txtid_proveedor"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.Nombre = nombre
    proveedor.Telefono = telefono
    proveedor.Email = email
    proveedor.Direccion = direccion
    proveedor.save()  # guarda el registro actualizado
    return redirect("/proveedor")

def borrarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()  # borra el registro
    return redirect("/proveedor")
