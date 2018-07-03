from django import forms
from django.forms import ModelForm
from .models import (VIResult,VIIResult,VIIIAResult,VIIIBResult)
from classroom.models import ClassRoom
from exam.models import Exam
from profiles.models import Profile
from django.utils.translation import ugettext_lazy as _


classVI = ClassRoom.objects.filter(classname='VI')
VIexam = Exam.objects.filter(classroom=classVI)
stu_VI = Profile.objects.filter(classroom='VI')

classVII = ClassRoom.objects.filter(classname='VII')
VIIexam = Exam.objects.filter(classroom=classVII)
stu_VII = Profile.objects.filter(classroom='VII')

classVIII_A = ClassRoom.objects.filter(classname='VIII_A')
VIII_A_exam = Exam.objects.filter(classroom=classVIII_A)
stu_VIII_A = Profile.objects.filter(classroom='VIII_A')

classVIII_B = ClassRoom.objects.filter(classname='VIII_B')
VIII_B_exam = Exam.objects.filter(classroom=classVIII_B)
stu_VIII_B = Profile.objects.filter(classroom='VIII_B')

OPTIONS = (
    ('view','View'),
    ('download','Download')

)


class VIResultForm(ModelForm):
    classroom = forms.ModelChoiceField(queryset =classVI)
    exam = forms.ModelChoiceField(queryset =VIexam)
    student = forms.ModelChoiceField(queryset =stu_VI)


    class Meta:
        model = VIResult
        fields = '__all__'
        exclude = ['total_marks','obtain_marks','percent']
        labels = {
            'sub_one': _('Subject-1'),
            'sub_one_mark': _('Obtain Marks'),
            'sub_one_tmark': _('Total Marks'),
            'sub_one_viva': _('Viva'),
            'sub_one_tviva': _('Viva M.M'),
            'sub_one_home': _('Homework'),
            'sub_one_thome': _('Homework M.M'),
            'sub_two': _('Subject-2'),
            'sub_two_mark': _('Obtain Marks'),
            'sub_two_tmark': _('Total Marks'),
            'sub_two_viva': _('Viva'),
            'sub_two_tviva': _('Viva M.M'),
            'sub_two_home': _('Homework'),
            'sub_two_thome': _('Homework M.M'),
            'sub_three': _('Subject-3'),
            'sub_three_mark': _('Obtain Marks'),
            'sub_three_tmark': _('Total Marks'),
            'sub_three_viva': _('Viva'),
            'sub_three_tviva': _('Viva M.M'),
            'sub_three_home': _('Homework'),
            'sub_three_thome': _('Homework M.M'),
            'sub_four': _('Subject-4'),
            'sub_four_mark': _('Obtain Marks'),
            'sub_four_tmark': _('Total Marks'),
            'sub_four_viva': _('Viva'),
            'sub_four_tviva': _('Viva M.M'),
            'sub_four_home': _('Homework'),
            'sub_four_thome': _('Homework M.M'),
            'sub_five': _('Subject-5'),
            'sub_five_mark': _('Obtain Marks'),
            'sub_five_tmark': _('Total Marks'),
            'sub_five_viva': _('Viva'),
            'sub_five_tviva': _('Viva M.M'),
            'sub_five_home': _('Homework'),
            'sub_five_thome': _('Homework M.M'),
            'sub_six': _('Subject-6'),
            'sub_six_mark': _('Obtain Marks'),
            'sub_six_tmark': _('Total Marks'),
            'sub_six_viva': _('Viva'),
            'sub_six_tviva': _('Viva M.M'),
            'sub_six_home': _('Homework'),
            'sub_six_thome': _('Homework M.M'),
            'sub_seven': _('Subject-7'),
            'sub_seven_mark': _('Obtain Marks'),
            'sub_seven_tmark': _('Total Marks'),
            'sub_seven_viva': _('Viva'),
            'sub_seven_tviva': _('Viva M.M'),
            'sub_seven_home': _('Homework'),
            'sub_seven_thome': _('Homework M.M'),
        }


class VIResultSearchForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset =classVI)
    exam = forms.ModelChoiceField(queryset =VIexam)
    student = forms.ModelChoiceField(queryset =stu_VI)
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)


