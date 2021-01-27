from django.db import models
from django.contrib.auth.models import User
from boletim.models import ParteBoletim,SecaoParteBoletim,TipoBoletim,Boletim
from base.models import Pessoa

class PessoaMateriaBoletim(models.Model):
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    texto_Individual = models.TextField()
    slug = models.SlugField()

class TipoDocumento(models.Model):
    descricao = models.CharField(max_length=255)
    slug = models.SlugField()
    def __str__(self):
        return self.descricao

class AssuntoEspecifico(models.Model):
    descricao = models.CharField(max_length=255)
    vai_Indice = models.BooleanField()
    texto_PadraoAbertura = models.TextField()
    vai_Alteracao = models.BooleanField()
    slug = models.SlugField()

class AssuntoGeral(models.Model):
    descricao = models.CharField(max_length=255)
    parte_Boletim = models.ForeignKey(ParteBoletim,on_delete=models.CASCADE)
    secao_ParteBoletim = models.ForeignKey(SecaoParteBoletim,on_delete=models.CASCADE)
    tipo_Boletim = models.ForeignKey(TipoBoletim,on_delete=models.CASCADE)
    slug = models.SlugField()

class Materia(models.Model):
    data = models.DateField()
    tipo_Documento = models.ForeignKey(TipoDocumento,on_delete=models.CASCADE)
    assunto_Especifico = models.ForeignKey(AssuntoEspecifico, on_delete=models.CASCADE)
    assunto_Geral = models.ForeignKey(AssuntoGeral,on_delete=models.CASCADE)
    texto_Abertura = models.TextField()
    texto_Fechamento = models.TextField()
    numero_Documento = models.IntegerField()
    vai_Alteracao = models.BooleanField()
    aprovada = models.BooleanField()
    data_Documento = models.DateField()
    tipo_Boletim = models.ForeignKey(TipoBoletim,on_delete=models.CASCADE)
    pagina = models.IntegerField()
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)    
    texto_FechamentoVaiAlteracao = models.BooleanField(default=False)
    ordem_Materia = models.IntegerField()
    #descricao_Assunto_Especifico = models.ForeignKey(AssuntoEspecifico, on_delete=models.CASCADE)
    #descricao_Assunto_Geral = models.ForeignKey(AssuntoGeral,on_delete=models.CASCADE)
    '''
    private $codom;
    private $codSubun;
    private $militarAss;
    private $mostraRef;
    '''
    slug = models.SlugField()

class IndiceBoletim(models.Model):
    ''' Classe que contém os dados do índice do boletim '''
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE)
    materia_Boletim =  models.ForeignKey(Materia, on_delete=models.CASCADE)
    slug = models.SlugField()
    '''
    private $boletim;
    private $materiaBi;
    '''
