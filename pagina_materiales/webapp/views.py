from django.shortcuts import render
from .models import Materiales, Marca
from django.db.models import Q

# Create your views here.


def inicio(request):
    return render(request, "webapp/index.html")


def materiales(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        materiales_totales = Materiales.objects.filter(Q(descripcion__icontains=search_post))
        for material in materiales_totales:
            print(material) 
    else:
        # If not searched, return default posts
        materiales_totales = Materiales.objects.all().order_by("-fecha_precio")
        
        #marcas= Marca.objects.all()
    return render(request, "materiales/listar.html", {
        "materiales": materiales_totales,
        #"marcas": marcas,

    })