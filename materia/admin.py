from django.contrib import admin
from .models import Materia, TipoDocumento

# Register your models here.
@admin.register(Materia)
class Materia(admin.ModelAdmin):
    pass