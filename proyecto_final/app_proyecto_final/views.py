from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm, PasswordChangeForm
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


#<----------------------------------------- Buscadores ----------------------------------------->
@login_required
def buscarSala(request):

    if request.method == "GET":

        nombre = request.GET['nombre']

        salas = Sala.objects.filter(nombre__icontains = nombre)

        return render(request, 'salas/buscar_sala.html', {"salas": salas, "nombre": nombre, "avatar": obtenerAvatars(request)})
    
    else:

        nombre = ""

        if nombre == "":

            respuesta = "No enviaste datos"
            return render(request, 'salas/buscar_sala.html', {"respuesta": respuesta, "avatar": obtenerAvatars(request)})

@login_required
def buscarAlumno(request):

    if request.method == "GET":

        dni = request.GET['dni']

        alumnos = Alumno.objects.filter(dni=dni)

        return render(request, 'alumnos/buscar_alumno.html', {"alumnos": alumnos, "dni": dni, "avatar": obtenerAvatars(request)})
    
    else:

        if dni == "":

            respuesta = "No enviaste datos"
            return render(request, 'alumnos/buscar_alumno.html', {"respuesta": respuesta, "avatar": obtenerAvatars(request)})


@login_required
def buscarDocente(request):

    if request.method == "GET":

        apellido = request.GET['apellido']

        docentes = Docente.objects.filter(apellido__icontains = apellido)

        return render(request, 'docentes/buscar_docente.html', {"docentes": docentes, "apellido": apellido, "avatar": obtenerAvatars(request)})
    
    else:

        apellido = ""

        if apellido == "":

            respuesta = "No enviaste datos"
            return render(request, 'docentes/buscar_docente.html', {"respuesta": respuesta, "avatar": obtenerAvatars(request)})
        

#<----------------------------------------- Salas ----------------------------------------->

@login_required
def salas(request): #Funcion para crear cursos

        if request.method == 'POST':

            formulario = SalasFormulario(request.POST) #de esta manera llega toda la info desde el html

            print(formulario)

            if formulario.is_valid(): #Si pasó la validacion de Django continuo.

                sala = Sala()
                sala.nivel = formulario.cleaned_data['nivel']
                sala.nombre = formulario.cleaned_data['nombre']
                sala.save()
                messages.success(request, "Curso agregado exitosamente")
                formulario = SalasFormulario()
                salas = Sala.objects.all()
                
                return render(request, 'salas/salas_lista.html', {'salas': salas, 'formulario': formulario, "avatar": obtenerAvatars(request)}) 
        else:

           formulario = SalasFormulario()
    
        return render(request, 'salas/salas.html', {'formulario': formulario, "avatar": obtenerAvatars(request)})

#Lista Salas
@login_required
def lista_salas(request):
    if request.method == "GET":

        salas = Sala.objects.all()
        
        formulario = SalasFormulario()

        return render(request, "salas/salas_lista.html", {"salas": salas, "formulario": formulario, "avatar": obtenerAvatars(request)})
    
#Eliminar Salas
@login_required
def eliminar_sala(request, id):

    sala = Sala.objects.get(id = id)
    print(sala)
    sala.delete()
    messages.success(request, "Eliminado correctamente")
    salas = Sala.objects.all()
    formulario = SalasFormulario()
    return render(request, 'salas/salas_lista.html', {"salas": salas, "mensaje": "Curso eliminado", "formulario":formulario, "avatar": obtenerAvatars(request)})

#Editar Salas
@login_required
def editar_sala(request, id):

    sala = Sala.objects.get(id = id)
    if request.method == "POST":
        formulario = SalasFormulario(request.POST)
        if formulario.is_valid():

            informacion = formulario.cleaned_data
            sala.nivel = informacion['nivel']
            sala.nombre = informacion['nombre']

            sala.save()
            messages.success(request, "Sala modificada")
            salas = Sala.objects.all()
            formulario = SalasFormulario()

            return render(request, 'salas/salas_lista.html', {"salas": salas, "mensaje": "Sala modificada exitosamente", "formulario": formulario, "avatar": obtenerAvatars(request)})
    
    else:
        formulario = SalasFormulario(initial={"nivel": sala.nivel, "nombre": sala.nombre})

        return render(request, 'salas/editar_sala.html', {"formulario": formulario, "sala": sala, "avatar": obtenerAvatars(request)})
    

