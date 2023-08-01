from django import forms
from .models import Materiales, Grupo, Marca, Proveedor, Unidad

class MaterialesForm(forms.ModelForm):

    #https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
    
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Descripcion', 'style': 'width: 300px;', 'class': 'form-control'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Precio', 'style': 'width: 200px;', 'class': 'form-control'}))
    grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 150px;', 'class': 'form-control'}))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 150px;', 'class': 'form-control'}))
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    unidad = forms.ModelChoiceField(queryset=Unidad.objects.all(), widget=forms.Select(attrs={ 'style': 'width: 150px;', 'class': 'form-control'}))



    class Meta:   
        model = Materiales
        fields = '__all__'





# https://stackoverflow.com/questions/48041375/django-select-a-valid-choice-that-choice-is-not-one-of-the-available-choices