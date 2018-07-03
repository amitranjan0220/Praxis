from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student_home/', views.student_home, name='student_home'),
    url(r'^student_contactus/', views.student_contactus, name='student_contactus'),
    url(r'^student_aboutus/', views.student_aboutus, name='student_aboutus'),
    url(r'^student_profile/', views.student_profile, name='student_profile'),
    url(r'^profile_edit/',views.profile_edit,name='student_profile_edit'),
    url(r'^attendance/', views.attendance, name='student_attendance'),
    url(r'^inbox/', views.student_inbox, name='student_inbox'),
    url(r'^student_notice/', views.notice,name='student_notice'),
    url(r'^student_homework/', views.homework,name='student_homework'),
    url(r'^event/', views.event,name='student_event'),
    url(r'^timetable/', views.timetable,name='student_timetable'),
    url(r'^leave/', views.leave,name='student_leave'),
    url(r'^exam/', views.exam, name='student_exam'),
    url(r'^exam_timetable/(?P<pk>\d+)/$', views.exam_timetable, name='student_exam_timetable'),
    url(r'^exam_list/', views.student_exam_list, name='student_exam_list'),
    url(r'^result/(?P<pk>\d+)/$', views.student_result, name='student_result'),
    url(r'^gallery/', views.gallery, name='student_gallery'),
    url(r'^student_grievance/', views.grievance, name='student_grievance'),
]
