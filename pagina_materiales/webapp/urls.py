from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("listar-materiales/", views.materiales, name="listar-materiales"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
    path("materiales/crear", views.crearMaterial, name="crear-material"),
    path("materiales/confirm-create", views.confirm_create, name="confirm-create"),
    path("materiales/editar/confirm-edit", views.confirm_edit, name="confirm-edit"),
    path("materiales/editar/<int:id>", views.editar_material, name="editar-material")

]
