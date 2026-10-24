from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='entradas')

    def __str__(self):
        return self.titulo