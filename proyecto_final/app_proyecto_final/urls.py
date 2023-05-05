from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', inicioApp, name = "inicioApp"),
    path('contacto/', contacto, name = "contacto"),
    path('about/', about, name = "about"),

    #Salas
    path('salas/', salas, name = "salas"),
    path('salas/lista', lista_salas, name = "listaSalas"),
    path('eliminarSala/<id>', eliminar_sala, name= "eliminarSala"),
    path('editarSala/<id>', editar_sala, name= "editarSala"),
    path('buscarSala/', buscarSala, name = "buscarSala"),

    #Docentes
    path('docentes/', docentes, name = "docentes"),
    path('docentes/lista', lista_docentes, name = "listaDocentes"),
    path('eliminarDocente/<id>', eliminar_docente, name= "eliminarDocente"),
    path('editarDocente/<id>', editar_docente, name= "editarDocente"),
    path('buscarDocente/', buscarDocente, name = "buscarDocente"),


    #Alumnos
    path('alumnos/', alumnos, name = "alumnos"),
    path('alumnos/lista', lista_alumnos, name = "listaAlumnos"),
    path('eliminarAlumno/<id>', eliminar_alumno, name= "eliminarAlumno"),
    path('editarAlumno/<id>', editar_alumno, name= "editarAlumno"),
    path('buscarAlumno/', buscarAlumno, name = "buscarAlumno"),
    
    #Login/Logout/Register
    path('login/', login_request, name = "login"),
    path('register/', register, name = 'register'),
    path('crearUser/', crearUser, name = 'crearUser'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('editarPerfil/', editarPerfil, name = 'editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('cambiar-contrasena/', cambiar_contrasena, name='cambiar_contrasena'),

    #Incripciones y Comentarios
    path('inscripciones/', inscripciones, name = "inscripciones"),

    #Lista Usuarios Registrados
    path('listaUsuarios/', lista_usuarios, name= "listaUsuarios")

]