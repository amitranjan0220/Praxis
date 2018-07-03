from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import Group


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid() and form.cleaned_data.get('code')=="code":
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.classroom = form.cleaned_data.get('classroom')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.father_name = form.cleaned_data.get('father_name')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.photo = form.cleaned_data.get('photo')
            user.profile.roll_no = form.cleaned_data.get('roll_no')
            user.save()
            my_group = Group.objects.get(name='student')
            my_group.user_set.add(user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('student_home')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})
