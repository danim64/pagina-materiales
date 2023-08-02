from django.shortcuts import render, redirect
from .models import Materiales, Marca, Grupo, Proveedor
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import MaterialesForm, GrupoForm, MarcaForm, ProveedorForm
from django.http import HttpResponseRedirect
from django.db.models.deletion import ProtectedError

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


def listar_grupo(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        grupo_totales = Grupo.objects.filter(Q(categoria__icontains=search_post))
        paginator = Paginator(grupo_totales, 10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        grupo_totales = Grupo.objects.all().order_by("-categoria")
        paginator = Paginator(grupo_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "grupo/listar.html", {
        "paginas": paginas,

    })

def eliminar_grupo(request, id):
    grupo = Grupo.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            grupo.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-grupo')
    return render(request,
                    'grupo/confirm_delete.html',
                    {'grupo': grupo})

def cant_erase(request):
    return render(request, "grupo/cannot_erase.html")

def crearGrupo(request):
    formulario_gr = GrupoForm(request.POST or None)
    if formulario_gr.is_valid():
        formulario_gr.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "grupo/crear.html", {
        "formulario":formulario_gr    
    })

def confirm_create_gr(request):
    return render(request, "grupo/confirm_create.html")


def listar_marca(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        marca_totales = Marca.objects.filter(Q(nombre__icontains=search_post))
        paginator = Paginator(marca_totales, 15)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        marca_totales = Marca.objects.all().order_by("-nombre")
        paginator = Paginator(marca_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "marca/listar.html", {
        "paginas": paginas,

    })

def crearMarca(request):
    formulario_mrk = MarcaForm(request.POST or None)
    if formulario_mrk.is_valid():
        formulario_mrk.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "grupo/crear.html", {
        "formulario":formulario_mrk    
    })

def confirm_create_mkr(request):
    return render(request, "marca/confirm_create.html")


def eliminar_marca(request, id):
    marca = Marca.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            marca.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-marca')
    return render(request,
                    'marca/confirm_delete.html',
                    {'marca': marca})


def cant_erase_mk(request):
    return render(request, "marca/cannot_erase.html")

def listar_proveedor(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        proveedor_totales = Proveedor.objects.filter(Q(nombre__icontains=search_post))
        paginator = Paginator(proveedor_totales, 5)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        proveedor_totales = Proveedor.objects.all().order_by("-nombre")
        paginator = Paginator(proveedor_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "proveedor/listar.html", {
        "paginas": paginas,

    })

def crearProveedor(request):
    formulario_prvd = ProveedorForm(request.POST or None)
    if formulario_prvd.is_valid():
        formulario_prvd.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "proveedor/crear.html", {
        "formulario":formulario_prvd 

    })

def confirm_create_prvd(request):
    return render(request, "proveedor/confirm_create.html")

def editar_proveedor(request, id):
    material = Proveedor.objects.get(id=id)
    formulario = ProveedorForm(request.POST or None, instance=material)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return HttpResponseRedirect("confirm-edit-prv")
    return render(request, "proveedor/editar.html", {"formulario" : formulario})

def confirm_edit_prv(request):
    return render(request, "proveedor/confirm_edit.html")



def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            proveedor.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-proveedor')
    return render(request,
                    'proveedor/confirm_delete.html',
                    {'proveedor': proveedor})