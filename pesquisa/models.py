from django.db import models

# Create your models here.

class Pergunta(models.Model):
    texto = models.CharField()
    data = models.DateField()

class Alternativa(models.Model):
    texto = models.CharField()
    votos - models.IntegerField()

    