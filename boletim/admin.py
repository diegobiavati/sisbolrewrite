from django.contrib import admin
from .models import Boletim, TipoBoletim, ParteBoletim, SecaoParteBoletim

# Register your models here.
@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    date_hierarchy = 'data_Publicacao'

@admin.register(TipoBoletim)
class TipoBIAdmin(admin.ModelAdmin):
    pass

@admin.register(ParteBoletim)
class ParteBoletim(admin.ModelAdmin):
    pass

@admin.register(SecaoParteBoletim)
class SecaoParteBoletim(admin.ModelAdmin):
    pass