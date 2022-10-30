from django.db import models


class TimetableCrewRequirements(models.Model):
    """ Crew requirements per timetable colour
    """
    timetable = models.CharField(max_length=25)
    turn = models.PositiveSmallIntegerField()
    points = models.PositiveSmallIntegerField()


class TimetableDatesColours(models.Model):
    """ The running days and the timetable colour by day
    """
    date = models.DateField()
    timetable = models.CharField(max_length=25)


class Availability(models.Model):
    """ Availability by person
    """
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=25)
    date = models.ForeignKey('TimetableDatesColours', on_delete=models.CASCADE)


class MasterRoster(models.Model):
    """ Master roster for output
    """
    date = models.ForeignKey('TimetableDatesColours', on_delete=models.CASCADE)
    timetable = models.ForeignKey('TimetableCrewRequirements', on_delete=models.CASCADE)
    turn = models.CharField(max_length=10)
    driver = models.CharField(max_length=100)
    fireman = models.CharField(max_length=100)
    trainee = models.CharField(max_length=100)
