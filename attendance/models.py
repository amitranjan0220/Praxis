from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from classroom.models import ClassRoom
# Create your models here.

class Attendance(models.Model):
    classroom = models.ForeignKey(ClassRoom,blank=True)
    student = models.ForeignKey(Profile,blank=True)
    atten = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.user.first_name

    # class Meta:
    #     ordering = ['-created_at','classroom']
