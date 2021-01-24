'''
Importa o módulo de banco de dados padrão do Django
'''
from django.db import models

class ParteBoletim(models.Model):
    numero_Parte = models.IntegerField()
    descricao = models.CharField(max_length=250)
    descricao_Reduzida = models.CharField(max_length=250)
    slug = models.SlugField()

class SecaoParteBoletim(models.Model):
    numero_Secao = models.IntegerField()
    descricao = models.CharField(max_length=250)
    slug = models.SlugField()

class TipoBoletim(models.Model):
    descricao = models.CharField(max_length=250)
    abreviatura = models.CharField(max_length=250)
    numero_Ultima_Pagina = models.IntegerField()
    numero_Ultimo_Boletim = models.IntegerField()
    inicia_Numero_Pagina = models.IntegerField()
    e_Aditamento = models.BooleanField()
    imprime_Bordas = models.BooleanField()
    titulo = models.CharField(max_length=250)
    slug = models.SlugField()

class Boletim(models.Model):
    ''' Classe Boletim '''
    pagina_Inicial = models.IntegerField()
    pagina_Final = models.IntegerField()
    aprovado = models.BooleanField(default=False)
    assinado = models.BooleanField(default=False)
    numero_Boletim = models.IntegerField()
    assina_ConfereBoletim = models.BooleanField(default=False)
    data_Publicacao = models.DateField()
    slug = models.SlugField()
    tipo_Boletim = models.ForeignKey(TipoBoletim, on_delete=models.CASCADE)
    boletim_De_Referencia = models.ForeignKey("Boletim", on_delete=models.CASCADE)
    slug = models.SlugField()