from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^event_home/', views.home, name='school_event_home'),
    url(r'^event_all/', views.all, name='school_event_all'),
    url(r'^event_create/', views.create, name='school_event_create'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='school_event_delete'),
]
