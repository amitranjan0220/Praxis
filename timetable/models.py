from django.db import models
from classroom.models import ClassRoom
# Create your models here.

class TimeTable(models.Model):
    classroom = models.ForeignKey(ClassRoom)
    time_1 = models.CharField(max_length=20)
    time_2 = models.CharField(max_length=20)
    time_3 = models.CharField(max_length=20)
    time_4 = models.CharField(max_length=20)
    time_5 = models.CharField(max_length=20)
    time_6 = models.CharField(max_length=20)
    time_7 = models.CharField(max_length=20)
    time_8 = models.CharField(max_length=20)
    subject_1= models.CharField(max_length=20,default="None")
    subject_2= models.CharField(max_length=20,default="None")
    subject_3= models.CharField(max_length=20,default="None")
    subject_4= models.CharField(max_length=20,default="None")
    subject_5=models.CharField(max_length=20,default="None")
    subject_6= models.CharField(max_length=20,default="None")
    subject_7= models.CharField(max_length=20,default="None")
    subject_8= models.CharField(max_length=20,default="None")
    subject_9= models.CharField(max_length=20,default="None")
    subject_10= models.CharField(max_length=20,default="None")
    subject_11= models.CharField(max_length=20,default="None")
    subject_12= models.CharField(max_length=20,default="None")
    subject_13= models.CharField(max_length=20,default="None")
    subject_14= models.CharField(max_length=20,default="None")
    subject_15= models.CharField(max_length=20,default="None")
    subject_16= models.CharField(max_length=20,default="None")
    subject_17= models.CharField(max_length=20,default="None")
    subject_18= models.CharField(max_length=20,default="None")
    subject_19= models.CharField(max_length=20,default="None")
    subject_20= models.CharField(max_length=20,default="None")
    subject_21=models.CharField(max_length=20,default="None")
    subject_22= models.CharField(max_length=20,default="None")
    subject_23= models.CharField(max_length=20,default="None")
    subject_24= models.CharField(max_length=20,default="None")
    subject_25= models.CharField(max_length=20,default="None")
    subject_26= models.CharField(max_length=20,default="None")
    subject_27= models.CharField(max_length=20,default="None")
    subject_28= models.CharField(max_length=20,default="None")
    subject_29= models.CharField(max_length=20,default="None")
    subject_30= models.CharField(max_length=20,default="None")
    subject_31= models.CharField(max_length=20,default="None")
    subject_32= models.CharField(max_length=20,default="None")
    subject_33= models.CharField(max_length=20,default="None")
    subject_34= models.CharField(max_length=20,default="None")
    subject_35= models.CharField(max_length=20,default="None")
    subject_36= models.CharField(max_length=20,default="None")
    subject_37=models.CharField(max_length=20,default="None")
    subject_38= models.CharField(max_length=20,default="None")
    subject_39= models.CharField(max_length=20,default="None")
    subject_40= models.CharField(max_length=20,default="None")
    subject_41= models.CharField(max_length=20,default="None")
    subject_42= models.CharField(max_length=20,default="None")
    subject_43= models.CharField(max_length=20,default="None")
    subject_44= models.CharField(max_length=20,default="None")
    subject_45= models.CharField(max_length=20,default="None")
    subject_46= models.CharField(max_length=20,default="None")
    subject_47= models.CharField(max_length=20,default="None")
    subject_48= models.CharField(max_length=20,default="None")

    def __str__(self):
        return self.classroom.classname
