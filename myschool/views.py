from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')

def school_base(request):
    return render(request,'school_base.html')

def student_base(request):
    return render(request,'student_base.html')

def offline(request):
    return render(request,'offline.html')
