from django.urls import path

from . import views

urlpatterns = [
    path("listar_clientes", views.listar_clientes, name="listar_clientes"),
    path("criar", views.criar_cliente, name="criar_cliente"),
    path("<int:cliente_id>/agendamentos", views.listar_servicos, name="listar_agendamentos"),
    path("<int:cliente_id>/agendamentos/criar", views.agendar_servico, name="agendar_servico"),
]