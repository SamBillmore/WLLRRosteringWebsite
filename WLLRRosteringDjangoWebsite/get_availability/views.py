from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Timetable, UserAvailability


@login_required
def availability_view(request):
    user = "Test user 3"  # TODO: Get the current user: request.user

    # Get all available dates
    timetables = Timetable.objects.all().order_by('timetable_date')

    # Get the user's existing availability
    user_availability = {ua.timetable_id.id: ua.selected for ua in UserAvailability.objects.filter(user__name=user)}

    # Count the number of users available per timetable date
    availability_counts = (
        UserAvailability.objects.filter(selected=True)
        .values('timetable_id')
        .annotate(count=Count('user'))
    )

    # Convert counts to a dictionary for easy access in the template
    availability_dict = {entry['timetable_id']: entry['count'] for entry in availability_counts}

    if request.method == "POST":
        selected_dates = request.POST.getlist("availability")  # List of selected timetable IDs

        # Update or create availability records
        for timetable in timetables:
            selected = str(timetable.id) in selected_dates
            availability, created = UserAvailability.objects.get_or_create(
                user=user, timetable_id=timetable, defaults={"selected": selected}
            )
            if not created:
                availability.selected = selected
                availability.save()

        return redirect('availability')  # Redirect to refresh the page

    return render(request, "get_availability/availability.html", {
        "timetables": timetables,
        "user_availability": user_availability,
        "availability_dict": availability_dict
    })
