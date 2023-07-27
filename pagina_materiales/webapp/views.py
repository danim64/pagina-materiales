from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "webapp/index.html")


def materiales(request):
    #libros = Libro.objects.all()
    return render(request, "materiales/listar.html", {
        #"libros": libros
    })