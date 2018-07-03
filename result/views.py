from django.shortcuts import render, redirect
from classroom.models import ClassRoom
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from . forms import (VIResultForm,VIResultSearchForm,VIIResultForm,VIIResultSearchForm,VIIIAResultForm,
VIIIAResultSearchForm, VIIIBResultForm, VIIIBResultSearchForm)
from .models import (VIResult,VIIResult,VIIIAResult, VIIIBResult)
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
# Create your views here.

@login_required
def school_result_home(request):
    user = request.user
    group = Group.objects.get(name='teacher').user_set.all()
    if user in group:
        return render(request,'school/result/school_result_home.html')
    else:
        return redirect("school_home")


@login_required
def VI_home(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VI' or user.id == 1:
        if request.method == "POST":
            form = VIResultForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                result = VIResult.objects.filter(student=student,exam=exam,classroom=classroom)
                if result.count() == 0:
                    form.save()
                    messages.success(request, 'Result created successfully')
                else:
                    messages.success(request, 'Result already created')
            else:
                pass
    else:
        return redirect('school_result_home')
    form = VIResultForm()
    return render(request,'school/result/VI_home.html',{'form':form})



@login_required
def VI_result_search(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VI' or user.id == 1:
        if request.method == 'POST':
            form = VIResultSearchForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                option = form.cleaned_data.get('option')
                if option == 'view':
                    try:
                        result = VIResult.objects.get(exam=exam,student=student,classroom=classroom)
                        context = {'list':result}
                        return render(request,'school/result/VI_result.html',context)
                    except:
                        messages.success(request, 'Result Not Created!')
                elif option == 'download':
                    try:
                        result = VIResult.objects.get(exam=exam,student=student,classroom=classroom)
                        html = render_to_string('school/result/pdf.html', {'list': result})
                        response = HttpResponse(content_type='application/pdf')
                        response['Content-Disposition'] = 'filename="result.pdf"'
                        weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
                        return response
                    except:
                        messages.success(request, 'Result Not Created!')
            else:
                pass
    else:
        return redirect('school_result_home')
    form = VIResultSearchForm()
    return render(request,'school/result/VI_result_search.html',{'form':form})



@login_required
def VI_result_edit(request,pk):
    result = VIResult.objects.get(pk=pk)
    form = VIResultForm(instance = result)
    if request.method == 'POST':
        form = VIResultForm(request.POST, instance = result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result updated successfully')
        else:
            return redirect("school_result_home")

    return render(request,'school/result/VI_result_edit.html',{'form':form})


@login_required
def VII_home(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VII' or user.id == 1:
        if request.method == "POST":
            form = VIIResultForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                result = VIIResult.objects.filter(student=student,exam=exam,classroom=classroom)
                if result.count() == 0:
                    form.save()
                    messages.success(request, 'Result created successfully')
                else:
                    messages.success(request, 'Result already created')
            else:
                pass
    else:
        return redirect('school_result_home')
    form = VIIResultForm()
    return render(request,'school/result/VII_home.html',{'form':form})



@login_required
def VII_result_search(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VII' or user.id == 1:
        if request.method == 'POST':
            form = VIIResultSearchForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                option = form.cleaned_data.get('option')
                if option == 'view':
                    try:
                        result = VIIResult.objects.get(exam=exam,student=student,classroom=classroom)
                        context = {'list':result}
                        return render(request,'school/result/VII_result.html',context)
                    except:
                        messages.success(request, 'Result Not Created!')
                elif option == 'download':
                    try:
                        result = VIIResult.objects.get(exam=exam,student=student,classroom=classroom)
                        html = render_to_string('school/result/pdf.html', {'list': result})
                        response = HttpResponse(content_type='application/pdf')
                        response['Content-Disposition'] = 'filename="result.pdf"'
                        weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
                        return response
                    except:
                        messages.success(request, 'Result Not Created!')

                else:
                    pass
    else:
        return redirect('school_result_home')
    form = VIIResultSearchForm()
    return render(request,'school/result/VII_result_search.html',{'form':form})


@login_required
def VII_result_edit(request,pk):
    result = VIIResult.objects.get(pk=pk)
    form = VIIResultForm(instance = result)
    if request.method == 'POST':
        form = VIIResultForm(request.POST, instance = result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result updated successfully')
        else:
            return redirect("school_result_home")

    return render(request,'school/result/VII_result_edit.html',{'form':form})



@login_required
def VIII_A_home(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VIIIA' or user.id == 1:
        if request.method == "POST":
            form = VIIIAResultForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                result = VIIIAResult.objects.filter(student=student,exam=exam,classroom=classroom)
                if result.count() == 0:
                    form.save()
                    messages.success(request, 'Result created successfully')
                else:
                    messages.success(request, 'Result already created')
            else:
                pass
    else:
        return redirect('school_result_home')
    form = VIIIAResultForm()
    return render(request,'school/result/VIII_A_home.html',{'form':form})



@login_required
def VIII_A_result_search(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VIIIA' or user.id == 1:
        if request.method == 'POST':
            form = VIIIAResultSearchForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                option = form.cleaned_data.get('option')
                if option == 'view':
                    try:
                        result = VIIIAResult.objects.get(exam=exam,student=student,classroom=classroom)
                        context = {'list':result}
                        return render(request,'school/result/VIII_A_result.html',context)
                    except:
                        messages.success(request, 'Result Not Created!')
                elif option == 'download':
                    try:
                        result = VIIIAResult.objects.get(exam=exam,student=student,classroom=classroom)
                        html = render_to_string('school/result/pdf.html', {'list': result})
                        response = HttpResponse(content_type='application/pdf')
                        response['Content-Disposition'] = 'filename="result.pdf"'
                        weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
                        return response
                    except:
                        messages.success(request, 'Result Not Created!')
                else:
                    pass
    else:
        return redirect('school_result_home')
    form = VIIIAResultSearchForm()
    return render(request,'school/result/VIII_A_result_search.html',{'form':form})



@login_required
def VIII_A_result_edit(request,pk):
    result = VIIIAResult.objects.get(pk=pk)
    form = VIIIAResultForm(instance = result)
    if request.method == 'POST':
        form = VIIIAResultForm(request.POST, instance = result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result updated successfully')
        else:
            return redirect("school_result_home")

    return render(request,'school/result/VIII_A_result_edit.html',{'form':form})



@login_required
def VIII_B_home(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VIIIB' or user.id ==  1:
        if request.method == "POST":
            form = VIIIBResultForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                result = VIIIBResult.objects.filter(student=student,exam=exam,classroom=classroom)
                if result.count() == 0:
                    form.save()
                    messages.success(request, 'Result created successfully')
                else:
                    messages.success(request, 'Result already created')
            else:
                pass
    else:
        return redirect('school_result_home')
    form = VIIIBResultForm()
    return render(request,'school/result/VIII_B_home.html',{'form':form})



@login_required
def VIII_B_result_search(request):
    user = request.user
    teacher = user.profile.classroom
    if teacher == 'Teacher_VIIIB' or user.id == 1:
        if request.method == 'POST':
            form = VIIIBResultSearchForm(request.POST)
            if form.is_valid():
                classroom = form.cleaned_data.get('classroom')
                exam = form.cleaned_data.get('exam')
                student = form.cleaned_data.get('student')
                option = form.cleaned_data.get('option')
                if option == 'view':
                    try:
                        result = VIIIBResult.objects.get(exam=exam,student=student,classroom=classroom)
                        context = {'list':result}
                        return render(request,'school/result/VIII_B_result.html',context)
                    except:
                        messages.success(request, 'Result Not Created!')
                elif option == 'download':
                    try:
                        result = VIIIBResult.objects.get(exam=exam,student=student,classroom=classroom)
                        html = render_to_string('school/result/pdf.html', {'list': result})
                        response = HttpResponse(content_type='application/pdf')
                        response['Content-Disposition'] = 'filename="result.pdf"'
                        weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
                        return response
                    except:
                        messages.success(request, 'Result Not Created!')
                else:
                    pass
    else:
        return redirect('school_result_home')
    form = VIIIBResultSearchForm()
    return render(request,'school/result/VIII_B_result_search.html',{'form':form})



@login_required
def VIII_B_result_edit(request,pk):
    result = VIIIBResult.objects.get(pk=pk)
    form = VIIIBResultForm(instance = result)
    if request.method == 'POST':
        form = VIIIBResultForm(request.POST, instance = result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result updated successfully')
        else:
            return redirect("school_result_home")

    return render(request,'school/result/VIII_B_result_edit.html',{'form':form})
