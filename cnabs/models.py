from django.db import models
from django import forms
from django.core.validators import MinLengthValidator


    
class ArquivoModel(models.Model):  
    tipo=models.CharField(max_length=1)
    data = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    valor=models.FloatField()
    cpf=models.IntegerField()
    cartao=models.CharField(max_length=12)
    hora =models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    dono_da_loja=models.CharField(max_length=14)
    nome_da_loja=models.CharField(max_length=19)
    
    # COlocar um charfiled no date
    
    # Consertar o reademe com os detalhes do que precisa baixar e como acessar a minha rota