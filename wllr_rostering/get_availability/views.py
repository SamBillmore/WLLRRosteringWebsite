from django.shortcuts import render, redirect
import logging

from wllr_rostering.get_availability.view_helpers import get_timetable_data
from wllr_rostering.get_availability.forms import AvailabilityForm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def input_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        logger.info(f"Name: {form['name'].value()}")
        logger.info(f"Grade: {form['grade'].value()}")
        logger.info(f"Dates: {form['dates'].value()}")
        return redirect("/availability")
    else:
        form = AvailabilityForm()

    availability_by_timetable = get_timetable_data()

    context = {
        'form': form,
        'availability_by_timetable': availability_by_timetable
    }

    return render(request, 'input_availability.html', context)
