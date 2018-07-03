from django.db import models
from django.contrib.auth.models import User
from classroom.models import ClassRoom
from profiles.models import Profile
# Create your models here.

MONTHS = (
    ('first','First Payment'),
    ('Second','Second Payment'),
    ('Third','Third Payment'),
)

class Payment(models.Model):
    user = models.ForeignKey(User)
    classroom = models.ForeignKey(ClassRoom)
    amount= models.BigIntegerField()
    month = models.CharField(max_length=30, choices=MONTHS)
    deposit_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-deposit_at']


class StudentSelect(models.Model):
    classroom = models.ForeignKey(ClassRoom)
    student = models.ForeignKey(Profile)
