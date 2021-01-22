from django.db import models

class TipoDocumento(models.Model):
    descricao = models.CharField(max_length=255)

# Create your models here.
class Materia(models.Model):
    data = models.DateField()
    tipoDocumento = models.ForeignKey(TipoDocumento,on_delete=models.CASCADE)

    '''
    private $tipoDoc;
    private $assuntoEspec;
    private $assuntoGeral;
    private $textoAbert;
    private $textoFech;
    private $nrDocumento;
    private $vaiAltr;
    private $aprovada;
    private $descrAssEsp;
    private $descrAssGer;
    private $dataDoc;
    private $tipoBol;
    private $pagina;
    private $usuario;
    private $codom;
    private $codSubun;
    private $ord_mat;
    private $militarAss;
    private $mostraRef;
    private $textoFechVaiAltr;
    '''