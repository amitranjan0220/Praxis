from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^homework_home/', views.home, name='school_homework_home'),
    url(r'^homework_all/', views.all, name='school_homework_all'),
    url(r'^Homework_create/', views.create, name='school_homework_create'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='school_homework_delete'),

]
