from django.urls import path

from . import views

urlpatterns = [
    path("listar_barbearias", views.listar_barbearias, name="listar_barbearias"),
    path("criar", views.criar_barbearia, name="criar_barbearia")
]