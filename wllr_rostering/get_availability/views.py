from django.shortcuts import render, redirect
import logging
from datetime import datetime

from wllr_rostering.get_availability.view_helpers import get_timetable_data
from wllr_rostering.get_availability.forms import AvailabilityForm
from wllr_rostering.get_availability.models import Availability

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def input_availability(request):
    if request.method == 'POST':
        post = request.POST.copy()
        request_dict = dict(request.POST)
        for date_string in request_dict['date']:
            formatted_date = datetime.strptime(date_string, '%Y-%m-%d').date()
            post['date'] = formatted_date
            save_data = {
                'name': post['name'],
                'grade': post['grade'],
                'date': post['date'],
            }
            availability = Availability(**save_data)
            try:
                availability.full_clean()
            except:
                return redirect("/availability/name_error")
            else:
                availability.save()
        return redirect("/availability/thank_you")
    else:
        form = AvailabilityForm()

    availability_by_timetable = get_timetable_data()

    context = {
        'form': form,
        'availability_by_timetable': availability_by_timetable
    }

    return render(request, 'input_availability.html', context)


def name_error(req):
    return render(req, 'name_error.html')


def thank_you(req):
    return render(req, 'thank_you.html')
