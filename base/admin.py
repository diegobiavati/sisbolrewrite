'''
Módulo que contém os dados bases para o sistema
'''
from django.contrib import admin
from .models import Pessoa,OrganizacaoMilitar

@admin.register(OrganizacaoMilitar)
class OrganizacaoMilitarAdmin(admin.ModelAdmin):
    ''' Classe Administravia para os dados das Organizações Militares '''

@admin.register(Pessoa)
class RegisterAdmin(admin.ModelAdmin):
    ''' Classe Adminsitravida para os dados das Pessoas que terão matérias publicadas '''
