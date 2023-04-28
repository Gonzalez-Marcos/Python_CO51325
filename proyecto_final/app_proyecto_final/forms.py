from django import forms

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#Funcion para almacenar primer letra en mayúscula
class ToUpperField(forms.CharField):
    def to_python(self, value):
        return value.title()

class CursoFormulario(forms.Form):

    curso = ToUpperField(min_length=3, max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))

    comision = forms.IntegerField()



class ProfesorFormulario(forms.Form):

    nombre = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    apellido = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField()

    profesion = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))



class EstudianteFormulario(forms.Form):

    nombre = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    apellido = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField()



class EntregableFormulario(forms.Form):

    nombre = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    fecha_entrega = forms.DateField(help_text= "Formato de la fecha debe ser: aaaa/mm/dd")

    entregado = forms.BooleanField()



class RegistroUsuarioForm(UserCreationForm):
    
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    first_name = ToUpperField(max_length=20, label='Nombre', required= None, widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name = ToUpperField(max_length=20, label='Apellido', required=None, widget=forms.TextInput(attrs={'class':'form-control'}))

    imagen = forms.ImageField(label="Imagen", required=None)

    class Meta: #Sirve para configurar la clase

        model=User

        fields=["username", "email", "password1", "password2", "first_name", "last_name"]

        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio



class UserEditForm(UserCreationForm):

    email=forms.CharField(label="Email usuario", widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    first_name=ToUpperField(label="Nombre", max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name=ToUpperField(label="Apellido", max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:

        model= User

        fields=["email", "password1", "password2", "first_name", "last_name"]

        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio

class FormularioInscripcion(forms.Form):

    nombre = ToUpperField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")



    
