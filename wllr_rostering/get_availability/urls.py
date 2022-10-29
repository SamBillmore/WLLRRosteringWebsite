from django.urls import path
from . import views


urlpatterns = [
    path("", views.timetable_dates_colours, name='timetable')
]
