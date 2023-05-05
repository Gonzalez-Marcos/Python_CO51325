from django.db import models

from django.contrib.auth.models import User

class PostBlog(models.Model):
    imagen = models.ImageField(null=True, blank=True,upload_to='imagenes/')
    titulo = models.TextField(max_length=200)
    texto = models.TextField(max_length=200)
    usuario = models.ForeignKey(User, related_name='postBlog', on_delete=models.CASCADE, null=True)
    fechaPost = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.fechaPost}"
   
class Comentario(models.Model):
    usuario = models.ForeignKey(User, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    texto = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(PostBlog, related_name='comentarios', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return f"{self.nombre} - {self.texto}"

