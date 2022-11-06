from django.urls import path
from wllr_rostering.get_availability import views


urlpatterns = [
    path("", views.input_availability, name='availability'),
]
