from django.db import models
from django.contrib.auth.models import User
from classroom.models import ClassRoom
from subject.models import Subject
# Create your models here.

class HomeWork(models.Model):
    class_class = models.ForeignKey(ClassRoom,on_delete=models.CASCADE,verbose_name="Classroom")
    class_subject = models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name="Subject")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.class_subject.subject

    class Meta:
        ordering = ['-created_at']
