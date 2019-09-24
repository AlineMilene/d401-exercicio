from django.db import models
from django.utils import timezone

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name='Nome',
        )
    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Nome')
    # data_nascimento = models.DataField()
    cpf = models.CharField(
        max_length=15,
        verbose_name='CPF',
        )
    cep = models.CharField(
        max_length=10)

    item_de_doacao = models.CharField(
        max_length=100)

    ativo = models.BooleanField(
        default=True)

    data_criacao = models.DateTimeField(
        default=timezone.now)

