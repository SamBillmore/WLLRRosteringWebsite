from django.urls import path

from . import views

app_name = "get_availability"
urlpatterns = [
    path("", views.availability_view, name="availability_view"),
]
