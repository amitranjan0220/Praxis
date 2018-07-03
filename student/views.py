from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm, LeaveForm
from django.contrib import messages
from profiles.models import Profile
from school.models import StudentMessage
from notice.models import Notice
from homework.models import HomeWork
from classroom.models import ClassRoom
from timetable.models import TimeTable
from event.models import Event
from exam.models import Exam, ExamTimeTable
from result.models import (VIResult,VIIResult,VIIIAResult,VIIIBResult)
from grievance.forms import GrievanceForm
from grievance.models import Grievance,GrievanceCount
from leave.models import LeaveCount
from django.contrib.auth.models import User

# Create your views here.

@login_required
def student_home(request):
    return render(request,'student/student/student_home.html')

@login_required
def student_aboutus(request):
    user1 = User.objects.get(pk=1)
    user = User.objects.all()[1:6]
    context = {'user':user,
               'user1':user1}
    return render(request,'student/student/student_aboutus.html',context)

@login_required
def student_contactus(request):
    return render(request,'student/student/student_contactus.html')

@login_required
def student_profile(request):
    staff = request.user
    context = {'list':staff}
    return render(request,'student/student/student_profile.html',context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile details updated successfully')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'student/student/profile_edit.html',{'user_form': user_form,'profile_form': profile_form})


@login_required
def attendance(request):
    user = request.user
    student=user.profile.attendance_set.all()[0:31]
    context = {'list':student}
    return render(request,'student/attendance/student_attendance.html',context)

@login_required
def student_inbox(request):
    user = request.user
    inbox = StudentMessage.objects.filter(user=user)
    context = {'list':inbox}
    return render(request,'student/inbox/student_inbox.html',context)


@login_required
def notice(request):
    notice = Notice.objects.all()[0:10]
    context = {'list':notice}
    return render(request,'student/notice/student_notice.html',context)



@login_required
def homework(request):
    user = request.user
    classroom = user.profile.classroom
    room = ClassRoom.objects.get(classname=classroom)
    homework = HomeWork.objects.filter(class_class=room)[0:30]
    context = {'list':homework}
    return render(request,'student/homework/student_homework.html',context)


@login_required
def timetable(request):
    user = request.user
    classroom = user.profile.classroom
    room = ClassRoom.objects.get(classname=classroom)
    timetable = TimeTable.objects.filter(classroom=room)
    context = {'list':timetable}
    return render(request,'student/timetable/student_timetable.html',context)

@login_required
def event(request):
    event = Event.objects.all()
    context = {'list':event}
    return render(request,'student/event/student_event.html',context)


@login_required
def leave(request):
    form = LeaveForm()
    if request.method == 'POST':
        leave = LeaveForm(request.POST)
        leave.save()
        user = User.objects.get(username='admin')
        count = LeaveCount(user=user)
        count.save()
        messages.success(request, 'successfully sent!')
    return render(request,'student/leave/student_leave.html',{'form':form})




@login_required
def exam(request):
    user =request.user
    cl = user.profile.classroom
    classroom = ClassRoom.objects.get(classname=cl)
    exam = Exam.objects.filter(classroom = classroom)
    context={'list':exam}
    return render(request,'student/exam/student_exam.html',context)



@login_required
def exam_timetable(request,pk):
    exam = Exam.objects.get(pk=pk)
    timetable= ExamTimeTable.objects.get(exam=exam)
    context={'list':timetable}

    return render(request, 'student/exam/student_exam_timetable.html',context)



@login_required
def student_exam_list(request):
    user =request.user
    cl = user.profile.classroom
    classroom = ClassRoom.objects.get(classname=cl)
    exam = Exam.objects.filter(classroom = classroom)
    context={'list':exam}
    return render(request,'student/result/student_exam_list.html',context)



@login_required
def student_result(request,pk):
    user = request.user
    profile = user.profile
    classroom =profile.classroom
    exam = Exam.objects.get(pk=pk)
    if classroom == 'VI':
        result = VIResult.objects.filter(student=profile,exam=exam)
        context = {'list':result}
        return render(request,'student/result/student_result_home.html',context)
    elif classroom == 'VII':
        result = VIIResult.objects.filter(student=profile,exam=exam)
        context = {'list':result}
        return render(request,'student/result/student_result_home.html',context)
    elif classroom == 'VIII_A':
        result = VIIIAResult.objects.filter(student=profile,exam=exam)
        context = {'list':result}
        return render(request,'student/result/student_result_home.html',context)
    elif classroom == 'VIII_B':
        result = VIIIBResult.objects.filter(student=profile,exam=exam)
        context = {'list':result}
        return render(request,'student/result/student_result_home.html',context)
    else:
        pass


@login_required
def gallery(request):
    return render(request,'student/gallery/student_gallery.html')


@login_required
def grievance(request):
    form = GrievanceForm()
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            sender = request.POST['sender']
            message = request.POST['message']
            user = request.user
            name = user.first_name + " " + user.last_name
            comp = Grievance.objects.create(sender=sender,message=message,username=name)
            messages.success(request, 'Sent Successfully')
            useradmin = User.objects.get(username = 'admin')
            count = GrievanceCount(user=useradmin)
            count.save()
    return render(request,'student/grievance/student_grievance.html',{'form':form})
