from django.shortcuts import render, redirect
from . forms import TimeTableForm
from . models import TimeTable
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'school/timetable/school_timetable_home.html')


@login_required
def all(request):
    timetable = TimeTable.objects.all()
    context = {'list':timetable}
    return render(request,'school/timetable/school_timetable_all.html',context)


@login_required
def create(request):
    user = request.user
    if user.id < 2:
        if request.method == "POST":
            form = TimeTableForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Timetable created successfully')
    else:
        return redirect("school_timetable_home")
    form = TimeTableForm()
    return render(request,'school/timetable/school_timetable_create.html',{'form':form})


@login_required
def delete(request ,pk):
    user =request.user
    if user.id <=2:
        timetable =TimeTable.objects.get(pk=pk)
        timetable.delete()
    else:
        return redirect("school_timetable_home")
    return redirect("school_timetable_all")
