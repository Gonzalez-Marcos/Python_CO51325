from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.


def cursos(request): #Funcion para crear cursos

    if request.method == 'POST':

        formulario = CursoFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid: #Si pasó la validacion de Django continuo.

            informacion = formulario.cleaned_data

            curso = Curso(nombre = informacion['curso'], comision = informacion['comision'])

            curso.save()

            return render(request, 'inicio.html')
    else:

        formulario = CursoFormulario()
    
    return render(request, 'cursos.html', {'formulario': formulario})
       

def profesores(request):

    if request.method == 'POST':

        formulario = ProfesorFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid: #Si pasó la validacion de Django continuo.

            informacion = formulario.cleaned_data

            profesor = Profesor(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion = informacion['profesion'])

            profesor.save()

            return render(request, 'inicio.html')
    else:

        formulario = ProfesorFormulario()
    
        return render(request, 'profesores.html', {'formulario': formulario})


def estudiantes(request):

    if request.method == 'POST':

        formulario = EstudianteFormulario(request.POST) #de esta manera llega toda la info desde el html

        print(formulario)

        if formulario.is_valid: #Si pasó la validacion de Django continuo.

            informacion = formulario.cleaned_data

            estudiante = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])

            estudiante.save()

            return render(request, 'inicio.html')
    else:

        formulario = EstudianteFormulario()
    
        return render(request, 'estudiantes.html', {'formulario': formulario})

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

def buscar(request):

    if request.GET:

        comision = request.GET['comision']

        
        
        cursos = Curso.objects.filter(comision__icontains = comision)

        return render(request, 'busqueda.html', {"cursos": cursos, "comision": comision})
    
    else:

        comision = ""

        if comision == "":

            respuesta = "No enviaste datos"
            return render(request, 'busqueda.html', {"respuesta": respuesta})

def inicio(request):

    return render(request, 'inicio.html')

def inicioApp(request):

    return render(request, 'inicio.html')
