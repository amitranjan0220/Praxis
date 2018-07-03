from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/',views.school_result_home,name="school_result_home"),
    url(r'^class_VI/', views.VI_home, name='class_VI'),
    url(r'^VI_result_search/', views.VI_result_search, name='VI_result_search'),
    url(r'^VI_edit/(?P<pk>\d+)/$', views.VI_result_edit, name='VI_result_edit'),
    url(r'^class_VII/', views.VII_home, name='class_VII'),
    url(r'^VII_result_search/', views.VII_result_search, name='VII_result_search'),
    url(r'^VII_edit/(?P<pk>\d+)/$', views.VII_result_edit, name='VII_result_edit'),
    url(r'^class_VIII_A/', views.VIII_A_home, name='class_VIII_A'),
    url(r'^VIII_A_result_search/', views.VIII_A_result_search, name='VIII_A_result_search'),
    url(r'^VIII_A_edit/(?P<pk>\d+)/$', views.VIII_A_result_edit, name='VIII_A_result_edit'),
    url(r'^class_VIII_B/', views.VIII_B_home, name='class_VIII_B'),
    url(r'^VIII_B_result_search/', views.VIII_B_result_search, name='VIII_B_result_search'),
    url(r'^VIII_B_edit/(?P<pk>\d+)/$', views.VIII_B_result_edit, name='VIII_B_result_edit'),
]
