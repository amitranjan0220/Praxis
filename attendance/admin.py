from django.contrib import admin
from .models import Attendance
# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['created_at','classroom','student']

admin.site.register(Attendance,AttendanceAdmin)
