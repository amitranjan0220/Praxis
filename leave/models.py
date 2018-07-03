from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Leave(models.Model):
    to = models.TextField(max_length=25)
    subject = models.CharField(max_length=20)
    letter = models.TextField(max_length=200)
    sender = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-created_at']

class LeaveCount(models.Model):
    user = models.ForeignKey(User)
    count = models.IntegerField(default=0)
