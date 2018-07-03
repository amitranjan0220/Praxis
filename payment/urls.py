from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.payment_home, name='school_payment_home'),
    url(r'^deposit_fees/', views.deposit_fees, name='school_deposit_fees'),
    url(r'^ajax/load_student/', views.load_student, name='ajax_load_student'),
    url(r'^payment_form/(?P<pk>\d+)/$', views.payment_form, name='payment_form'),
    url(r'^manage_fees/', views.manage_fees, name='school_manage_fees'),
    url(r'^student_search/', views.student_search, name='school_student_search'),
    url(r'^search_by_month/', views.search_by_month, name='school_search_by_month'),

]
