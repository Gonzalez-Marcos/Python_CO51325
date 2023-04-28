from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', inicioApp, name = "inicioApp"),
    path('buscar/', buscar, name = "buscar"),
    path('contacto/', contacto, name = "contacto"),
    path('about/', about, name = "about"),

    path('entregables/', entregables, name = "entregables"),

    #Cursos
    path('cursos/', cursos, name = "cursos"),
    path('cursos/lista', lista_cursos, name = "listaCursos"),
    path('eliminarCurso/<id>', eliminar_curso, name= "eliminarCurso"),
    path('editarCurso/<id>', editar_curso, name= "editarCurso"),

    #Profesores
    path('profesores/', profesores, name = "profesores"),
    path('profesores/lista', lista_profesores, name = "listaProfesores"),
    path('eliminarProfesor/<id>', eliminar_profesor, name= "eliminarProfesor"),
    path('editarProfesor/<id>', editar_profesor, name= "editarProfesor"),

    #Estudiantes
    path('estudiantes/', estudiantes, name = "estudiantes"),
    path('estudiantes/lista', lista_estudiantes, name = "listaEstudiantes"),
    path('eliminarEstudiante/<id>', eliminar_estudiante, name= "eliminarEstudiante"),
    path('editarEstudiante/<id>', editar_estudiante, name= "editarEstudiante"),
    
    #Login/Logout/Register
    path('login/', login_request, name = "login"),
    path('register/', register, name = 'register'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('editarPerfil/', editarPerfil, name = 'editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),

    #Incripciones y Comentarios
    path('inscripciones/', inscripciones, name = "inscripciones"),

]