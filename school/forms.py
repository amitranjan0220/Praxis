from django import forms
from django.contrib.auth.models import User
from profiles.models import Profile
from django.forms import ModelForm


class PasswordResetForm(forms.Form):
        password = forms.CharField(label="New Password",widget=forms.PasswordInput)
        re_password = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','classroom','unique_id']


class NoticeForm(forms.Form):
    msg = forms.CharField(label="Message",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), required=True)
