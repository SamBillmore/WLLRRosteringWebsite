# Generated by Django 4.1.2 on 2022-10-30 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableCrewRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timetable', models.CharField(max_length=25)),
                ('turn', models.PositiveSmallIntegerField()),
                ('points', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimetableDatesColours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('timetable', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MasterRoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.CharField(max_length=10)),
                ('driver', models.CharField(max_length=100)),
                ('fireman', models.CharField(max_length=100)),
                ('trainee', models.CharField(max_length=100)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_availability.timetabledatescolours')),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_availability.timetablecrewrequirements')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=25)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_availability.timetabledatescolours')),
            ],
        ),
    ]
