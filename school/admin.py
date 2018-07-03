from django.contrib import admin
from . models import School,StudentMessage, MessageCount
# Register your models here.

admin.site.register(School)
admin.site.register(StudentMessage)
admin.site.register(MessageCount)