#<----------------------------------------- Docentes ----------------------------------------->

@login_required
def docentes(request):

    if request.method == 'POST':

        formulario = DocenteFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid(): #Si pasó la validacion de Django continuo.

                docente = Docente()
                docente.nombre = formulario.cleaned_data['nombre'] 
                docente.apellido = formulario.cleaned_data['apellido'] 
                docente.email = formulario.cleaned_data['email']
                docente.telefono = formulario.cleaned_data['telefono']
                docente.save()
                messages.success(request, "Docente creado correctamente")
                formulario = DocenteFormulario()
                docentes = Docente.objects.all()


                return render(request, 'docentes/docentes_lista.html', {"docentes": docentes, "formulario": formulario ,"avatar": obtenerAvatars(request)})
        
        else:
                return render(request, 'docentes/docentes.html', {"formulario": formulario, 'mensaje': "Error al enviar el formulario" ,"avatar": obtenerAvatars(request)})
            
    else:

        formulario = DocenteFormulario()
    
        return render(request, 'docentes/docentes.html', {'formulario': formulario, "avatar": obtenerAvatars(request)})

#Lista Docentes
@login_required
def lista_docentes(request):

    if request.method == "GET":

        docentes = Docente.objects.all()
        
        formulario = DocenteFormulario()

        return render(request, "docentes/docentes_lista.html", {"docentes": docentes, "formulario": formulario, "avatar": obtenerAvatars(request)})
    
#Eliminar Docente
@login_required
def eliminar_docente(request, id):

    docente = Docente.objects.get(id = id)
    print(docente)
    docente.delete()
    messages.success(request, "Eliminado correctamente")
    docentes = Docente.objects.all()
    formulario = DocenteFormulario()

    return render(request, 'docentes/docentes_lista.html', {"docentes": docentes, "mensaje": "Docente eliminado", "formulario": formulario, "avatar": obtenerAvatars(request)})

