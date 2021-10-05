from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from barbeiro.models import Barbeiro, BarbeiroServico
from barbearia.models import Barbearia


# Create your views here.
def listar_barbeiros(request):
    barbeiros = Barbeiro.objects.all()
    c = {
        "barbeiros": barbeiros
    }
    return render(request, 'barbeiro/listar_barbeiros.html', context=c)


def criar_barbeiro(request):
    if request.method == 'GET':
        barbearias = Barbearia.objects.all()
        c = {
            "barbearias": barbearias
        }
        return render(request, 'barbeiro/criar_barbeiro.html', context=c)
    if request.method == 'POST':
        barbearia_id = int(request.POST["barbearia"])
        barbearia = Barbearia.objects.get(id=barbearia_id)
        nome = request.POST["nome"]
        Barbeiro.objects.create(
            nome=nome,
            barbearia=barbearia
        )
        return HttpResponseRedirect(reverse("listar_barbeiros"))


def listar_servicos(request, barbeiro_id):
    barbeiro = Barbeiro.objects.get(id=barbeiro_id)
    c = {
        "barbeiro": barbeiro,
        "servicos": barbeiro.servicos.all()
    }
    return render(request, 'barbeiro/listar_servicos.html', context=c)


def criar_servico(request, barbeiro_id):
    barbeiro = Barbeiro.objects.get(id=barbeiro_id)
    c = {
        "barbeiro": barbeiro,
    }
    if request.method == 'GET':
        return render(request, 'barbeiro/criar_servico.html', context=c)
    if request.method == 'POST':
        nome = request.POST["nome"]
        preco = request.POST["preco"]
        duracao = request.POST["duracao"]
        BarbeiroServico.objects.create(
            nome=nome,
            preco=preco,
            duracao=duracao,
            barbeiro=barbeiro
        )
        return HttpResponseRedirect(reverse("listar_servicos", args=(barbeiro_id,)))
