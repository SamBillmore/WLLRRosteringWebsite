from django.db.models import Count, Q
from django.shortcuts import render

from .models import Timetable


def index(request):
    timetable_summary = Timetable.objects.annotate(
        selected_count=Count("useravailability",
            filter=Q(useravailability__selected=True))
    ).order_by('timetable_date')

    context = {
        "timetable_summary": timetable_summary
    }
    return render(request, "get_availability/index.html", context)
