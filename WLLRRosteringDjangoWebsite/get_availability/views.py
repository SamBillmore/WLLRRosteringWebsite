from django.db.models import Count, Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Timetable


@login_required
def index(request):
    timetable_summary = Timetable.objects.annotate(
        selected_count=Count("useravailability",
            filter=Q(useravailability__selected=True))
    ).order_by('timetable_date')

    context = {
        "timetable_summary": timetable_summary
    }
    return render(request, "get_availability/index.html", context)
