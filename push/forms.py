from django import forms

class PushForm(forms.Form):
    msg = forms.CharField(label="Message",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), required=True)
