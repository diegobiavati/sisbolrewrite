from django.contrib import admin
from .models import Materia,TipoDocumento,PessoaMateriaBoletim,AssuntoEspecifico,AssuntoGeral

# Register your models here.
@admin.register(PessoaMateriaBoletim)
class PessoaMateriaBoletimA(admin.ModelAdmin):
    pass

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    pass

@admin.register(AssuntoEspecifico)
class AssuntoEspecificoAdmin(admin.ModelAdmin):
    pass

@admin.register(AssuntoGeral)
class AssuntoGeralAdmin(admin.ModelAdmin):
    pass

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    pass