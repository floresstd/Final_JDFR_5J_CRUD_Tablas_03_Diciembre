from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def inicio_vistaProducto(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProductos.html", {"misproductos": losproductos})

def registrarProducto(request):
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    stock = request.POST["txtstock"]

    guardarproducto = Producto.objects.create(
        Nombre=nombre, Descripcion=descripcion, Precio=precio, Stock=stock
    )  # GUARDA EL REGISTRO

    return redirect("/producto")

def seleccionarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "editarproducto.html", {"misproductos": producto})

def editarProducto(request):
    id_producto = request.POST["txtid_producto"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    precio = request.POST["txtprecio"]
    stock = request.POST["txtstock"]

    producto = Producto.objects.get(id_producto=id_producto)
    producto.Nombre = nombre
    producto.Descripcion = descripcion
    producto.Precio = precio
    producto.Stock = stock
    producto.save()  # guarda el registro actualizado
    return redirect("/producto")

def borrarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()  # borra el registro
    return redirect("/producto")
