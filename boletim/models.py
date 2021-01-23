'''
Importa o módulo de banco de dados padrão do Django
'''
from django.db import models

class ParteBoletim(models.Model):
    numeroParte = models.IntegerField()
    descricao = models.CharField(max_length=250)
    descricaoReduzida = models.CharField(max_length=250)
    slug = models.SlugField()

class SecaoParteBoletim(models.Model):
    numeroSecao = models.IntegerField()
    descricao = models.CharField(max_length=250)
    slug = models.SlugField()

class TipoBoletim(models.Model):
    descricao = models.CharField(max_length=250)
    abreviatura = models.CharField(max_length=250)
    slug = models.SlugField()
    numeroUltimaPagina = models.IntegerField()
    numeroUltimoBoletim = models.IntegerField()
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
    numeroBoletim = models.IntegerField()
    assinaConfereBoletim = models.BooleanField(default=False)
    dataPublicacao = models.DateField()
    slug = models.SlugField()
    tipoBoletim = models.ForeignKey(TipoBoletim, on_delete=models.CASCADE)
    boletimDeReferencia = models.ForeignKey("Boletim", on_delete=models.CASCADE)
    slug = models.SlugField()