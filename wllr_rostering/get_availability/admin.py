from django.contrib import admin
from wllr_rostering.get_availability.models import TimetableCrewRequirements, TimetableDatesColours, Availability, MasterRoster


class TimetableCrewRequirementsAdmin(admin.ModelAdmin):
    pass


class TimetableDatesColoursAdmin(admin.ModelAdmin):
    pass


class AvailabilityAdmin(admin.ModelAdmin):
    pass


class MasterRosterAdmin(admin.ModelAdmin):
    pass


admin.site.register(TimetableCrewRequirements, TimetableCrewRequirementsAdmin)
admin.site.register(TimetableDatesColours, TimetableDatesColoursAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(MasterRoster, MasterRosterAdmin)
