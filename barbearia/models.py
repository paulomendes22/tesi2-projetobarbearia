from django.db import models


class Barbearia(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.nome} - {self.id}"
