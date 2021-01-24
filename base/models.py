import datetime
from django.db import models

def selecao_anos():
    return [(r,r) for r in range(datetime.date.today().year-10, datetime.date.today().year+2)]

def ano_atual():
    return datetime.date.today().year

class OrganizacaoMilitar(models.Model):
	nome = models.CharField(max_length=250)
	sigla = models.CharField(max_length=250)
	designacao_Historica = models.CharField(max_length=250)
	subordinacao_1 = models.CharField(max_length=250)
	sobordinacao_2 = models.CharField(max_length=250)
	subordinacao_3 = models.CharField(max_length=250)
	subordinacao_4 = models.CharField(max_length=250)
	guarnicao = models.CharField(max_length=250)
	codom = models.IntegerField(unique=True)
	ano_Corrente = models.IntegerField(choices=selecao_anos(), default=ano_atual())
	slug = models.SlugField()

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
	slug = models.SlugField()