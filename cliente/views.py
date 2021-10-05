from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from cliente.models import Cliente, ClienteAgendamento
from barbeiro.models import BarbeiroServico


# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()
    c = {
        "clientes": clientes
    }
    return render(request, 'cliente/listar_clientes.html', context=c)


def criar_cliente(request):
    if request.method == 'GET':
        return render(request, 'cliente/criar_cliente.html')
    if request.method == 'POST':
        nome = request.POST["nome"]
        Cliente.objects.create(
            nome=nome
        )
        return HttpResponseRedirect(reverse("listar_clientes"))


def listar_servicos(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    c = {
        "cliente": cliente,
        "servicos_agendados": ClienteAgendamento.objects.filter(cliente=cliente)
    }
    return render(request, 'cliente/listar_servicos.html', context=c)


def agendar_servico(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    servicos = BarbeiroServico.objects.all()
    c = {
        "cliente": cliente,
        "servicos": servicos,
    }
    if request.method == 'GET':
        return render(request, 'cliente/agendar_servico.html', context=c)
    if request.method == 'POST':
        data = request.POST["data"]
        servico_id = int(request.POST["servico"])
        servico = BarbeiroServico.objects.get(id=servico_id)
        ClienteAgendamento.objects.create(
            cliente=cliente,
            barbeiro=servico.barbeiro,
            servico=servico,
            data=data
        )
        return HttpResponseRedirect(reverse("listar_agendamentos", args=(cliente.id,)))
    return