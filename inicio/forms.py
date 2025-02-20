from django import forms



class CrearBebida(forms.Form):
    tipo = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)
    descripcion = forms.CharField(required=False, widget=forms.Textarea)
    

    