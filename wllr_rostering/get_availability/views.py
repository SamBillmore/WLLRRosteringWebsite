from django.shortcuts import render
from wllr_rostering.get_availability.models import TimetableDatesColours, TimetableCrewRequirements


def timetable_dates_colours(request):
    timetable_dates = TimetableDatesColours.objects.select_related('colour').all()
    # timetable_crew_reqs = TimetableCrewRequirements.objects.all()

    context = {
        'timetable_dates': timetable_dates,
        # 'timetable_crew_reqs': timetable_crew_reqs
    }
    return render(request, 'timetable_dates.html', context)
