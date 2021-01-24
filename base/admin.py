from django.contrib import admin
from .models import Pessoa,OrganizacaoMilitar

@admin.register(OrganizacaoMilitar)
class OrganizacaoMilitarAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class RegisterAdmin(admin.ModelAdmin):
    pass