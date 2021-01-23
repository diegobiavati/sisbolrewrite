from django.contrib import admin
from .models import Pessoa

# Register your models here.
@admin.register(Pessoa)
class RegisterAdmin(admin.ModelAdmin):
    pass