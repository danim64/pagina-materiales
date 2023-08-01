from django.shortcuts import render, redirect
from .models import Materiales, Marca
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import MaterialesForm
from django.http import HttpResponseRedirect

# Create your views here.


def inicio(request):
    return render(request, "webapp/index.html")


def materiales(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        materiales_totales = Materiales.objects.filter(Q(descripcion__icontains=search_post))
        paginator = Paginator(materiales_totales, 15)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        materiales_totales = Materiales.objects.all().order_by("-fecha_precio")
        paginator = Paginator(materiales_totales,15)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "materiales/listar.html", {
        "paginas": paginas,

    })


def eliminar(request, id):
    material = Materiales.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        material.delete()
        # redirect to the bands list
        return redirect('listar-materiales')
    return render(request,
                    'materiales/confirm_delete.html',
                    {'material': material})


def crearMaterial(request):
    formulario = MaterialesForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "materiales/crear.html", {
        "formulario":formulario    
    })



def confirm_create(request):
    return render(request, "materiales/confirm_create.html")

def confirm_edit(request):
    return render(request, "materiales/confirm_edit.html")


def editar_material(request, id):
    material = Materiales.objects.get(id=id)
    formulario = MaterialesForm(request.POST or None, instance=material)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return HttpResponseRedirect("confirm-edit")
    return render(request, "materiales/editar.html", {"formulario" : formulario})