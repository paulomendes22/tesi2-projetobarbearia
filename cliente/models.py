from django.db import models

from barbeiro.models import Barbeiro, BarbeiroServico


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nome} - {self.id}"


class ClienteAgendamento(models.Model):
    STATUS_AGENDAMENTO_ESCOLHAS = [
        ('0', 'Agendado'),
        ('1', 'Executado'),
        ('2', 'Cancelado pelo cliente'),
        ('3', 'Cancelado pelo barbeiro'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    servico = models.ForeignKey(BarbeiroServico, on_delete=models.CASCADE)
    data = models.DateTimeField()
    status = models.CharField(
        max_length=2,
        choices=STATUS_AGENDAMENTO_ESCOLHAS,
        default='0',
    )

    def __str__(self) -> str:
        return f"{self.cliente} - {self.barbeiro} - {self.servico} - {self.data}"