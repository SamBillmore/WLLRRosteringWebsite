import pandas as pd

from wllr_rostering.get_availability.models import TimetableDatesColours, TimetableCrewRequirements, Availability
from wllr_rostering.get_availability.grades_availabe import GRADE_OPTIONS


def _check_grade_naming(grade_to_check, list_positions):
    for position in list_positions:
        if GRADE_OPTIONS[position][0] != grade_to_check:
            raise ValueError('Code error: grade labels do not align')
    return grade_to_check


def availability_by_date(availability_df):
    if availability_df.empty:
        availability_df = pd.DataFrame(columns=['name', 'grade', 'date'])
    driver_availability_by_date_df = availability_df[availability_df['grade']==_check_grade_naming('driver', [0])] \
            .groupby('date') \
            .count() \
            .reset_index()[['date', 'grade']] \
            .rename(columns={'grade': 'drivers_available'})
    fireman_availability_by_date_df = availability_df[availability_df['grade']==_check_grade_naming('fireman', [1])] \
            .groupby('date') \
            .count() \
            .reset_index()[['date', 'grade']] \
            .rename(columns={'grade': 'firemen_available'})
    trainee_availability_by_date_df = availability_df[availability_df['grade']==_check_grade_naming('trainee', [2,3])] \
            .groupby('date') \
            .count() \
            .reset_index()[['date', 'grade']] \
            .rename(columns={'grade': 'trainees_available'})
    availability_by_date_df = pd.merge(
        left=driver_availability_by_date_df,
        right=pd.merge(
            left=fireman_availability_by_date_df,
            right=trainee_availability_by_date_df,
            left_on='date',
            right_on='date',
            how='outer'
        ),
        left_on='date',
        right_on='date',
        how='outer'
    )
    return availability_by_date_df


def max_timetable_crew_reqs(timetable_crew_reqs_df):
    max_timetable_crew_reqs_df = timetable_crew_reqs_df \
        .groupby('timetable') \
        .max('turn') \
        .reset_index()[['timetable', 'turn']] \
        .rename(columns={'turn': 'turns_to_be_covered'})
    return max_timetable_crew_reqs_df


def availability_by_timetable(timetable_dates_colours_df, max_timetable_crew_reqs_df, availability_by_date_df):
    def crews_required(row, turn_type):
        return max(row['turns_to_be_covered'] - row[f'{turn_type}_available'], 0)
    all_availability_by_date = pd.merge(
        left=pd.merge(
            left=timetable_dates_colours_df,
            right=max_timetable_crew_reqs_df,
            left_on='timetable',
            right_on='timetable',
            how='left'
        ),
        right=availability_by_date_df,
        left_on='date',
        right_on='date',
        how='left'
    ).fillna(0)
    for turn_type in ['drivers', 'firemen', 'trainees']:
        all_availability_by_date[f'{turn_type}_required'] = all_availability_by_date.apply(
            lambda row: crews_required(row, turn_type),
            axis=1
        )
    return all_availability_by_date


def get_timetable_data():
    timetable_dates_colours_df = pd.DataFrame(list(TimetableDatesColours.objects.all().values()))
    timetable_crew_reqs_df = pd.DataFrame(list(TimetableCrewRequirements.objects.all().values()))
    availability_df = pd.DataFrame(list(Availability.objects.all().values()))
        
    max_timetable_crew_reqs_df = max_timetable_crew_reqs(timetable_crew_reqs_df)
    availability_by_date_df = availability_by_date(availability_df)
    availability_by_timetable_df = availability_by_timetable(
        timetable_dates_colours_df, max_timetable_crew_reqs_df, availability_by_date_df
    )
    return availability_by_timetable_df.to_dict('index')
