from django.db import models

# Create your models here.
class Event(models.Model):
    start_date = models.DateField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.message
