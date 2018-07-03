from django.shortcuts import render, redirect
from . forms import EventForm
from . models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request,'school/event/school_event_home.html')

@login_required
def all(request):
    event = Event.objects.all()
    context = {'list':event}
    return render(request,'school/event/school_event_all.html',context)

@login_required
def create(request):
    user = request.user
    if user.id <= 2:
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Event created successfully')
    else:
        return redirect("school_event_home")
    form = EventForm()
    return render(request,'school/event/school_event_create.html',{'form': form})


@login_required
def delete(request ,pk):
    user = request.user
    if user.id <=2:
        event =Event.objects.get(pk=pk)
        event.delete()
    else:
        return redirect("school_event_all")
    return redirect("school_event_all")
