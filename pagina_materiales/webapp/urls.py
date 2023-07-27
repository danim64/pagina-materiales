from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("listar-materiales/", views.materiales, name="listar-materiales"),

]
