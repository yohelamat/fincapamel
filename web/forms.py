from django import forms
from .models import ArticuloBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = ArticuloBlog
        fields = ['titulo', 'imagen', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Escribe un título llamativo...',
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Escribe la noticia aquí...',
                'rows': 5,
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'
            }),
        }