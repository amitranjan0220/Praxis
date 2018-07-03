from django.shortcuts import render,redirect
from . models import HomeWork
from . forms import HomeWorkForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request,'school/homework/school_homework_home.html')


@login_required
def all(request):
    homework = HomeWork.objects.all()[0:100]
    context = {'list':homework}
    return render(request,'school/homework/school_homework_all.html',context)


@login_required
def create(request):
    if request.method == 'POST':
        form = HomeWorkForm(request.POST)
        form.save()
        messages.success(request, 'Homework created successfully')
    else:
        form = HomeWorkForm()
    return render(request,'school/homework/school_homework_create.html',{'form':form})


@login_required
def delete(request ,pk):
    user = request.user
    if user.id <= 2:
        homework =HomeWork.objects.get(pk=pk)
        homework.delete()
    else:
        return redirect("school_homework_home")
    return redirect("school_homework_all")
