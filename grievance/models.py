from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Grievance(models.Model):
    message = models.TextField(max_length=200)
    sender = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20,default=False)

    def __str__(self):
        return self.sender

    class Meta:
        ordering = ['-created_at']

class GrievanceCount(models.Model):
    user = models.ForeignKey(User)
    count = models.IntegerField(default=0)
