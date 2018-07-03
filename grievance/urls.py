from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.school_grievance,name='school_grievance'),
    url(r'^delete/(?P<pk>\d+)/$', views.grievance_delete, name='school_grievance_delete'),

]
