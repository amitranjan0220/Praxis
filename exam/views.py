from django.shortcuts import render,redirect
from . models import Exam
from . models import ExamTimeTable
from . forms import ExamForm, ExamTimeTableForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request,'school/exam/school_exam_home.html')

@login_required
def create(request):
    user = request.user
    if user.id <2:
        if request.method == "POST":
            form = ExamForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Exam created successfully')
    else:
        return redirect("school_exam_home")
    form = ExamForm()
    return render(request,'school/exam/school_exam_create.html',{'form':form})


@login_required
def exam_timetable(request):
    user = request.user
    if user.id <2:
        if request.method == "POST":
            form = ExamTimeTableForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Timetable created successfully')
    else:
        return redirect("school_exam_home")
    form = ExamTimeTableForm()
    return render(request,'school/exam/school_exam_timetable.html',{'form':form})


@login_required
def all(request):
    exam = Exam.objects.all()
    context ={'exam':exam}
    return render(request,'school/exam/school_exam_all.html',context)


@login_required
def timetable(request,pk):
    try:
        exam = Exam.objects.get(pk=pk)
        timetable = ExamTimeTable.objects.get(exam=exam)
        context = {'list':timetable}
        return render(request,'school/exam/school_single_exam_timetable.html',context)
    except:
        messages.success(request, 'Timetable is not created')
        return redirect("school_exam_home")

@login_required
def exam_delete(request,pk):
    user = request.user
    if user.id <=2:
        exam = Exam.objects.get(pk=pk)
        exam.delete()
    else:
        return redirect("school_exam_home")
    return redirect("school_exam_home")
