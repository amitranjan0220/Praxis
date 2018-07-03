from django import forms


MONTHS = (
    ('1','January'),
    ('2','February'),
    ('3','March'),
    ('4','April'),
    ('5','May'),
    ('6','June'),
    ('7','July'),
    ('8','August'),
    ('9','September'),
    ('10','October'),
    ('11','November'),
    ('12','December'),
    )

CLASSCHOICES =(
    ('VI','VI'),
    ('VII','VII'),
    ('VIII_A','VIII_A'),
    ('VIII_B','VIII_B'),
)

OPTIONS = (
    ('view','View'),
    ('download','Download')

)

class AttendanceForm(forms.Form):
    classroom = forms.ChoiceField(widget=forms.Select, choices=CLASSCHOICES, required=True)
    date = forms.DateField(widget = forms.SelectDateWidget())
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)


class AttendanceMonthForm(forms.Form):
    classroom = forms.ChoiceField(widget=forms.Select, choices=CLASSCHOICES, required=True)
    month = forms.ChoiceField(widget=forms.Select,choices=MONTHS)
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
