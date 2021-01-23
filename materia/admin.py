from django.contrib import admin
from .models import Materia,TipoDocumento,PessoaMateriaBoletim

# Register your models here.
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    pass

@admin.register(PessoaMateriaBoletim)
class PessoaMateriaBoletimA(admin.ModelAdmin):
    pass

