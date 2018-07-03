from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/',views.push_home,name='push_home'),
]
