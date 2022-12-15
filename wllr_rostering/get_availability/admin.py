from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from wllr_rostering.get_availability.models import TimetableCrewRequirements, TimetableDatesColours, Availability, MasterRoster


class TimetableCrewRequirementsAdmin(ImportExportModelAdmin):
    list_display = ['timetable','turn','points']


class TimetableDatesColoursAdmin(ImportExportModelAdmin):
    list_display = ['date', 'timetable']


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'date']


class MasterRosterAdmin(admin.ModelAdmin):
    list_display = ['date', 'timetable', 'turn', 'driver', 'fireman', 'trainee']


admin.site.register(TimetableCrewRequirements, TimetableCrewRequirementsAdmin)
admin.site.register(TimetableDatesColours, TimetableDatesColoursAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(MasterRoster, MasterRosterAdmin)
