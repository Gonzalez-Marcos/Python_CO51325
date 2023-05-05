from django import forms

from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

#Funcion para almacenar primer letra en mayúscula
class ToUpperField(forms.CharField):
    def to_python(self, value):
        return value.title()


class SalasFormulario(forms.Form):

    nivel = ToUpperField(min_length=3, max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    nombre = ToUpperField(min_length=3, max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'name': 'nombre'}))


class DocenteFormulario(forms.Form):

    nombre = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    apellido = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))

    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


class AlumnoFormulario(forms.Form):

    nombre = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    apellido = ToUpperField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))

    dni = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


class RegistroUsuarioForm(UserCreationForm):
    
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    first_name = ToUpperField(max_length=20, label='Nombre', required= None, widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name = ToUpperField(max_length=20, label='Apellido', required=None, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta: #Sirve para configurar la clase

        model=User

        fields=["username", "email", "password1", "password2", "first_name", "last_name"]

        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio


class SuperUsuarioForm(UserCreationForm):

    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    first_name = ToUpperField(max_length=20, label='Nombre', required= None, widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name = ToUpperField(max_length=20, label='Apellido', required=None, widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # Agregar un campo booleano para indicar si el usuario es un superusuario
    is_superuser = forms.BooleanField(required=False, label="Usuario ADMIN")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2", "is_superuser")


class UserEditForm(UserCreationForm):

    email=forms.CharField(label="Email usuario", widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control', 'disabled': 'true'}))

    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'form-control', 'disabled': 'true'}))

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


class CambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:

        fields=['old_password', 'new_password1', 'new_password2']

        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio
    
