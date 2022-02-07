from django import forms
from product.models import productmodel

class productform(forms.ModelForm):
    class Meta:
        model=productmodel
        fields='__all__'
        
    