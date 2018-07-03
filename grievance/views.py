from django.shortcuts import render,redirect
from . forms import GrievanceForm
from . models import Grievance
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def school_grievance(request):
    user = request.user
    if user.id <= 2:
        grievance = Grievance.objects.all()
        context = {'list':grievance}
        return render(request,'school/grievance/school_grievance.html',context)
    else:
        return redirect("school_home")


@login_required
def grievance_delete(request ,pk):
    user = request.user
    if user.id <= 2:
        grievance =Grievance.objects.get(pk=pk)
        grievance.delete()
    else:
        return redirect("school_home")
    return redirect("school_grievance")
