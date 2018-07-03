from django.shortcuts import get_object_or_404
from django.utils.functional import curry
from django.shortcuts import render, redirect
from .models import Attendance
from profiles.models import Profile
from django.contrib.auth.models import User, Group
from classroom.models import ClassRoom
from django.contrib import messages
from . forms import AttendanceForm, AttendanceMonthForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
# Create your views here.

@login_required
def attendance_home(request):
    user = request.user
    group = Group.objects.get(name='teacher').user_set.all()
    if user in group:
        return render(request,'school/attendance/school_attendance.html')
    else:
        return redirect("school_home")


@login_required
def take_attendance(request):
    user = request.user
    group = Group.objects.get(name='teacher').user_set.all()
    if user in group:
        return render(request,'school/attendance/take_attendance.html')
    else:
        return redirect("school_home")



@login_required
def download_option(request):
    return render(request,'school/attendance/download_option.html')

@login_required
def attendance_report(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        classroom = request.POST['classroom']
        date_day = request.POST['date_day']
        date_month = request.POST['date_month']
        date_year = request.POST['date_year']
        option = request.POST['option']
        class_room = ClassRoom.objects.get(classname=classroom)
        if option == 'view':
            try:
                attendance = Attendance.objects.filter(classroom=class_room, created_at__day=date_day,
                                            created_at__month=date_month,created_at__year=date_year)
                return render(request,'school/attendance/attendance_search.html',{'list':attendance,
                                                                                  'class':classroom})
            except:
               pass
        elif option == 'download':
            try:
                a = Attendance.objects.filter(classroom=class_room, created_at__day=date_day,
                                            created_at__month=date_month,created_at__year=date_year)
                latest = a.latest('created_at')
                date = latest.created_at.strftime("%d-%m-%Y")
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="{}-{}.csv"'.format(latest.classroom,date)

                writer = csv.writer(response)
                writer.writerow(['Date', 'Roll Number', 'Name', 'status'])
                for a in a:
                    date = a.created_at.strftime("%d-%m-%Y")
                    roll = a.student.roll_no
                    attendance = a.atten
                    writer.writerow([date,roll, a, attendance])
                return response
            except:
                pass
    return render(request,'school/attendance/attendance_report.html',{'form':form})


@login_required
def attendance_report_month(request):
    if request.method == 'POST':
        form = AttendanceMonthForm(request.POST)
        if form.is_valid():
            classroom = request.POST['classroom']
            month = request.POST['month']
            option = request.POST['option']
            class_room = ClassRoom.objects.get(classname=classroom)
            if option == 'view':
                try:
                    attendance = Attendance.objects.filter(classroom=class_room,
                                                           created_at__month=month)
                    return render(request,'school/attendance/attendance_search_month.html',{'list':attendance,
                                                                                      'class':classroom})
                except:
                   pass
            elif option == 'download':
                try:
                    a = Attendance.objects.filter(classroom=class_room,
                                                           created_at__month=month)
                    latest = a.latest('created_at')
                    date = latest.created_at.strftime("%d-%m-%Y")
                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(latest.classroom)

                    writer = csv.writer(response)
                    writer.writerow(['Date', 'Roll Number', 'Name', 'status'])
                    for a in a:
                        date = a.created_at.strftime("%d-%m-%Y")
                        roll = a.student.roll_no
                        attendance = a.atten
                        writer.writerow([date,roll, a, attendance])
                    return response
                except:
                    pass

    else:
        form = AttendanceMonthForm()
    return render(request,'school/attendance/attendance_report_month.html',{'form':form})



@login_required
def class_VI(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VI' or user.id == 1:
        student = Profile.objects.filter(classroom='VI')
        stu = Profile.objects.filter(classroom='VI')
        try:
            for student in student:
                if request.method == 'POST':
                    form = request.POST[student.user.username]
                    classroom = ClassRoom.objects.get(classname=student.classroom)
                    att = Attendance.objects.create(student=student ,atten=form,classroom=classroom )
            if request.method == 'POST':
                messages.success(request, 'Attendance Taken Successfully')
        except:
                messages.success(request, 'please fill absent or present for every student')

        context = {'stu':stu}
        return render(request,'school/attendance/class_VI.html',context)
    else:
        return redirect("school_home")


@login_required
def class_VII(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VII' or user.id == 1:
        student = Profile.objects.filter(classroom='VII')
        stu = Profile.objects.filter(classroom='VII')
        try:
            for student in student:
                if request.method == 'POST':
                    form = request.POST[student.user.username]
                    classroom = ClassRoom.objects.get(classname=student.classroom)
                    att = Attendance.objects.create(student=student ,atten=form,classroom=classroom )
            if request.method == 'POST':
                messages.success(request, 'Attendance Taken Successfully')
        except:
                messages.success(request, 'please fill absent or present for every student')

        context = {'stu':stu}
        return render(request,'school/attendance/class_VII.html',context)
    else:
        return redirect("school_home")


@login_required
def class_VIII_A(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VIIIA' or user.id == 1:
        student = Profile.objects.filter(classroom='VIII_A')
        stu = Profile.objects.filter(classroom='VIII_A')
        try:
            for student in student:
                if request.method == 'POST':
                    form = request.POST[student.user.username]
                    classroom = ClassRoom.objects.get(classname=student.classroom)
                    att = Attendance.objects.create(student=student ,atten=form,classroom=classroom )
            if request.method == 'POST':
                messages.success(request, 'Attendance Taken Successfully')
        except:
                messages.success(request, 'please fill absent or present for every student')

        context = {'stu':stu}
        return render(request,'school/attendance/class_VIII_A.html',context)
    else:
        return redirect("school_home")


@login_required
def class_VIII_B(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VIIIB' or user.id == 1:
        student = Profile.objects.filter(classroom='VIII_B')
        stu = Profile.objects.filter(classroom='VIII_B')
        try:
            for student in student:
                if request.method == 'POST':
                    form = request.POST[student.user.username]
                    classroom = ClassRoom.objects.get(classname=student.classroom)
                    att = Attendance.objects.create(student=student ,atten=form,classroom=classroom )
            if request.method == 'POST':
                messages.success(request, 'Attendance Taken Successfully')
        except:
                messages.success(request, 'please fill absent or present for every student')

        context = {'stu':stu}
        return render(request,'school/attendance/class_VIII_B.html',context)
    else:
        return redirect("school_home")
