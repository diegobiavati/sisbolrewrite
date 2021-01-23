from django.contrib import admin
from .models import Boletim, TipoBoletim

# Register your models here.
@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    date_hierarchy = 'dataPublicacao'

@admin.register(TipoBoletim)
class TipoBIAdmin(admin.ModelAdmin):
    pass
