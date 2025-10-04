from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True, null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo