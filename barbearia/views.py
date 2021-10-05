from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from barbearia.models import Barbearia


def index(request):
    return render(request, 'barbearia/index.html')

# Create your views here.
def listar_barbearias(request):
    barbearias = Barbearia.objects.all()
    c = {
        "barbearias": barbearias
    }
    return render(request, 'barbearia/listar_barbearias.html', context=c)


def criar_barbearia(request):
    if request.method == 'GET':
        return render(request, 'barbearia/criar_barbearia.html')
    if request.method == 'POST':
        nome = request.POST["nome"]
        Barbearia.objects.create(
            nome=nome
        )
        return HttpResponseRedirect(reverse("listar_barbearias"))
