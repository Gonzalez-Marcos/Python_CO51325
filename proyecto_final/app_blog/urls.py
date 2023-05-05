from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #blog
    path('blogs/', vista_post, name="blog"),

    #Post
    path('nuevoPost/', postBlog, name='nuevoPost'),

    #detallePost/comentario
    path('post/<int:id>/', detalle_blog, name='detalleBlog')


]