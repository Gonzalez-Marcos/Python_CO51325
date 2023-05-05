from django import forms

from django.contrib.auth.models import User

from .models import Comentario, PostBlog

#Funcion para almacenar primer letra en mayúscula
class ToUpperField(forms.CharField):
    def to_python(self, value):
        return value.title()
    
# app_blog/forms.py

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'texto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentario'}),
        }


class FormularioPost(forms.ModelForm):

    imagen = forms.ImageField(label='Imagen')

    titulo = forms.CharField(max_length=200, label='Título', widget=forms.TextInput(attrs={'class':'form-control'}))

    texto = forms.CharField(label='Comentario', widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = PostBlog
        fields = ['imagen', 'titulo', 'texto']
