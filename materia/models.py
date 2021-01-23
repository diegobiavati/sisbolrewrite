from django.db import models
from boletim.models import ParteBoletim,SecaoParteBoletim,TipoBoletim

class TipoDocumento(models.Model):
    descricao = models.CharField(max_length=255)
    slug = models.SlugField()

class AssuntoEspecifico(models.Model):
    descricao = models.CharField(max_length=255)
    vaiIndice = models.BooleanField()
    textoPadraoAbertura = models.TextField()
    vaiAlteracao = models.BooleanField()
    slug = models.SlugField()

class AssuntoGeral(models.Model):
    descricao = models.CharField(max_length=255)
    parteBoletim = models.ForeignKey(ParteBoletim,on_delete=models.CASCADE)
    secaoParteBoletim = models.ForeignKey(SecaoParteBoletim,on_delete=models.CASCADE)
    tipoBoletim = models.ForeignKey(TipoBoletim, on_delete=models.CASCADE)
    slug = models.SlugField()

# Create your models here.
class Materia(models.Model):
    data = models.DateField()
    tipoDocumento = models.ForeignKey(TipoDocumento,on_delete=models.CASCADE)
    assuntoEspecifico = models.ForeignKey(AssuntoEspecifico, on_delete=models.CASCADE)
    assuntoGeral = models.ForeignKey(AssuntoGeral, on_delete=models.CASCADE)
    textoAbertura = models.TextField()
    textoFechamento = models.TextField()
    numeroDocumento = models.IntegerField()
    vaiAlteracao = models.BooleanField()
    aprovada = models.BooleanField()
    dataDocumento = models.DateField()
    tipoBoletim = models.ForeignKey(TipoBoletim, on_delete=models.CASCADE)
    pagina = models.IntegerField()
    slug = models.SlugField()
    
    '''
    private $descrAssEsp;
    private $descrAssGer;
    private $usuario;
    private $codom;
    private $codSubun;
    private $ord_mat;
    private $militarAss;
    private $mostraRef;
    private $textoFechVaiAltr;
    '''