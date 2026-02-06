from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='servicios/')
    icono = models.CharField(max_length=50, help_text="Clase de FontAwesome (ej: fa-solid fa-bed)")
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/')
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class ExperienciaAliada(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='aliados/')
    enlace = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
    
    from django.db import models

# Modelo para el Blog
class ArticuloBlog(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    imagen = models.ImageField(upload_to='blog/', verbose_name="Foto Principal")
    contenido = models.TextField(verbose_name="Contenido del Artículo")
    fecha_publicacion = models.DateField(auto_now_add=True, verbose_name="Fecha")

    class Meta:
        verbose_name = "Artículo del Blog"
        verbose_name_plural = "Blog - Noticias"
        ordering = ['-fecha_publicacion'] # Lo más nuevo primero

    def __str__(self):
        return self.titulo

# Modelo para los Servicios (Hospedaje, Pasadías, etc.)
class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion_corta = models.CharField(max_length=200, help_text="Texto corto para la tarjeta del inicio")
    imagen = models.ImageField(upload_to='servicios/')
    enlace_html = models.CharField(max_length=50, default="hospedaje.html", help_text="Nombre del archivo HTML al que lleva (ej: hospedaje.html)")
    orden = models.IntegerField(default=0, help_text="Número para ordenar (1 sale primero, 2 segundo...)")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios del Inicio"
        ordering = ['orden']

    def __str__(self):
        return self.titulo