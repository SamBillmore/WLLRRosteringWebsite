from django import forms
from django.forms import models

from wllr_rostering.get_availability.models import TimetableDatesColours, Availability


class CustomModelChoiceIterator(models.ModelChoiceIterator):
    """ Overwrites standard django method to also return obj.
    This allows the values of obj to be used.
    """
    def choice(self, obj):
        return (self.field.prepare_value(obj),
                self.field.label_from_instance(obj),
                obj)


class CustomModelChoiceField(models.ModelMultipleChoiceField):
    """ Overwrites standard django method and class variable `choices`
    (inherited by ModelMultipleChoiceField from ModelChoiceField)
    to use the CustomModelChoiceIterator.
    """
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return CustomModelChoiceIterator(self)

    choices = property(_get_choices, models.ModelMultipleChoiceField._set_choices)


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'

    name = forms.CharField(max_length = 100)
    grade = forms.CharField(max_length = 25)
    dates = CustomModelChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = TimetableDatesColours.objects.all()
    )
