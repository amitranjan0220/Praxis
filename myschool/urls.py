"""myschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^my_admin_django/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^account/', include('account.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^classroom/', include('classroom.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^student/', include('student.urls')),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^notice/', include('notice.urls')),
    url(r'^homework/', include('homework.urls')),
    url(r'^subject/', include('subject.urls')),
    url(r'^timetable/', include('timetable.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^leave/', include('leave.urls')),
    url(r'^exam/', include('exam.urls')),
    url(r'^result/', include('result.urls')),
    url(r'^push/', include('push.urls')),
    url(r'^webpush/', include('webpush.urls')),
    url(r'^grievance/', include('grievance.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^sw.js', (TemplateView.as_view(template_name="sw.js", content_type='application/javascript', )), name='sw.js'),
    url(r'^school_base/', views.school_base,name='school_base'),
    url(r'^student_base/', views.student_base,name='student_base'),
    url(r'^offline/', views.offline,name='offline'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
