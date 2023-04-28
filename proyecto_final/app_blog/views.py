from django.shortcuts import render
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

# Create your views here.


#<----------------------------------------- Comentarios ----------------------------------------->
def comentario(request, id):

    post = PostBlog.objects.get(id=id)

    if request.method == 'POST':

        formulario = FormularioComentario(request.POST)

        if formulario.is_valid():

            nuevo_comentario = Comentario(
            nombre=formulario.cleaned_data['nombre'],
            texto=formulario.cleaned_data['texto'],
            usuario=request.user,  # agregamos el usuario que hizo el comentario
            post_id = id
            )
            nuevo_comentario.save()
            comentarios = Comentario.objects.all().order_by('-fechaComentario')
            formulario = FormularioComentario()

            return render(request, 'detalleBlog.html', {"formulario": formulario, 'post': post, "comentarios": comentarios, "avatar": obtenerAvatars(request)})
    else:
        formulario = FormularioComentario()
        comentarios = Comentario.objects.all().order_by('-fechaComentario')
        posts = [post]

        return render(request, 'detalleBlog.html',{'formulario': formulario, 'post': posts, 'comentarios': comentarios, "avatar": obtenerAvatars(request)})

def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'inicioBlog.html', {'comentarios': comentarios, "avatar": obtenerAvatars(request)})


def postBlog(request):

    if request.method == 'POST':

        formulario = FormularioPost(request.POST, request.FILES)

        if formulario.is_valid():

            post = PostBlog()
            post.imagen=formulario.cleaned_data['imagen']
            post.text=formulario.cleaned_data['text']
            post.usuario = request.user
            post.save()
            formulario = FormularioPost()
            posts = PostBlog.objects.all()

            return render(request, 'comentario.html', {"formulario": formulario, 'posts': posts, "avatar": obtenerAvatars(request)})
        
        else:
            return render(request, 'postBlog.html', {"formulario": formulario, "avatar": obtenerAvatars(request)})
        
    else:
            formulario = FormularioPost()
            
            return render(request, 'postBlog.html',{'formulario': formulario, "avatar": obtenerAvatars(request)})
    
def vista_post(request):
     
    posts = PostBlog.objects.all()

    return render(request, 'inicioBlog.html', {'posts': posts, "avatar": obtenerAvatars(request)})

def detalleBlog(request, id):

    post = PostBlog.objects.get(id = id)
    formulario = FormularioComentario()
    comentarios = Comentario.objects.all()

    return render(request, 'detalleBlog.html', {'formulario': formulario,'comentarios': comentarios, 'post': post, "avatar": obtenerAvatars(request)})