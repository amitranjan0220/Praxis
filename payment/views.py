from django.shortcuts import render, redirect
from classroom.models import ClassRoom
from .forms import SelectStudentForm,SelectForm, PaymentForm, SearchByMonthForm
from profiles.models import Profile
from .models import Payment
from django.contrib.auth.models import User
from django.contrib import messages
from school.models import StudentMessage, MessageCount
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.contrib.auth.decorators import login_required
from webpush import send_user_notification
# Create your views here.
@login_required
def payment_home(request):
    user = request.user
    if user.username == 'admin':
        return render(request,'school/payment/payment_home.html')
    else:
        return redirect("school_home")

@login_required
def load_student(request):
    class_room = request.GET.get('classroom')
    room =ClassRoom.objects.get(pk=class_room)
    student = Profile.objects.filter(classroom=room.classname)
    return render(request,'school/payment/student_list.html',{'student':student})


@login_required
def deposit_fees(request):
    if request.method == 'POST':
        form = SelectStudentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data.get('student')
            user = student.user
            context ={'list':user}
            form.save(commit=False)
            return render(request,'school/payment/student_select.html',context)
    else:
        form = SelectStudentForm()
    return render(request,'school/payment/deposit_fees.html',{'form':form})


@login_required
def payment_form(request,pk):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=pk)
            classroom = user.profile.classroom
            class_room = ClassRoom.objects.get(classname=classroom)
            amount = form.cleaned_data.get('amount')
            month = form.cleaned_data.get('month')
            payment=Payment(user=user,classroom=class_room,amount=amount,month=month)
            payment.save()
            text = "Your fees of amount {} is deposited .".format(amount)
            msg = StudentMessage(user=user,msg=text)
            msg.save()
            count = MessageCount(user=user)
            count.save()
            messages.success(request, 'Fees Deposited Successfully')
            try:
                payload = {"head":"Praxis", "body":text}
                send_user_notification(user=user, payload=payload,ttl=1000)
            except:
                pass
            # html = render_to_string('school/payment/payment_pdf.html', {'user': user,
            #                                                             'amount':amount,
            #                                                             'month':month})
            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'filename="Invoice.pdf"'
            # weasyprint.HTML(string=html).write_pdf(response,
            #                            stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
            # return response
    else:
        form = PaymentForm()
    return render(request,'school/payment/payment_form.html',{'form':form})

@login_required
def manage_fees(request):
    return render(request,'school/payment/manage_fees.html')


@login_required
def student_search(request):
    if request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data.get('student')
            option = form.cleaned_data.get('option')
            if option == 'view':
                try:
                    user = student.user
                    payment = Payment.objects.filter(user=user)
                    context ={'list':payment,'user':user}
                    form.save(commit=False)
                    return render(request,'school/payment/student_fees_detail.html',context)
                except:
                    pass
            elif option == 'download':
                try:
                    user = student.user
                    payment = Payment.objects.filter(user=user)
                    html = render_to_string('school/payment/payment_pdf.html', {'user': user,
                                                                             'payment':payment})
                    response = HttpResponse(content_type='application/pdf')
                    response['Content-Disposition'] = 'filename="Invoice.pdf"'
                    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
                    return response
                except:
                    pass

    else:
        form = SelectForm()
    return render(request,'school/payment/student_search.html',{'form':form})


@login_required
def search_by_month(request):
    if request.method == 'POST':
        form = SearchByMonthForm(request.POST)
        if form.is_valid():
            classroom = form.cleaned_data.get('classroom')
            class_room = ClassRoom.objects.get(classname=classroom)
            month = form.cleaned_data.get('month')
            payment = Payment.objects.filter(classroom=class_room, month=month)
            context = {'pay':payment}
            return render(request,'school/payment/monthly_fees.html',context)
    else:
        form = SearchByMonthForm()
    return render(request,'school/payment/fees_by_month.html',{'form':form})
