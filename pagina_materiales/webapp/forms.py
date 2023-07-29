from django import forms
from .models import Materiales

class MaterialesForm(forms.ModelForm):
    class Meta:
    
        model = Materiales
        fields = "__all__"