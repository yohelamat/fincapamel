from django.contrib import admin
from .models import ArticuloBlog, Servicio

# Configuración para el Blog
@admin.register(ArticuloBlog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)

# Configuración para los Servicios
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')
    ordering = ['orden']