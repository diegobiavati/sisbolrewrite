from django.db import models

# Create your models here.
class Boletim(models.Model):
    pagInicial = models.IntegerField()
    pagFinal = models.IntegerField()
    aprovado = models.BooleanField(default=False)
    assinado = models.BooleanField(default=False)
    numeroBI = models.IntegerField()
    assinaConfereBI = models.BooleanField(default=False)
    dataPub = models.DateField()
    slug = models.SlugField()
    #tipoPub = models.
    #biRef = models.
    #colMateriaBI = models.