from django.db import models
from django.contrib.auth.models import User
from classroom.models import ClassRoom
# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=40)

    def __str__(self):
        return self.subject
