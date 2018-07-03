from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile
from django.forms import ModelForm
from leave.models import Leave
from django.forms import ModelForm, Textarea

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','classroom','unique_id']


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
        widgets = {
            'to': Textarea(attrs={'cols': 40, 'rows': 5}),
            'sender': Textarea(attrs={'cols': 40, 'rows': 5}),
        }
