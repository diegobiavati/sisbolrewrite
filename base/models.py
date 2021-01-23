from django.db import models

# Create your models here.
class Pessoa(models.Model):
	SEXOS = [
		("F", "Feminino"),
		("M", "Masculino"),
		("N", "Nenhuma das opções"),
	]
	identidade = models.CharField(max_length=250)
	funcao = models.CharField(max_length=250)
	nome_Completo = models.CharField(max_length=250)
	nome_Guerra = models.CharField(max_length=250)
	slug = models.SlugField()
	sexo = models.CharField(max_length=1, choices=SEXOS, blank=False, null=False)

'''private $id_militar;
	private $funcao;
	private $nome;
	private $nome_guerra;
	private $dataNasc;
	private $nome_pai;
	private $nome_mae;
	private $cpf;
	private $pis_pasep;
	private $data_atualiz;
	private $sexo;
	private $perm_pub_bi;
	private $omVinc;
	private $subun;
	'''