from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput

CHOICES = (('Male', 'Male'),('Female', 'Female'))

CLASSCHOICES =(
    ('VI','VI'),
    ('VII','VII'),
    ('VIII_A','VIII_A'),
    ('VIII_B','VIII_B'),
)

class SignUpForm(UserCreationForm):
    code = forms.CharField(max_length=20,label="School Code",
                    error_messages = {'required' : "Please enter correct school code",
                                           'invalid'  : "Wrong code. Please correct."},
                                           required=True)
    gender = forms.ChoiceField(label ="Gender",widget=forms.RadioSelect, choices=CHOICES, required=True)
    father_name = forms.CharField(label="Father Name")
    birth_date = forms.DateField(label ="Date of Birth",widget = forms.SelectDateWidget(years=range(1980,2017)))
    classroom = forms.ChoiceField(label="Class",widget=forms.Select, choices=CLASSCHOICES, required=True)
    address = forms.CharField( label="Address",widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), required=True)
    phone = forms.CharField(label = "Mobile No.", required=True)
    roll_no = forms.CharField(label = "Roll No.")
    photo = forms.ImageField(help_text="Upload passport size photo", required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        for fieldname in ['password1']:
            self.fields[fieldname].help_text = "Minimum 8 (character and number both) "


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'email': TextInput(attrs={'cols': 80, 'rows': 0}),
        }
