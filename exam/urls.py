from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^exam_home/', views.home, name='school_exam_home'),
    url(r'^create/',views.create, name='school_exam_create'),
    url(r'^exam_timetable/',views.exam_timetable, name='school_exam_timetable'),
    url(r'^all/',views.all, name='school_exam_all'),
    url(r'^exam&timetable/(?P<pk>\d+)/$', views.timetable, name='exam_single_timetable'),
    url(r'^delete/(?P<pk>\d+)/$',views.exam_delete, name='exam_delete'),
]
