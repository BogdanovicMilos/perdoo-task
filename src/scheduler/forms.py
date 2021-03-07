from django import forms
from django.forms import ModelForm
from scheduler.models import Scheduler


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class SchedulerForm(ModelForm):

    class Meta:
        model = Scheduler
        fields = ('url', 'date',)
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'input URL'}),
            'date': DateTimeInput(attrs={'class': 'form-control'}),
        }


class SchedulerListForm(ModelForm):

    class Meta:
        model = Scheduler
        fields = ('url', 'date', 'status',)