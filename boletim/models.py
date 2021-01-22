'''
Importa o módulo de banco de dados padrão do Django
'''
from django.db import models

class TipoBI(models.Model):
    descricao = models.CharField(max_length=250)
    abreviatura = models.CharField(max_length=250)
    slug = models.SlugField()
    numeroUltimaPagina = models.IntegerField()
    numeroUltimoBI = models.IntegerField()
    iniciaNumeroPagina = models.IntegerField()
    eAditamento = models.BooleanField()
    imprimeBordas = models.BooleanField()
    titulo = models.CharField(max_length=250)

class Boletim(models.Model):
    ''' Classe Boletim '''
    paginaInicial = models.IntegerField()
    paginaFinal = models.IntegerField()
    aprovado = models.BooleanField(default=False)
    assinado = models.BooleanField(default=False)
    numeroBI = models.IntegerField()
    assinaConfereBI = models.BooleanField(default=False)
    dataPublicacao = models.DateField()
    slug = models.SlugField()
    tipoPub = models.ForeignKey(TipoBI, on_delete=models.CASCADE)
    #biRef = models.
    #colMateriaBI = models.