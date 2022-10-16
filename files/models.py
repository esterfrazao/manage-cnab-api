import uuid

from django.core.validators import MaxLengthValidator
from django.db import models


class Types(models.IntegerChoices):
    DEBITO = 1
    BOLETO = 2
    FINANCIAMENTO = 3
    CREDITO = 4
    EMPRESTIMO = 5
    VENDAS = 6
    TED = 7
    DOC = 8
    ALUGUEL = 9


class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.IntegerField(choices=Types.choices)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    itin = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    def __repr__(self) -> str:
        return f"{self.type}{self.date}{round(self.value * 100)}{self.itin}{self.card}{self.hour}{self.owner}{self.store_name}"
