from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #blog
    path('blog/', vista_post, name="blog"),

    #Comentarios
    path('comentarios/<id>', comentario, name = "comentarios"),

    #Post
    path('nuevoPost/', postBlog, name='nuevoPost'),

    #detallePost/comentario
    path('detalleBlog/<id>', detalleBlog, name='detalleBlog')


]