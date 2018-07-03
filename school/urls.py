from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^school_home/',views.school_home,name="school_home"),
    url(r'^school_aboutus/',views.school_aboutus,name="school_aboutus"),
    url(r'^school_contactus/',views.school_contactus,name="school_contactus"),
    url(r'^school_profile/',views.school_profile,name="school_profile"),
    url(r'^profile_edit/',views.profile_edit,name='school_profile_edit'),
    url(r'^school_class_list/$', views.school_class_list, name='school_class_list'),
    url(r'list_download/(?P<pk>\d+)/$', views.student_list_download, name="list_download"),
    url(r'^student_per_class/(?P<pk>\d+)/$', views.student_per_class, name='student_per_class'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^msg/(?P<pk>\d+)/$', views.msg, name='msg'),
    url(r'^school_gallery/', views.school_gallery, name='school_gallery'),
    url(r'^search/$', views.search, name='search'),
    url(r'^block/(?P<pk>\d+)/$', views.student_block, name='student_block'),
    url(r'^unblock/(?P<pk>\d+)/$', views.student_unblock, name='student_unblock'),
    url(r'^student/(?P<pk>\d+)/$', views.student, name="school_student"),
    url(r'^reset_password/(?P<pk>\d+)/$', views.reset_password, name="reset_password"),
    url(r'^reset_inbox/', views.reset_inbox, name='reset_inbox'),
    url(r'^reset_leave/', views.reset_leave, name='reset_leave'),
    url(r'^reset_grievance/', views.reset_grievance, name='reset_grievance'),
]
