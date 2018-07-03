from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=20)
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