#Editar Docente
@login_required
def editar_docente(request, id):

    docente = Docente.objects.get(id = id)

    if request.method == "POST":
        formulario = DocenteFormulario(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            docente.nombre = informacion['nombre']
            docente.apellido = informacion['apellido']
            docente.email = informacion['email']
            docente.telefono = informacion['telefono']


            docente.save()
            messages.success(request, "Editado correctamente")

            docentes = Docente.objects.all()
            formulario = DocenteFormulario()

            return render(request, 'docentes/docentes_lista.html', {"docentes": docentes, "mensaje": "Docente modificado exitosamente", "formulario": formulario, "avatar": obtenerAvatars(request)})
    else:
        formulario = DocenteFormulario(initial={"nombre": docente.nombre, "apellido": docente.apellido, "email": docente.email, "telefono": docente.telefono})

        return render(request, 'docentes/editar_docente.html', {"formulario": formulario, "docente": docente, "avatar": obtenerAvatars(request)})


#<----------------------------------------- Alumnos ----------------------------------------->
@login_required
def alumnos(request):

    if request.method == 'POST':

        formulario = AlumnoFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid(): #Si pasó la validacion de Django continuo.

            alumno = Alumno()
            alumno.nombre = formulario.cleaned_data['nombre'] 
            alumno.apellido = formulario.cleaned_data['apellido'] 
            alumno.dni = formulario.cleaned_data['dni']
            alumno.save()
            messages.success(request, "Alumno creado correctamente")
            formulario = AlumnoFormulario()
            alumnos = Alumno.objects.all()
            
            return render(request, "alumnos/alumnos_lista.html", {"alumnos": alumnos, "formulario": formulario, "avatar": obtenerAvatars(request)})

    else:

        formulario = AlumnoFormulario()
    
        return render(request, 'alumnos/alumnos.html', {'formulario': formulario, "avatar": obtenerAvatars(request)})

#Lista Alumnos
@login_required
def lista_alumnos(request):

    if request.method == "GET":

        alumnos = Alumno.objects.all()
        
        formulario = AlumnoFormulario()

        return render(request, "alumnos/alumnos_lista.html", {"alumnos": alumnos, "formulario": formulario, "avatar": obtenerAvatars(request)})
    
#Eliminar Alumnos
@login_required
def eliminar_alumno(request, id):

    alumno = Alumno.objects.get(id = id)
    print(alumno)
    alumno.delete()
    messages.success(request, "Eliminado correctamente")
    alumnos = Alumno.objects.all()
    formulario = AlumnoFormulario()

    return render(request, 'alumnos/alumnos_lista.html', {"alumnos": alumnos, "mensaje": "Estudiante eliminado", "formulario": formulario, "avatar": obtenerAvatars(request)})

#Editar Alumnos
@login_required
def editar_alumno(request, id):

    alumno = Alumno.objects.get(id = id)

    if request.method == "POST":
        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            alumno.nombre = informacion['nombre']
            alumno.apellido = informacion['apellido']
            alumno.dni = informacion['dni']

            alumno.save()
            messages.success(request, "Editado correctamente")
            alumnos = Alumno.objects.all()
            formulario = AlumnoFormulario()

            return render(request, 'alumnos/alumnos_lista.html', {"alumnos": alumnos, "mensaje": "Estudiante modificado exitosamente", "formulario": formulario, "avatar": obtenerAvatars(request)})
    else:
        formulario = AlumnoFormulario(initial={"nombre": alumno.nombre, "apellido": alumno.apellido, "dni": alumno.dni})

        return render(request, 'alumnos/editar_alumno.html', {"formulario": formulario, "alumno": alumno})


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

#Cambiar Password
@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = CambioPassword(request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            formulario = AuthenticationForm()
            return render(request, 'user/login.html', {'formulario': formulario, "avatar": obtenerAvatars(request)} )
    else:
        form = CambioPassword(user=request.user)
    return render(request, 'user/cambioPassword.html', {'form': form, "avatar": obtenerAvatars(request)})
    

#Editar Perfil
def editarPerfil(request):
    
    usuario = request.user

    if request.method == "POST":

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.save()

            return render(request, 'inicio.html', {"mensaje": f"Usuario {usuario.username} editado exitosamente.", "avatar": obtenerAvatars(request)})
        else:

            return render(request, 'user/editarPerfil.html', {"formulario": formulario, "nombreusuario": usuario.username, "avatar": obtenerAvatars(request)})
        
    else:

        formulario = UserEditForm(instance = usuario)
                                  
        return render(request, 'user/editarPerfil.html', {"formulario": formulario, "nombreusuario": usuario.username, "avatar": obtenerAvatars(request)})


#<----------------------------------------- Register/Super User ----------------------------------------->
def register(request):

    if request.method=="POST":

        formulario = RegistroUsuarioForm(request.POST, request.FILES)

        if formulario.is_valid():

            username= formulario.cleaned_data.get("username")

            formulario.save()

            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        
        else:
            return render(request, "user/register.html", {"formulario": formulario, "mensaje":"Error al crear el usuario"})
    else:
        formulario= RegistroUsuarioForm()
        
        return render(request, "user/register.html", {"formulario": formulario})

#Lista de Usuarios registrados
@login_required
def lista_usuarios(request):

    if request.method == "GET":

        usuarios = User.objects.all().order_by('-is_superuser')
        
        formulario = AlumnoFormulario()

        return render(request, "user/lista_usuarios.html", {"usuarios": usuarios, "formulario": formulario, "avatar": obtenerAvatars(request)})


def crearUser(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        form = SuperUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            is_superuser = form.cleaned_data.get('is_superuser', False)

            # Crear el objeto de usuario y establecer los atributos
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            user.is_superuser = is_superuser

            # Guardar el objeto de usuario en la base de datos
            user.save()
            messages.success(request, "Usuario creado correctamente")


            return  render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente", "avatar": obtenerAvatars(request)})
    else:
        # Mostrar el formulario para crear el superusuario
        form = SuperUsuarioForm()

    return render(request, 'user/crear_superusuario.html', {'form': form, "avatar": obtenerAvatars(request)})


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

