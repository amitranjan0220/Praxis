from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^notice_home/', views.home, name='school_notice_home'),
    url(r'^notice_all/', views.all, name='school_notice_all'),
    url(r'^notice_create/', views.create, name='school_notice_create'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='school_notice_delete'),


]
