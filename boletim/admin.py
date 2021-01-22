from django.contrib import admin
from .models import Boletim, TipoBI

# Register your models here.
@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    date_hierarchy = 'dataPublicacao'

@admin.register(TipoBI)
class TipoBIAdmin(admin.ModelAdmin):
    pass
