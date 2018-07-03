from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        group_teacher = Group.objects.get(name='teacher').user_set.all()
        group_student = Group.objects.get(name='student').user_set.all()
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None and  user in group_teacher:
                if user.is_active:
                    login(request, user)
                    return redirect('school_home')
            elif user is not None and  user in group_student:
                if user.is_active:
                    login(request, user)
                    return redirect('student_home')
            else:
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
