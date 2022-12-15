from django.urls import path
from wllr_rostering.get_availability import views


urlpatterns = [
    path("", views.input_availability, name='availability'),
    path("name_error", views.name_error, name='name_error'),
    path("thank_you", views.thank_you, name='thank_you'),
]
