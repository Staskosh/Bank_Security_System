from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import datetime, timedelta


def is_visit_long(visit, seconds):
    entered_time = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at)
    duration = leaved_at - entered_time
    is_strange = duration.total_seconds() >= seconds
    return is_strange


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    user_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in user_visits:
        entered_time = localtime(visit.entered_at)
        leaved_at = localtime(visit.leaved_at)
        duration = leaved_at - entered_time
        flag = is_visit_long(visit, seconds=3600)
        this_passcard_visits.append({
            'entered_at': entered_time,
            'duration': duration,
            'is_strange': flag,
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
