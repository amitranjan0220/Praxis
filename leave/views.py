from django.shortcuts import render,redirect
from . models import Leave
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all(request):
    user = request.user
    if user.id <= 2:
        leave = Leave.objects.all()
        context = {'list':leave}
        return render(request, 'school/leave/school_leave_all.html',context)
    else:
        return redirect("school_home")


@login_required
def single(request,pk):
    leave = Leave.objects.get(pk=pk)
    context = {'list':leave}
    return render(request,'school/leave/school_leave_single.html',context)


@login_required
def leave_delete(request ,pk):
    leave =Leave.objects.get(pk=pk)
    leave.delete()
    return redirect("leave_all")
