from django.db import models
from classroom.models import ClassRoom

# Create your models here.
class Exam(models.Model):
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField(default='2018-03-01')
    end_date = models.DateField(default='2018-03-01')

    def __str__(self):
        return self.name

class ExamTimeTable(models.Model):
    exam = models.OneToOneField(Exam,on_delete=models.CASCADE)
    day_one = models.TextField(blank=True,default="e.g-20/02/2018 - Monday - Hindi-10:00 am to 11:00 am,English-1:00 pm to 2:00 pm")
    day_two = models.TextField(blank=True)
    day_three = models.TextField(blank=True)
    day_four = models.TextField(blank=True)
    day_five = models.TextField(blank=True)
    day_six = models.TextField(blank=True)
    day_seven = models.TextField(blank=True)

    def __str__(self):
        return self.exam.name
