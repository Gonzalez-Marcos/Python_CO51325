from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *

from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  

from app_proyecto_final.models import Avatar #Traigo los avatar de la otra App
from app_proyecto_final.views import obtenerAvatars #Traigo los avatar de la otra App


#Para configurar alertas en vistas
from django.contrib import messages


#<----------------------------------------- Comentarios ----------------------------------------->
@login_required
def postBlog(request):

    if request.method == 'POST':

        formulario = FormularioPost(request.POST, request.FILES)

        if formulario.is_valid():

            post = PostBlog()
            post.imagen=formulario.cleaned_data['imagen']
            post.titulo=formulario.cleaned_data['titulo']
            post.texto=formulario.cleaned_data['texto']
            post.usuario = request.user
            post.save()
            formulario = FormularioPost()
            posts_list = PostBlog.objects.all().order_by('-fechaPost')

            return render(request, 'inicioBlog.html', {"formulario": formulario, 'posts': posts_list, "avatar": obtenerAvatars(request)})
        
        else:
            return render(request, 'postBlog.html', {"formulario": formulario, "avatar": obtenerAvatars(request)})
        
    else:
            formulario = FormularioPost()
            
            return render(request, 'postBlog.html',{'formulario': formulario, "avatar": obtenerAvatars(request)})
    
def vista_post(request):
     
    posts = PostBlog.objects.all().order_by('-fechaPost')

    return render(request, 'inicioBlog.html', {'posts': posts, "avatar": obtenerAvatars(request)})

def detalle_blog(request, id):
    post = PostBlog.objects.get(id=id)
    comentarios = post.comentarios.all()
    total_comentarios = comentarios.count() + 1 # obtenemos el total de comentarios
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.usuario = request.user
            nuevo_comentario.post = post
            nuevo_comentario.save()
            comentario_form = ComentarioForm()

            return render(request, 'detalleBlog.html', {'post': post, 'comentarios': comentarios, 
                        'comentario_form': comentario_form, 'id': str(id),"totalComentario": total_comentarios, "avatar": obtenerAvatars(request)})
    else:
        comentario_form = ComentarioForm()
    return render(request, 'detalleBlog.html', {'post': post, 'comentarios': comentarios, 'comentario_form': comentario_form, 'id': str(id),"totalComentario": total_comentarios, "avatar": obtenerAvatars(request)})
