from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from . models import HomeWork

@receiver(post_save, sender=None)
def homework_alert(sender,instance,created,**kwargs):
    print('hello')
