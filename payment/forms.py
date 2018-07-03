from django.forms import ModelForm, Select
from classroom.models import ClassRoom
from profiles.models import Profile
from .models import StudentSelect, Payment
from django import forms


OPTIONS = (
    ('view','View'),
    ('download','Download')

)

class SelectStudentForm(ModelForm):
    class Meta:
        model = StudentSelect
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Profile.objects.none()

        if 'classroom' in self.data:
            try:
                class_room = int(self.data.get('classroom'))
                room =ClassRoom.objects.get(pk=class_room)
                self.fields['student'].queryset = Profile.objects.filter(classroom=room.classname)
            except (ValueError, TypeError,):
                pass
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.classroom.student_set.order_by('classroom')

class SelectForm(ModelForm):
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
    class Meta:
        model = StudentSelect
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Profile.objects.none()

        if 'classroom' in self.data:
            try:
                class_room = int(self.data.get('classroom'))
                room =ClassRoom.objects.get(pk=class_room)
                self.fields['student'].queryset = Profile.objects.filter(classroom=room.classname)
            except (ValueError, TypeError,):
                pass
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.classroom.student_set.order_by('classroom')


class PaymentForm(ModelForm):

    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ['user','classroom']


CLASSCHOICES =(
    ('VI','VI'),
    ('VII','VII'),
    ('VIII_A','VIII_A'),
    ('VIII_B','VIII_B'),
)


MONTHS = (
    ('first','First Payment'),
    ('Second','Second Payment'),
    ('Third','Third Payment'),
)


class SearchByMonthForm(forms.Form):
    classroom = forms.ChoiceField(label="Class",widget=forms.Select, choices=CLASSCHOICES, required=True)
    month = forms.ChoiceField(label="Month",widget=forms.Select, choices=MONTHS, required=True)
