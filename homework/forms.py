from django import forms
from . models import HomeWork

class HomeWorkForm(forms.ModelForm):

    class Meta:
        model = HomeWork
        fields = '__all__'
