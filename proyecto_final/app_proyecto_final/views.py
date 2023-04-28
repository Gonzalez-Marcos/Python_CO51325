from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  

#Para configuracion de Emails
from django.core.mail import send_mail
from django.conf import settings

#Para configurar alertas en vistas
from django.contrib import messages



# Inicios

def inicioApp(request):

    return render(request, 'inicio.html', {"avatar": obtenerAvatars(request)})

def inicio(request):

    return render(request, 'inicio.html', {"avatar": obtenerAvatars(request)})

def contacto(request):

    return render(request, 'contacto.html', {"avatar": obtenerAvatars(request)})

def about(request):

    return render(request, 'about.html', {"avatar": obtenerAvatars(request)})



def entregables(request):

    if request.method == 'POST':

        formulario = EntregableFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid: #Si pasó la validacion de Django continuo.

            informacion = formulario.cleaned_data

            entregable = Entregable(nombre = informacion['nombre'], fecha_entrega = informacion['fecha_entrega'], entregado = informacion['entregado'])

            entregable.save()

            return render(request, 'inicio.html')
    else:

        formulario = EntregableFormulario()
    
        return render(request, 'entregables.html', {'formulario': formulario})


#<----------------------------------------- Buscador ----------------------------------------->
@login_required
def buscar(request):

    if request.GET:

        nombre = request.GET['nombre']

        estudiantes = Estudiante.objects.filter(nombre__icontains = nombre)

        return render(request, 'busqueda.html', {"estudiantes": estudiantes, "nombre": nombre, "avatar": obtenerAvatars(request)})
    
    else:

        nombre = ""

        if nombre == "":

            respuesta = "No enviaste datos"
            return render(request, 'busqueda.html', {"respuesta": respuesta, "avatar": obtenerAvatars(request)})


#<----------------------------------------- Cursos ----------------------------------------->

@login_required
def cursos(request): #Funcion para crear cursos

        if request.method == 'POST':

            formulario = CursoFormulario(request.POST) #de esta manera llega toda la info desde el html

            print(formulario)

            if formulario.is_valid(): #Si pasó la validacion de Django continuo.

                curso = Curso()
                curso.nombre = formulario.cleaned_data['curso']
                curso.comision = formulario.cleaned_data['comision']
                curso.save()
                messages.success(request, "Curso agregado exitosamente")
                formulario = CursoFormulario()
                cursos = Curso.objects.all()
                
                return render(request, 'cursos/cursos_lista.html', {'cursos': cursos, 'formulario': formulario, "avatar": obtenerAvatars(request)}) 
        else:

           formulario = CursoFormulario()
    
        return render(request, 'cursos/cursos.html', {'formulario': formulario, "avatar": obtenerAvatars(request)})

#Lista Cursos
@login_required
def lista_cursos(request):
    if request.method == "GET":

        cursos = Curso.objects.all()
        
        formulario = CursoFormulario()

        return render(request, "cursos/cursos_lista.html", {"cursos": cursos, "formulario": formulario, "avatar": obtenerAvatars(request)})
    
#Eliminar Cursos
@login_required
def eliminar_curso(request, id):

    curso = Curso.objects.get(id = id)
    print(curso)
    curso.delete()
    messages.success(request, "Eliminado correctamente")
    cursos = Curso.objects.all()
    formulario = CursoFormulario()
    return render(request, 'cursos/cursos_lista.html', {"cursos": cursos, "mensaje": "Curso eliminado", "formulario":formulario, "avatar": obtenerAvatars(request)})

