from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.forms import ModelForm
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from scheduler.models import Scheduler


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class SchedulerForm(ModelForm):

    class Meta:
        model = Scheduler
        fields = ['url', 'date']
        widgets = {
            'date': DateTimeInput(),
        }
        # widgets = {
        #     'url': forms.TextInput(attrs={'class': 'input', 'placeholder': 'url'}),
        #     'date': DateTimeInput(),
        # }


class SchedulerListForm(ModelForm):

    class Meta:
        model = Scheduler
        fields = ['url', 'date', 'status']