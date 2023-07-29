from django.shortcuts import render
from .models import Materiales, Marca
from django.db.models import Q
from django.core.paginator import Paginator

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