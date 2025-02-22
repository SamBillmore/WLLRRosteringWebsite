from django.db import models


class User(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    timetable_date = models.DateField()
    timetable_colour = models.CharField()

    def __str__(self) -> str:
        return self.timetable_date.strftime('%Y-%m-%d')


class UserAvailability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timetable_id = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    selected = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.user}_{self.timetable_id.timetable_date.strftime('%Y-%m-%d')}"
