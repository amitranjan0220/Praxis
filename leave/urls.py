from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/', views.all, name="school_leave_all"),
    url(r'^single/(?P<pk>\d+)/$',views.single, name="school_leave_single"),
    url(r'^delete/(?P<pk>\d+)/$', views.leave_delete, name='school_leave_delete'),

]
