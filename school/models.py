from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    email = models.EmailField()
    phone1 = models.BigIntegerField()
    phone2 = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " School"



class StudentMessage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']

class MessageCount(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)
