from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,blank=True ,default=False)
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10)
    father_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=15)
    classroom = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='profile/%Y/%m/%d/', default = 'profile/myAvatar.png')
    unique_id = models.IntegerField(default=0)


    def __str__(self):
        return '{}{} {}'.format(self.user.first_name,self.user.last_name,self.roll_no)

    class Meta:
        ordering = ["classroom"]

    def save(self):
        im = Image.open(self.photo)
        output = BytesIO()
        im = im.resize( (200,200) )
        im.save(output, format="JPEG", quality=100)
        output.seek(0)
        self.photo = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Profile,self).save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    try:
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    except:
        pass
