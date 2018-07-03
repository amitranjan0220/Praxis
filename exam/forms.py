from django.forms import ModelForm
from . models import Exam, ExamTimeTable

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamTimeTableForm(ModelForm):
    class Meta:
        model = ExamTimeTable
        fields = '__all__'
