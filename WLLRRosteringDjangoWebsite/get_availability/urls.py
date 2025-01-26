from django.urls import path

from . import views

app_name = "get_availability"
urlpatterns = [
    path("", views.index, name="index"),
]
