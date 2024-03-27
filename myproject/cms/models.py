from django.db import models

# Create your models here.

class Contenido(models.Model):
    clave = models.CharField(max_length = 64)
    valor = models.TextField()

    def __str__(self):
        return self.clave


class Comentario(models.Model):
    titulo = models.CharField(max_length = 200)
    # Cuerpo = comentario del usuario
    cuerpo = models.TextField(blank = False)
    fecha = models.DateTimeField("publicado")
    contenido = models.ForeignKey(Contenido, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo + " --> " + self.contenido.__str__()