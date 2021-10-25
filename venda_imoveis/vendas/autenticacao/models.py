from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.
class Cliente(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    FORMAPAGAMENTO_CHOICES = (
        ("À Vista", "À Vista"),
        ("180 Parcelas", "180 Parcelas"),
    )
    ativo = models.BooleanField(default=True)
    imovel = models.ForeignKey("Imovel", verbose_name=("imovel"), on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    corretor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("corretor"), on_delete=models.CASCADE)
    cliente = models.ForeignKey("Cliente", verbose_name=("cliente"), on_delete=models.CASCADE)
    condicao_pagamento = models.CharField(max_length=30, verbose_name=("Forma de Pagamento"), choices=FORMAPAGAMENTO_CHOICES, null=True)
    
    
class Imovel(models.Model):
    ativo = models.BooleanField(default=True)
    disponivel = models.BooleanField(default=True)
    tipo = models.CharField(max_length=50, null=True)
    valor = models.DecimalField(max_digits=50, decimal_places=2)
    localizacao = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.localizacao


