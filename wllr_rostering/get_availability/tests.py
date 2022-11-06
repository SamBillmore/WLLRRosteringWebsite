from django.test import TestCase
import datetime

from wllr_rostering.get_availability.models import TimetableDatesColours, TimetableCrewRequirements, Availability
from wllr_rostering.get_availability.view_helpers import get_timetable_data


class TimetableDatesColoursTestCase(TestCase):
    
    def setUp(self):
        TimetableDatesColours.objects.create(date=datetime.date(2022, 1, 1), timetable='Blue')
        TimetableDatesColours.objects.create(date=datetime.date(2022, 1, 2), timetable='Green')
        TimetableCrewRequirements.objects.create(timetable='Blue', turn=1, points=10)
        TimetableCrewRequirements.objects.create(timetable='Blue', turn=2, points=20)
        TimetableCrewRequirements.objects.create(timetable='Green', turn=1, points=30)
        TimetableCrewRequirements.objects.create(timetable='Green', turn=2, points=40)
        TimetableCrewRequirements.objects.create(timetable='Green', turn=3, points=50)
        Availability.objects.create(name='Gungby', grade='driver', date=datetime.date(2022, 1, 1))
        Availability.objects.create(name='Trev', grade='driver', date=datetime.date(2022, 1, 1))
        Availability.objects.create(name='Kate', grade='fireman', date=datetime.date(2022, 1, 2))

    def test_views_get_timetable_data(self):
        """
        """
        output = get_timetable_data()
        expected = {
            0: {
                'id': 1,
                'date': datetime.date(2022, 1, 1),
                'timetable': 'Blue',
                'turns_to_be_covered': 2,
                'drivers_available': 2.0,
                'firemen_available': 0.0,
                'trainees_available': 0.0,
                'drivers_required': 0.0,
                'firemen_required': 2.0,
                'trainees_required': 2.0
            },
            1: {
                'id': 2,
                'date': datetime.date(2022, 1, 2),
                'timetable': 'Green',
                'turns_to_be_covered': 3,
                'drivers_available': 0.0,
                'firemen_available': 1.0,
                'trainees_available': 0.0,
                'drivers_required': 3.0,
                'firemen_required': 2.0,
                'trainees_required': 3.0
            }
        }
        self.assertEqual(output, expected)