#Editar cursos
@login_required
def editar_curso(request, id):

    curso = Curso.objects.get(id = id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():

            informacion = formulario.cleaned_data
            curso.nombre = informacion['curso']
            curso.comision = informacion['comision']

            curso.save()
            messages.success(request, "Curso modificado")
            cursos = Curso.objects.all()
            formulario = CursoFormulario()

            return render(request, 'cursos/cursos_lista.html', {"cursos": cursos, "mensaje": "Curso modificado exitosamente", "formulario": formulario, "avatar": obtenerAvatars(request)})
    
    else:
        formulario = CursoFormulario(initial={"curso": curso.nombre, "comision": curso.comision})

        return render(request, 'cursos/editar_curso.html', {"formulario": formulario, "curso": curso, "avatar": obtenerAvatars(request)})
    

#<----------------------------------------- Profesores ----------------------------------------->

@login_required
def profesores(request):

    if request.method == 'POST':

        formulario = ProfesorFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid(): #Si pasó la validacion de Django continuo.

                profesor = Profesor()
                profesor.nombre = formulario.cleaned_data['nombre'] 
                profesor.apellido = formulario.cleaned_data['apellido'] 
                profesor.email = formulario.cleaned_data['email']
                profesor.profesion = formulario.cleaned_data['profesion']
                profesor.save()
                messages.success(request, "Profesor creado correctamente")
                formulario = ProfesorFormulario()
                profesores = Profesor.objects.all()


                return render(request, 'profesores/profesores_lista.html', {"profesores": profesores, "formulario": formulario ,"avatar": obtenerAvatars(request)})
        
        else:
                return render(request, 'profesores/profesores.html', {"formulario": formulario, 'mensaje': "Error al enviar el formulario" ,"avatar": obtenerAvatars(request)})
            
    else:

        formulario = ProfesorFormulario()
    
        return render(request, 'profesores/profesores.html', {'formulario': formulario})

#Lista Profesores
@login_required
def lista_profesores(request):

    if request.method == "GET":

        profesores = Profesor.objects.all()
        
        formulario = ProfesorFormulario()

        return render(request, "profesores/profesores_lista.html", {"profesores": profesores, "formulario": formulario, "avatar": obtenerAvatars(request)})
    
#Eliminar Profesor
@login_required
def eliminar_profesor(request, id):

    profesor = Profesor.objects.get(id = id)
    print(profesor)
    profesor.delete()
    messages.success(request, "Eliminado correctamente")
    profesores = Profesor.objects.all()
    formulario = ProfesorFormulario()

    return render(request, 'profesores/profesores_lista.html', {"profesores": profesores, "mensaje": "Profesor eliminado", "formulario": formulario, "avatar": obtenerAvatars(request)})

#Editar Profesor
@login_required
def editar_profesor(request, id):

    profesor = Profesor.objects.get(id = id)

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']


            profesor.save()
            messages.success(request, "Editado correctamente")

            profesores = Profesor.objects.all()
            formulario = ProfesorFormulario()

            return render(request, 'profesores/profesores_lista.html', {"profesores": profesores, "mensaje": "Profesor modificado exitosamente", "formulario": formulario, "avatar": obtenerAvatars(request)})
    else:
        formulario = ProfesorFormulario(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "email": profesor.email, "profesion": profesor.profesion})

        return render(request, 'profesores/editar_profesor.html', {"formulario": formulario, "profesor": profesor, "avatar": obtenerAvatars(request)})


#<----------------------------------------- Estudiantes ----------------------------------------->
@login_required
def estudiantes(request):

    if request.method == 'POST':

        formulario = EstudianteFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid(): #Si pasó la validacion de Django continuo.

            estudiante = Estudiante()
            estudiante.nombre = formulario.cleaned_data['nombre'] 
            estudiante.apellido = formulario.cleaned_data['apellido'] 
            estudiante.email = formulario.cleaned_data['email']
            estudiante.save()

            formulario = EstudianteFormulario()
            estudiantes = Estudiante.objects.all()
            
            return render(request, "estudiantes/estudiantes_lista.html", {"estudiantes": estudiantes, "formulario": formulario, "avatar": obtenerAvatars(request)})

    else:

        formulario = EstudianteFormulario()
    
        return render(request, 'estudiantes/estudiantes.html', {'formulario': formulario, "avatar": obtenerAvatars(request)})

#Lista Estudiantes
@login_required
def lista_estudiantes(request):

    if request.method == "GET":

        estudiantes = Estudiante.objects.all()
        
        formulario = EstudianteFormulario()

        return render(request, "estudiantes/estudiantes_lista.html", {"estudiantes": estudiantes, "formulario": formulario, "avatar": obtenerAvatars(request)})
    
#Eliminar Estudiante
@login_required
def eliminar_estudiante(request, id):

    estudiante = Estudiante.objects.get(id = id)
    print(estudiante)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    formulario = EstudianteFormulario()

    return render(request, 'estudiantes/estudiantes_lista.html', {"estudiantes": estudiantes, "mensaje": "Estudiante eliminado", "formulario": formulario, "avatar": obtenerAvatars(request)})

