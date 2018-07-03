from django.shortcuts import render
from .forms import PushForm
from webpush import send_user_notification
from django.contrib.auth.models import User
# Create your views here.
def push_home(request):
    if request.method == 'POST':
        form = PushForm(request.POST)
        if form.is_valid():
            message = request.POST['msg']
            payload = {"head":"school", "body":message, 'icon': '/static/icons/push.png'}
            user = User.objects.all()
            try:
                for user in user:
                    send_user_notification(user=user, payload=payload,ttl=1000)
            except:
                pass
    else:
        form = PushForm()
    return render(request,'school/push/push_home.html',{'form':form})
