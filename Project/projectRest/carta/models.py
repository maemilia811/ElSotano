from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.CharField(max_length=200, verbose_name='Descripción')
    price = models.IntegerField(verbose_name='Precio')
    image = models.ImageField(upload_to="projects", verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'proyecto'
    verbose_name_plural = 'proyectos'
    ordering = ['-created']