#Editar Estudiante
@login_required
def editar_estudiante(request, id):

    estudiante = Estudiante.objects.get(id = id)

    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']

            estudiante.save()
            estudiantes = Estudiante.objects.all()
            formulario = EstudianteFormulario()

            return render(request, 'estudiantes/estudiantes_lista.html', {"estudiantes": estudiantes, "mensaje": "Estudiante modificado exitosamente", "formulario": formulario, "avatar": obtenerAvatars(request)})
    else:
        formulario = EstudianteFormulario(initial={"nombre": estudiante.nombre, "apellido": estudiante.apellido, "email": estudiante.email})

        return render(request, 'estudiantes/editar_estudiante.html', {"formulario": formulario, "estudiante": estudiante})


#<----------------------------------------- Login ----------------------------------------->
def login_request(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion['username']
            contrasenia = informacion['password']

            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:

                login(request, user)
                

                return render(request, 'inicio.html', {"mensaje": f"Bienvenido {usuario}", "avatar": obtenerAvatars(request)})
            else:

                return render(request, 'user/login.html', {"formulario": formulario, "mensaje": "Usuario o contraseña incorrecto"})
        
        else:

            return render (request, 'user/login.html', {"formulario": formulario, "mensaje": "Usuario o contraseña incorrecto"})
    else:
        formulario = AuthenticationForm()

    return render(request, 'user/login.html', {'formulario': formulario})

#Editar Perfil
def editarPerfil(request):
    
    usuario = request.user

    if request.method == "POST":

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()

            return render(request, 'inicio.html', {"mensaje": f"Usuario {usuario.username} editado exitosamente.", "avatar": obtenerAvatars(request)})
        else:

            return render(request, 'user/editarPerfil.html', {"formulario": formulario, "nombreusuario": usuario.username, "avatar": obtenerAvatars(request)})
        
    else:

        formulario = UserEditForm(instance = usuario)
                                  
        return render(request, 'user/editarPerfil.html', {"formulario": formulario, "nombreusuario": usuario.username, "avatar": obtenerAvatars(request)})


#<----------------------------------------- Register ----------------------------------------->
def register(request):

    if request.method=="POST":

        formulario = RegistroUsuarioForm(request.POST)

        if formulario.is_valid():

            username= formulario.cleaned_data.get("username")

            formulario.save()

            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        
        else:
            return render(request, "user/register.html", {"formulario": formulario, "mensaje":"Error al crear el usuario"})
    else:
        formulario= RegistroUsuarioForm()
        
        return render(request, "user/register.html", {"formulario": formulario})

@login_required
#<----------------------------------------- Avatars ----------------------------------------->
def obtenerAvatars(request):

    avatares = Avatar.objects.filter(user = request.user.id)

    if len(avatares) != 0:

        return avatares[0].imagen.url
    
    else:

        return "/media/Avatars/lAwxR.png"

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        formulario=AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)

            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            usuario = request.user
            formulario = UserEditForm(instance = usuario)

            return render(request, "user/editarPerfil.html", {"formulario": formulario, "mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatars(request)})
        else:
            return render(request, "agregarAvatar.html", {"formulario": formulario, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        formulario=AvatarForm()
        return render(request, "user/agregarAvatar.html", {"formulario": formulario, "usuario": request.user, "avatar":obtenerAvatars(request)})

#<----------------------------------------- Inscripciones ----------------------------------------->

def inscripciones(request):

    if request.method == "POST":

        form = FormularioInscripcion(request.POST)
        
        if form.is_valid():

            informacion = form.cleaned_data 

            nombre = informacion["nombre"]
            email = informacion["email"]
            telefono = informacion["telefono"]
            mensaje = informacion["mensaje"]

            subject = "Solicitud de Inscripción"

            message = request.POST["nombre"] + "\n " + request.POST["email"] + "\n" + request.POST["telefono"] + "\n " + request.POST["mensaje"]

            email_from = settings.EMAIL_HOST_USER

            recipient_list = ["programmer.gonzalezmarcos@gmail.com"] 

            send_mail(subject, message, email_from, recipient_list)

            messages.success(request, "Nos pondremos en contacto a la brevedad. Gracias")

            form = FormularioInscripcion()

            return render(request, 'inscripciones.html', {"form": form, "avatar": obtenerAvatars(request)})
        
    form = FormularioInscripcion()
    return render(request, 'inscripciones.html', {"form": form, "avatar": obtenerAvatars(request)})

