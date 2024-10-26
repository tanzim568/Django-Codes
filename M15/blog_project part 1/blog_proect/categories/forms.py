from django import forms
from .models import Catergory

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Catergory
        fields='__all__'