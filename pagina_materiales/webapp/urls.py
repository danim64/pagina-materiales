from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("listar-materiales/", views.materiales, name="listar-materiales"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
    path("materiales/crear", views.crearMaterial, name="crear-material"),

]
