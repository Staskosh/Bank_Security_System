from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import datetime, timedelta


def get_duration(visit):
    time_now = localtime()
    entered_time = localtime(visit.entered_at)
    duration = time_now - entered_time
    return duration


def storage_information_view(request):
    users_in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for user in users_in_storage:
        time_now = localtime()
        entered_time = localtime(user.entered_at)
        duration = time_now - entered_time
        who_entered = user.passcard
        non_closed_visits.append({
            'who_entered': who_entered,
            'entered_at': entered_time,
            'duration': duration,
        })
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
