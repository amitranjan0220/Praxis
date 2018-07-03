from django.contrib import admin
from . models import HomeWork
# Register your models here.
class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ['created_at','class_class','class_subject',]

admin.site.register(HomeWork,HomeWorkAdmin)
