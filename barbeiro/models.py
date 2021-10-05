from django.db import models

from barbearia.models import Barbearia

class Barbeiro(models.Model):
    nome = models.CharField(max_length=200)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nome} - {self.barbearia} - {self.id}"


class BarbeiroServico(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, related_name="servicos")
    duracao = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nome} - {self.id}"