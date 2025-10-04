from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Proyecto  # importar el modelo

# Registrar el modelo para que aparezca en el admin
admin.site.register(Proyecto)
