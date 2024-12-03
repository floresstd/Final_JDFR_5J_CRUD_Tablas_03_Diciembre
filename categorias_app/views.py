from django.shortcuts import render, redirect
from .models import Categoria

# Vista inicial para mostrar todas las categorías
def inicio_vistaCategoria(request):
    lascategorias = Categoria.objects.all()
    return render(request, "gestionarCategorias.html", {"miscategorias": lascategorias})

# Registrar una nueva categoría
def registrarCategoria(request):
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    Categoria.objects.create(
        Nombre=nombre,
        Descripcion=descripcion,
    )  # Guarda el nuevo registro

    return redirect("/categoria")

# Seleccionar una categoría específica para editarla
def seleccionarCategoria(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    return render(request, "editarcategoria.html", {"miscategorias": categoria})

# Editar una categoría existente
def editarCategoria(request):
    id_categoria = request.POST["txtid_categoria"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.Nombre = nombre
    categoria.Descripcion = descripcion
    categoria.save()  # Guarda el registro actualizado

    return redirect("/categoria")

# Eliminar una categoría
def borrarCategoria(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    categoria.delete()  # Borra el registro

    return redirect("/categoria")
