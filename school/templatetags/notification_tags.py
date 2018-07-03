from django import template
from django.db.models import Count
from django.contrib import messages
from leave.models import LeaveCount
from django.contrib.auth.models import User
from grievance.models import GrievanceCount

register = template.Library()

from ..models import MessageCount


@register.simple_tag(takes_context=True)
def notification(context):
    user = context['request'].user
    stu = MessageCount.objects.filter(user=user)
    total = stu.count()
    return total


@register.simple_tag()
def leave_count():
    user = User.objects.get(username='admin')
    stu = LeaveCount.objects.filter(user=user)
    total = stu.count()
    return total

@register.simple_tag()
def grievance_count():
    user = User.objects.get(username='admin')
    stu = GrievanceCount.objects.filter(user=user)
    total = stu.count()
    return total
