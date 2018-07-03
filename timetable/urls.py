from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^timetable_home/', views.home, name='school_timetable_home'),
    url(r'^timetable_all/', views.all, name='school_timetable_all'),
    url(r'^timetable_create/', views.create, name='school_timetable_create'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name="school_timetable_delete"),
]
