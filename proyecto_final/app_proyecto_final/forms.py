from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(min_length = 3, max_length = 15)

    comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)

    apellido = forms.CharField(max_length=30)

    email = forms.EmailField()

    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)

    apellido = forms.CharField(max_length=30)

    email = forms.EmailField()

class EntregableFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)

    fecha_entrega = forms.DateField(help_text= "Formato de la fecha debe ser: aaaa/mm/dd")

    entregado = forms.BooleanField()