from django import forms
from . models import Event
from django.forms.extras.widgets import SelectDateWidget

class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=SelectDateWidget(), label="Start Date")

    class Meta:
        model = Event
        fields = '__all__'
