from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visiters = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visiter in visiters:
        total_seconds = get_duration(visiter)
        duration_session = {
            "entered_at": visiter.entered_at,
            "duration": format_duration(total_seconds),
            "is_strange": is_visit_long(visiter, seconds=3600)
        }
        this_passcard_visits.append(duration_session)       
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, "passcard_info.html", context)
