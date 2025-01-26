from django.contrib import admin
from .models import Timetable, User, UserAvailability


admin.site.register(User)
admin.site.register(Timetable)
admin.site.register(UserAvailability)
