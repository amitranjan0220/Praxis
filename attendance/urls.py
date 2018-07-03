from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^attendance_home/', views.attendance_home, name='attendance_home'),
    url(r'^take_attendance/', views.take_attendance, name='take_attendance'),
    url(r'^attendance_report/', views.attendance_report, name='attendance_report'),
    url(r'^attendance_report_month/', views.attendance_report_month, name='attendance_report_month'),
    url(r'^download_option/', views.download_option, name='download_option'),
    url(r'^VI/', views.class_VI, name='VI'),
    url(r'^VII/', views.class_VII, name='VII'),
    url(r'^VIII_A/', views.class_VIII_A, name='VIII_A'),
    url(r'^VIII_B/', views.class_VIII_B, name='VIII_B'),
]
