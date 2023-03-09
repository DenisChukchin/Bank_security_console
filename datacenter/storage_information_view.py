from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def storage_information_view(request):
    visiters = Visit.objects.filter(leaved_at__isnull=True)   
    non_closed_visits = []
    for visiter in visiters:
        total_seconds = get_duration(visiter)
        entered_at = localtime(visiter.entered_at)
        stayed_inside = {
            "who_entered": visiter.passcard.owner_name,
            "entered_at": entered_at.strftime("%d.%m.%Y %H:%M"),
            "duration": format_duration(total_seconds),
            "is_strange": is_visit_long(visiter, seconds=3600)
        }
        non_closed_visits.append(stayed_inside)    
    context = {
        "non_closed_visits": non_closed_visits
    }
    return render(request, "storage_information.html", context)
