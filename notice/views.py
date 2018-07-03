from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Notice
from . forms import NoticeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,'school/notice/school_notice_home.html')


@login_required
def all(request):
    notice = Notice.objects.all()[0:10]
    context = {'list':notice}
    return render(request,'school/notice/school_notice_all.html',context)


@login_required
def create(request):
    user = request.user
    if user.id <=2:
        if request.method == 'POST':
            form = NoticeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Notice created Successfully')
            else:
                return redirect("school_notice_home")
    else:
        return redirect("school_notice_home")
    form = NoticeForm()
    return render(request,'school/notice/school_notice_create.html',{'form':form})


@login_required
def delete(request ,pk):
    user = request.user
    if user.id <= 2:
        notice =Notice.objects.get(pk=pk)
        notice.delete()
    else:
        return redirect("school_notice_home")
    return redirect("school_notice_all")
