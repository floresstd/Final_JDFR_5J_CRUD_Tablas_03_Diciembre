from django.shortcuts import render, redirect
from .models import Orden

# Vista inicial para mostrar todas las órdenes
def inicio_vistaOrden(request):
    lasordenes = Orden.objects.all()
    return render(request, "gestionarOrdenes.html", {"misordenes": lasordenes})

# Registrar una nueva orden
def registrarOrden(request):
    id_cliente = request.POST["txtid_cliente"]
    fecha = request.POST["datefecha"]
    id_producto = request.POST["txtid_producto"]
    id_categoria = request.POST["txtid_categoria"]
    cantidad = request.POST["txtcantidad"]
    precio = request.POST["txtprecio"]  # Nuevo campo para el precio

    Orden.objects.create(
        Id_cliente=id_cliente,
        Fecha=fecha,
        Id_producto=id_producto,
        Id_Categoria=id_categoria,
        Cantidad=cantidad,
        Precio=precio,  # Guardar el precio
    )  # Guarda el nuevo registro

    return redirect("/orden")

# Seleccionar una orden específica para editarla
def seleccionarOrden(request, id_orden):
    orden = Orden.objects.get(id_orden=id_orden)
    return render(request, "editarorden.html", {"misorden": orden})  # Corregido para usar singular

# Editar una orden existente
def editarOrden(request):
    id_orden = request.POST["txtid_orden"]
    id_cliente = request.POST["txtid_cliente"]
    fecha = request.POST["datefecha"]
    id_producto = request.POST["txtid_producto"]
    id_categoria = request.POST["txtid_categoria"]
    cantidad = request.POST["txtcantidad"]
    precio = request.POST["txtprecio"]  # Nuevo campo para el precio

    orden = Orden.objects.get(id_orden=id_orden)
    orden.Id_cliente = id_cliente
    orden.Fecha = fecha
    orden.Id_producto = id_producto
    orden.Id_Categoria = id_categoria
    orden.Cantidad = cantidad
    orden.Precio = precio  # Actualizar el precio
    orden.save()  # Guarda el registro actualizado

    return redirect("/orden")

# Borrar una orden
def borrarOrden(request, id_orden):
    orden = Orden.objects.get(id_orden=id_orden)
    orden.delete()  # Borra el registro

    return redirect("/orden")
