from django.contrib import admin
from . models import Exam,ExamTimeTable
# Register your models here.
class ExamAdmin(admin.ModelAdmin):
    list_display = ['classroom','name']

admin.site.register(Exam,ExamAdmin)
admin.site.register(ExamTimeTable)
