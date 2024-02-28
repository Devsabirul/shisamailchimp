from django import forms
from .models import *


class AddEmailForm(forms.ModelForm):

    class Meta:
        model = EmailAdd
        exclude =('author',)
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            "category": forms.TextInput(attrs={'class': 'form-control mb-3'})
        }
    
