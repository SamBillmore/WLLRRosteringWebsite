from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # fieldsets = list(UserAdmin.fieldsets) + [
    #     ("Additional Info", {"fields": ["email"]}),
    # ]

    # Ensure email is displayed in the list view
    list_display = ("username", "email")
    search_fields = ("username", "email")  # Make email searchable

admin.site.register(CustomUser, CustomUserAdmin)
