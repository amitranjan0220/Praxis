from django.db import models
from profiles.models import Profile
from classroom.models import ClassRoom
from exam.models import Exam
# Create your models here.

class VIResult(models.Model):
    student = models.ForeignKey(Profile)
    classroom = models.ForeignKey(ClassRoom)
    exam = models.ForeignKey(Exam)
    sub_one = models.CharField(max_length=20, default='HINDI')
    sub_one_mark = models.IntegerField(null=True)
    sub_one_tmark= models.IntegerField(null=True)
    sub_one_viva = models.IntegerField(null=True,blank=True, default=0)
    sub_one_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_one_home = models.IntegerField(null=True,blank=True,default=0)
    sub_one_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_two = models.CharField(max_length=20,default='ENGLISH')
    sub_two_mark = models.IntegerField(null=True)
    sub_two_tmark= models.IntegerField(null=True)
    sub_two_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_home = models.IntegerField(null=True,blank=True,default=0)
    sub_two_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_three = models.CharField(max_length=20,default='MATH')
    sub_three_mark = models.IntegerField(null=True)
    sub_three_tmark= models.IntegerField(null=True)
    sub_three_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_home = models.IntegerField(null=True,blank=True,default=0)
    sub_three_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_four = models.CharField(max_length=20,default='S.S.T')
    sub_four_mark = models.IntegerField(null=True)
    sub_four_tmark= models.IntegerField(null=True)
    sub_four_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_home = models.IntegerField(null=True,blank=True,default=0)
    sub_four_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_five = models.CharField(max_length=20,default='SCIENCE')
    sub_five_mark = models.IntegerField(null=True)
    sub_five_tmark= models.IntegerField(null=True)
    sub_five_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_home = models.IntegerField(null=True,blank=True,default=0)
    sub_five_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_six = models.CharField(max_length=20, default='COMPUTER')
    sub_six_mark = models.IntegerField(null=True)
    sub_six_tmark= models.IntegerField(null=True)
    sub_six_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_home = models.IntegerField(null=True,blank=True,default=0)
    sub_six_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_seven = models.CharField(max_length=20,default='ART')
    sub_seven_mark = models.IntegerField(null=True)
    sub_seven_tmark= models.IntegerField(null=True)
    sub_seven_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_home = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_thome = models.IntegerField(null=True,blank=True,default=0)
    obtain_marks = models.IntegerField(null=True)
    total_marks = models.IntegerField(null=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.exam.name

    def save(self, *args, **kwargs):
        self.obtain_marks =(self.sub_one_mark + self.sub_one_viva + self.sub_one_home
                + self.sub_two_mark + self.sub_two_viva + self.sub_two_home
                + self.sub_three_mark + self.sub_three_viva + self.sub_three_home
                + self.sub_four_mark + self.sub_four_viva + self.sub_four_home
                + self.sub_five_mark + self.sub_five_viva + self.sub_five_home
                + self.sub_six_mark + self.sub_six_viva + self.sub_six_home
                + self.sub_seven_mark + self.sub_seven_viva + self.sub_seven_home
                )
        self.total_marks = (
                self.sub_one_tmark + self.sub_one_tviva + self.sub_one_thome
              + self.sub_two_tmark + self.sub_two_tviva + self.sub_two_thome
              + self.sub_three_tmark + self.sub_three_tviva + self.sub_three_thome
              + self.sub_four_tmark + self.sub_four_tviva + self.sub_four_thome
              + self.sub_five_tmark + self.sub_five_tviva + self.sub_five_thome
              + self.sub_six_tmark + self.sub_six_tviva + self.sub_six_thome
              + self.sub_seven_tmark + self.sub_seven_tviva + self.sub_seven_thome
            )
        self.percent = float(self.obtain_marks)*(100/self.total_marks)
        super(VIResult,self).save(*args,**kwargs)

class VIIResult(models.Model):
    student = models.ForeignKey(Profile)
    classroom = models.ForeignKey(ClassRoom)
    exam = models.ForeignKey(Exam)
    sub_one = models.CharField(max_length=20, default='HINDI')
    sub_one_mark = models.IntegerField(null=True)
    sub_one_tmark= models.IntegerField(null=True)
    sub_one_viva = models.IntegerField(null=True,blank=True, default=0)
    sub_one_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_one_home = models.IntegerField(null=True,blank=True,default=0)
    sub_one_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_two = models.CharField(max_length=20,default='ENGLISH')
    sub_two_mark = models.IntegerField(null=True)
    sub_two_tmark= models.IntegerField(null=True)
    sub_two_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_home = models.IntegerField(null=True,blank=True,default=0)
    sub_two_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_three = models.CharField(max_length=20,default='MATH')
    sub_three_mark = models.IntegerField(null=True)
    sub_three_tmark= models.IntegerField(null=True)
    sub_three_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_home = models.IntegerField(null=True,blank=True,default=0)
    sub_three_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_four = models.CharField(max_length=20,default='S.S.T')
    sub_four_mark = models.IntegerField(null=True)
    sub_four_tmark= models.IntegerField(null=True)
    sub_four_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_home = models.IntegerField(null=True,blank=True,default=0)
    sub_four_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_five = models.CharField(max_length=20,default='SCIENCE')
    sub_five_mark = models.IntegerField(null=True)
    sub_five_tmark= models.IntegerField(null=True)
    sub_five_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_home = models.IntegerField(null=True,blank=True,default=0)
    sub_five_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_six = models.CharField(max_length=20, default='COMPUTER')
    sub_six_mark = models.IntegerField(null=True)
    sub_six_tmark= models.IntegerField(null=True)
    sub_six_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_home = models.IntegerField(null=True,blank=True,default=0)
    sub_six_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_seven = models.CharField(max_length=20,default='ART')
    sub_seven_mark = models.IntegerField(null=True)
    sub_seven_tmark= models.IntegerField(null=True)
    sub_seven_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_home = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_thome = models.IntegerField(null=True,blank=True,default=0)
    obtain_marks = models.IntegerField(null=True)
    total_marks = models.IntegerField(null=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.exam.name

    def save(self, *args, **kwargs):
        self.obtain_marks = (
              self.sub_one_mark + self.sub_one_viva + self.sub_one_home
            + self.sub_two_mark + self.sub_two_viva + self.sub_two_home
            + self.sub_three_mark + self.sub_three_viva + self.sub_three_home
            + self.sub_four_mark + self.sub_four_viva + self.sub_four_home
            + self.sub_five_mark + self.sub_five_viva + self.sub_five_home
            + self.sub_six_mark + self.sub_six_viva + self.sub_six_home
            + self.sub_seven_mark + self.sub_seven_viva + self.sub_seven_home
        )
        self.total_marks = (
                self.sub_one_tmark + self.sub_one_tviva + self.sub_one_thome
              + self.sub_two_tmark + self.sub_two_tviva + self.sub_two_thome
              + self.sub_three_tmark + self.sub_three_tviva + self.sub_three_thome
              + self.sub_four_tmark + self.sub_four_tviva + self.sub_four_thome
              + self.sub_five_tmark + self.sub_five_tviva + self.sub_five_thome
              + self.sub_six_tmark + self.sub_six_tviva + self.sub_six_thome
              + self.sub_seven_tmark + self.sub_seven_tviva + self.sub_seven_thome
            )
        self.percent = float(self.obtain_marks)*(100/self.total_marks)
        super(VIIResult,self).save(*args,**kwargs)


class VIIIAResult(models.Model):
    student = models.ForeignKey(Profile)
    classroom = models.ForeignKey(ClassRoom)
    exam = models.ForeignKey(Exam)
    sub_one = models.CharField(max_length=20, default='HINDI')
    sub_one_mark = models.IntegerField(null=True)
    sub_one_tmark= models.IntegerField(null=True)
    sub_one_viva = models.IntegerField(null=True,blank=True, default=0)
    sub_one_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_one_home = models.IntegerField(null=True,blank=True,default=0)
    sub_one_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_two = models.CharField(max_length=20,default='ENGLISH')
    sub_two_mark = models.IntegerField(null=True)
    sub_two_tmark= models.IntegerField(null=True)
    sub_two_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_home = models.IntegerField(null=True,blank=True,default=0)
    sub_two_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_three = models.CharField(max_length=20,default='MATH')
    sub_three_mark = models.IntegerField(null=True)
    sub_three_tmark= models.IntegerField(null=True)
    sub_three_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_home = models.IntegerField(null=True,blank=True,default=0)
    sub_three_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_four = models.CharField(max_length=20,default='S.S.T')
    sub_four_mark = models.IntegerField(null=True)
    sub_four_tmark= models.IntegerField(null=True)
    sub_four_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_home = models.IntegerField(null=True,blank=True,default=0)
    sub_four_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_five = models.CharField(max_length=20,default='SCIENCE')
    sub_five_mark = models.IntegerField(null=True)
    sub_five_tmark= models.IntegerField(null=True)
    sub_five_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_home = models.IntegerField(null=True,blank=True,default=0)
    sub_five_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_six = models.CharField(max_length=20, default='COMPUTER')
    sub_six_mark = models.IntegerField(null=True)
    sub_six_tmark= models.IntegerField(null=True)
    sub_six_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_home = models.IntegerField(null=True,blank=True,default=0)
    sub_six_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_seven = models.CharField(max_length=20,default='ART')
    sub_seven_mark = models.IntegerField(null=True)
    sub_seven_tmark= models.IntegerField(null=True)
    sub_seven_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_home = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_thome = models.IntegerField(null=True,blank=True,default=0)
    obtain_marks = models.IntegerField(null=True)
    total_marks = models.IntegerField(null=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.exam.name

    def save(self, *args, **kwargs):
        self.obtain_marks = (
              self.sub_one_mark + self.sub_one_viva + self.sub_one_home
            + self.sub_two_mark + self.sub_two_viva + self.sub_two_home
            + self.sub_three_mark + self.sub_three_viva + self.sub_three_home
            + self.sub_four_mark + self.sub_four_viva + self.sub_four_home
            + self.sub_five_mark + self.sub_five_viva + self.sub_five_home
            + self.sub_six_mark + self.sub_six_viva + self.sub_six_home
            + self.sub_seven_mark + self.sub_seven_viva + self.sub_seven_home
        )
        self.total_marks = (
                self.sub_one_tmark + self.sub_one_tviva + self.sub_one_thome
              + self.sub_two_tmark + self.sub_two_tviva + self.sub_two_thome
              + self.sub_three_tmark + self.sub_three_tviva + self.sub_three_thome
              + self.sub_four_tmark + self.sub_four_tviva + self.sub_four_thome
              + self.sub_five_tmark + self.sub_five_tviva + self.sub_five_thome
              + self.sub_six_tmark + self.sub_six_tviva + self.sub_six_thome
              + self.sub_seven_tmark + self.sub_seven_tviva + self.sub_seven_thome
            )
        self.percent = float(self.obtain_marks)*(100/self.total_marks)
        super(VIIIAResult,self).save(*args,**kwargs)


class VIIIBResult(models.Model):
    student = models.ForeignKey(Profile)
    classroom = models.ForeignKey(ClassRoom)
    exam = models.ForeignKey(Exam)
    sub_one = models.CharField(max_length=20, default='HINDI')
    sub_one_mark = models.IntegerField(null=True)
    sub_one_tmark= models.IntegerField(null=True)
    sub_one_viva = models.IntegerField(null=True,blank=True, default=0)
    sub_one_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_one_home = models.IntegerField(null=True,blank=True,default=0)
    sub_one_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_two = models.CharField(max_length=20,default='ENGLISH')
    sub_two_mark = models.IntegerField(null=True)
    sub_two_tmark= models.IntegerField(null=True)
    sub_two_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_two_home = models.IntegerField(null=True,blank=True,default=0)
    sub_two_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_three = models.CharField(max_length=20,default='MATH')
    sub_three_mark = models.IntegerField(null=True)
    sub_three_tmark= models.IntegerField(null=True)
    sub_three_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_three_home = models.IntegerField(null=True,blank=True,default=0)
    sub_three_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_four = models.CharField(max_length=20,default='S.S.T')
    sub_four_mark = models.IntegerField(null=True)
    sub_four_tmark= models.IntegerField(null=True)
    sub_four_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_four_home = models.IntegerField(null=True,blank=True,default=0)
    sub_four_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_five = models.CharField(max_length=20,default='SCIENCE')
    sub_five_mark = models.IntegerField(null=True)
    sub_five_tmark= models.IntegerField(null=True)
    sub_five_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_five_home = models.IntegerField(null=True,blank=True,default=0)
    sub_five_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_six = models.CharField(max_length=20, default='COMPUTER')
    sub_six_mark = models.IntegerField(null=True)
    sub_six_tmark= models.IntegerField(null=True)
    sub_six_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_six_home = models.IntegerField(null=True,blank=True,default=0)
    sub_six_thome = models.IntegerField(null=True,blank=True,default=0)
    sub_seven = models.CharField(max_length=20,default='ART')
    sub_seven_mark = models.IntegerField(null=True)
    sub_seven_tmark= models.IntegerField(null=True)
    sub_seven_viva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_tviva = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_home = models.IntegerField(null=True,blank=True,default=0)
    sub_seven_thome = models.IntegerField(null=True,blank=True,default=0)
    obtain_marks = models.IntegerField(null=True)
    total_marks = models.IntegerField(null=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.exam.name

    def save(self, *args, **kwargs):
        self.obtain_marks = (
              self.sub_one_mark + self.sub_one_viva + self.sub_one_home
            + self.sub_two_mark + self.sub_two_viva + self.sub_two_home
            + self.sub_three_mark + self.sub_three_viva + self.sub_three_home
            + self.sub_four_mark + self.sub_four_viva + self.sub_four_home
            + self.sub_five_mark + self.sub_five_viva + self.sub_five_home
            + self.sub_six_mark + self.sub_six_viva + self.sub_six_home
            + self.sub_seven_mark + self.sub_seven_viva + self.sub_seven_home
        )
        self.total_marks = (
                self.sub_one_tmark + self.sub_one_tviva + self.sub_one_thome
              + self.sub_two_tmark + self.sub_two_tviva + self.sub_two_thome
              + self.sub_three_tmark + self.sub_three_tviva + self.sub_three_thome
              + self.sub_four_tmark + self.sub_four_tviva + self.sub_four_thome
              + self.sub_five_tmark + self.sub_five_tviva + self.sub_five_thome
              + self.sub_six_tmark + self.sub_six_tviva + self.sub_six_thome
              + self.sub_seven_tmark + self.sub_seven_tviva + self.sub_seven_thome
            )
        self.percent = float(self.obtain_marks)*(100/self.total_marks)
        super(VIIIBResult,self).save(*args,**kwargs)
