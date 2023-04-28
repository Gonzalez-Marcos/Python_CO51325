from django import forms

from django.contrib.auth.models import User

from .models import Comentario, PostBlog

#Funcion para almacenar primer letra en mayúscula
class ToUpperField(forms.CharField):
    def to_python(self, value):
        return value.title()
    
class FormularioComentario(forms.ModelForm):

    nombre = ToUpperField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'class':'form-control'}))

    texto = forms.CharField(max_length=20, label='Comentario', widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:

        model = Comentario

        fields = ["nombre", "texto"]

class FormularioPost(forms.ModelForm):

    imagen = forms.ImageField(label='Imagen')

    text = forms.CharField(max_length=200, label='Comentario', widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = PostBlog
        fields = ['imagen', 'text']
