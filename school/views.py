from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from .forms import UserEditForm, ProfileEditForm, NoticeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import messages
from classroom.models import ClassRoom
from .models import StudentMessage, MessageCount
from .filters import UserFilter
from leave.models import LeaveCount
from grievance.models import GrievanceCount
import csv
# Create your views here.


@login_required
def school_home(request):
    return render(request,'school/school/school_home.html',)


@login_required
def school_aboutus(request):
    user1 = User.objects.get(pk=1)
    user = User.objects.all()[1:6]
    context = {'user':user,
               'user1':user1}
    return render(request,'school/school/school_aboutus.html',context)


@login_required
def school_contactus(request):
    return render(request,'school/school/school_contactus.html')

@login_required
def school_profile(request):
    staff = request.user
    context = {'list':staff}
    return render(request,'school/school/school_profile.html',context)

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
    return render(request,'school/school/profile_edit.html',{'user_form': user_form,'profile_form': profile_form})


@login_required
def school_class_list(request):
    user = request.user
    if user.id <= 2:
        classroom = ClassRoom.objects.all()
        context = {
        'list':classroom,
        }
        return render(request,'school/school/school_class_list.html',context)
    else:
        return redirect("school_home")

@login_required
def student_per_class(request,pk):
    classroom = ClassRoom.objects.get(pk=pk)
    classname = classroom.classname
    student = Profile.objects.filter(classroom=classname)
    context = {
    'list':student,
    'class':classname,
    }
    return render(request,'school/school/student_per_class.html',context)

@login_required
def student_list_download(request,pk):
    classroom = ClassRoom.objects.get(pk=pk)
    classname = classroom.classname
    student = Profile.objects.filter(classroom=classname)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(classname)
    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Roll Number','Class','Birth Date','Gender','Phone','Address'])
    for student in student:
        writer.writerow([student.user.first_name ,student.user.last_name,student.roll_no,
            student.classroom,student.birth_date,student.gender,student.phone,student.address])
    return response

@login_required
def edit(request,pk):
    student = Profile.objects.get(pk=pk)
    user = student.user
    if request.method == 'POST':
        user_form = UserEditForm(instance=user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile details updated successfully')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=user.profile)
    return render(request,'school/school/profile_edit.html',{'user_form': user_form,'profile_form': profile_form})


@login_required
def msg(request,pk):
    student = Profile.objects.get(pk=pk)
    user = student.user
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['msg']
            msg = StudentMessage(user=user,msg=message)
            msg.save()
            messages.success(request, 'Message sent successfully')
            obj = MessageCount(user=user)
            obj.save()
        else:
            pass
    else:
        form = NoticeForm()
    return render(request,'school/school/student_msg.html',{'form':form})


def reset_inbox(request):
    try:
        obj = MessageCount.objects.all()
        obj.delete()
    except:
        pass
    return HttpResponse("OK")


@login_required
def school_gallery(request):
    return render(request,'school/school/school_gallery.html')


@login_required
def search(request):
    user = request.user
    if user.id <3:
        user_list = User.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, 'school/school/user_list.html', {'filter': user_filter})
    else:
        return redirect('school_home')


@login_required
def student_block(request,pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect ("search")

@login_required
def student_unblock(request,pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect ("search")


@login_required
def student(request,pk):
    student = User.objects.get(pk=pk)
    context = {'list':student}
    return render(request,"school/school/school_profile.html",context)


@login_required
def reset_password(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data.get('password')
            pass2 = form.cleaned_data.get('re_password')
            if pass1 == pass2:
                try:
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    messages.success(request, 'Password changed successfully')
                except:
                    messages.success(request, 'Please type valid Password')
            else:
                messages.success(request, 'Password do not matched')
    else:
        form = PasswordResetForm()
    return render(request,'school/school/reset_password.html',{'form':form})


def reset_leave(request):
    try:
        obj = LeaveCount.objects.all()
        obj.delete()
    except:
        pass
    return HttpResponse("OK")

def reset_grievance(request):
    try:
        obj = GrievanceCount.objects.all()
        obj.delete()
    except:
        pass
    return HttpResponse("OK")
