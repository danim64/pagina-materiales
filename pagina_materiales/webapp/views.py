from django.shortcuts import render, redirect
from .models import Materiales, Marca
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import MaterialesForm

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


    material.delete()
    return redirect("listar-materiales")



def eliminar(request, id):
    material = Materiales.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        material.delete()
        # redirect to the bands list
        return redirect('listar-materiales')

    # no need for an `else` here. If it's a GET request, just continue

    return render(request,
                    'materiales/confirm_delete.html',
                    {'material': material})

def crearMaterial(request):
    formulario = MaterialesForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    return render(request, "materiales/crear.html", {
        
        "formulario":formulario
        
    })