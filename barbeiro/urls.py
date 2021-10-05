from django.urls import path

from . import views

urlpatterns = [
    path("listar", views.listar_barbeiros, name="listar_barbeiros"),
    path("criar", views.criar_barbeiro, name="criar_barbeiro"),
    path("<int:barbeiro_id>/servicos", views.listar_servicos, name="listar_servicos"),
    path("<int:barbeiro_id>/servicos/criar", views.criar_servico, name="criar_servico"),
]