class VIIResultForm(ModelForm):
    classroom = forms.ModelChoiceField(queryset =classVII)
    exam = forms.ModelChoiceField(queryset =VIIexam)
    student = forms.ModelChoiceField(queryset =stu_VII)

    class Meta:
        model = VIIResult
        fields = '__all__'
        exclude = ['total_marks','obtain_marks','percent']
        labels = {
            'sub_one': _('Subject-1'),
            'sub_one_mark': _('Obtain Marks'),
            'sub_one_tmark': _('Total Marks'),
            'sub_one_viva': _('Viva'),
            'sub_one_tviva': _('Viva M.M'),
            'sub_one_home': _('Homework'),
            'sub_one_thome': _('Homework M.M'),
            'sub_two': _('Subject-2'),
            'sub_two_mark': _('Obtain Marks'),
            'sub_two_tmark': _('Total Marks'),
            'sub_two_viva': _('Viva'),
            'sub_two_tviva': _('Viva M.M'),
            'sub_two_home': _('Homework'),
            'sub_two_thome': _('Homework M.M'),
            'sub_three': _('Subject-3'),
            'sub_three_mark': _('Obtain Marks'),
            'sub_three_tmark': _('Total Marks'),
            'sub_three_viva': _('Viva'),
            'sub_three_tviva': _('Viva M.M'),
            'sub_three_home': _('Homework'),
            'sub_three_thome': _('Homework M.M'),
            'sub_four': _('Subject-4'),
            'sub_four_mark': _('Obtain Marks'),
            'sub_four_tmark': _('Total Marks'),
            'sub_four_viva': _('Viva'),
            'sub_four_tviva': _('Viva M.M'),
            'sub_four_home': _('Homework'),
            'sub_four_thome': _('Homework M.M'),
            'sub_five': _('Subject-5'),
            'sub_five_mark': _('Obtain Marks'),
            'sub_five_tmark': _('Total Marks'),
            'sub_five_viva': _('Viva'),
            'sub_five_tviva': _('Viva M.M'),
            'sub_five_home': _('Homework'),
            'sub_five_thome': _('Homework M.M'),
            'sub_six': _('Subject-6'),
            'sub_six_mark': _('Obtain Marks'),
            'sub_six_tmark': _('Total Marks'),
            'sub_six_viva': _('Viva'),
            'sub_six_tviva': _('Viva M.M'),
            'sub_six_home': _('Homework'),
            'sub_six_thome': _('Homework M.M'),
            'sub_seven': _('Subject-7'),
            'sub_seven_mark': _('Obtain Marks'),
            'sub_seven_tmark': _('Total Marks'),
            'sub_seven_viva': _('Viva'),
            'sub_seven_tviva': _('Viva M.M'),
            'sub_seven_home': _('Homework'),
            'sub_seven_thome': _('Homework M.M'),
        }


class VIIResultSearchForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset =classVII)
    exam = forms.ModelChoiceField(queryset =VIIexam)
    student = forms.ModelChoiceField(queryset =stu_VII)
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)


class VIIIAResultForm(ModelForm):
    classroom = forms.ModelChoiceField(queryset =classVIII_A)
    exam = forms.ModelChoiceField(queryset =VIII_A_exam)
    student = forms.ModelChoiceField(queryset =stu_VIII_A)

    class Meta:
        model = VIIIAResult
        fields = '__all__'
        exclude = ['total_marks','obtain_marks','percent']
        labels = {
            'sub_one': _('Subject-1'),
            'sub_one_mark': _('Obtain Marks'),
            'sub_one_tmark': _('Total Marks'),
            'sub_one_viva': _('Viva'),
            'sub_one_tviva': _('Viva M.M'),
            'sub_one_home': _('Homework'),
            'sub_one_thome': _('Homework M.M'),
            'sub_two': _('Subject-2'),
            'sub_two_mark': _('Obtain Marks'),
            'sub_two_tmark': _('Total Marks'),
            'sub_two_viva': _('Viva'),
            'sub_two_tviva': _('Viva M.M'),
            'sub_two_home': _('Homework'),
            'sub_two_thome': _('Homework M.M'),
            'sub_three': _('Subject-3'),
            'sub_three_mark': _('Obtain Marks'),
            'sub_three_tmark': _('Total Marks'),
            'sub_three_viva': _('Viva'),
            'sub_three_tviva': _('Viva M.M'),
            'sub_three_home': _('Homework'),
            'sub_three_thome': _('Homework M.M'),
            'sub_four': _('Subject-4'),
            'sub_four_mark': _('Obtain Marks'),
            'sub_four_tmark': _('Total Marks'),
            'sub_four_viva': _('Viva'),
            'sub_four_tviva': _('Viva M.M'),
            'sub_four_home': _('Homework'),
            'sub_four_thome': _('Homework M.M'),
            'sub_five': _('Subject-5'),
            'sub_five_mark': _('Obtain Marks'),
            'sub_five_tmark': _('Total Marks'),
            'sub_five_viva': _('Viva'),
            'sub_five_tviva': _('Viva M.M'),
            'sub_five_home': _('Homework'),
            'sub_five_thome': _('Homework M.M'),
            'sub_six': _('Subject-6'),
            'sub_six_mark': _('Obtain Marks'),
            'sub_six_tmark': _('Total Marks'),
            'sub_six_viva': _('Viva'),
            'sub_six_tviva': _('Viva M.M'),
            'sub_six_home': _('Homework'),
            'sub_six_thome': _('Homework M.M'),
            'sub_seven': _('Subject-7'),
            'sub_seven_mark': _('Obtain Marks'),
            'sub_seven_tmark': _('Total Marks'),
            'sub_seven_viva': _('Viva'),
            'sub_seven_tviva': _('Viva M.M'),
            'sub_seven_home': _('Homework'),
            'sub_seven_thome': _('Homework M.M'),
        }


class VIIIAResultSearchForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset =classVIII_A)
    exam = forms.ModelChoiceField(queryset =VIII_A_exam)
    student = forms.ModelChoiceField(queryset =stu_VIII_A)
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)


class VIIIBResultForm(ModelForm):
    classroom = forms.ModelChoiceField(queryset =classVIII_B)
    exam = forms.ModelChoiceField(queryset =VIII_B_exam)
    student = forms.ModelChoiceField(queryset =stu_VIII_B)

    class Meta:
        model = VIIIBResult
        fields = '__all__'
        exclude = ['total_marks','obtain_marks','percent']
        labels = {
            'sub_one': _('Subject-1'),
            'sub_one_mark': _('Obtain Marks'),
            'sub_one_tmark': _('Total Marks'),
            'sub_one_viva': _('Viva'),
            'sub_one_tviva': _('Viva M.M'),
            'sub_one_home': _('Homework'),
            'sub_one_thome': _('Homework M.M'),
            'sub_two': _('Subject-2'),
            'sub_two_mark': _('Obtain Marks'),
            'sub_two_tmark': _('Total Marks'),
            'sub_two_viva': _('Viva'),
            'sub_two_tviva': _('Viva M.M'),
            'sub_two_home': _('Homework'),
            'sub_two_thome': _('Homework M.M'),
            'sub_three': _('Subject-3'),
            'sub_three_mark': _('Obtain Marks'),
            'sub_three_tmark': _('Total Marks'),
            'sub_three_viva': _('Viva'),
            'sub_three_tviva': _('Viva M.M'),
            'sub_three_home': _('Homework'),
            'sub_three_thome': _('Homework M.M'),
            'sub_four': _('Subject-4'),
            'sub_four_mark': _('Obtain Marks'),
            'sub_four_tmark': _('Total Marks'),
            'sub_four_viva': _('Viva'),
            'sub_four_tviva': _('Viva M.M'),
            'sub_four_home': _('Homework'),
            'sub_four_thome': _('Homework M.M'),
            'sub_five': _('Subject-5'),
            'sub_five_mark': _('Obtain Marks'),
            'sub_five_tmark': _('Total Marks'),
            'sub_five_viva': _('Viva'),
            'sub_five_tviva': _('Viva M.M'),
            'sub_five_home': _('Homework'),
            'sub_five_thome': _('Homework M.M'),
            'sub_six': _('Subject-6'),
            'sub_six_mark': _('Obtain Marks'),
            'sub_six_tmark': _('Total Marks'),
            'sub_six_viva': _('Viva'),
            'sub_six_tviva': _('Viva M.M'),
            'sub_six_home': _('Homework'),
            'sub_six_thome': _('Homework M.M'),
            'sub_seven': _('Subject-7'),
            'sub_seven_mark': _('Obtain Marks'),
            'sub_seven_tmark': _('Total Marks'),
            'sub_seven_viva': _('Viva'),
            'sub_seven_tviva': _('Viva M.M'),
            'sub_seven_home': _('Homework'),
            'sub_seven_thome': _('Homework M.M'),
        }


class VIIIBResultSearchForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset =classVIII_B)
    exam = forms.ModelChoiceField(queryset =VIII_B_exam)
    student = forms.ModelChoiceField(queryset =stu_VIII_B)
    option = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
