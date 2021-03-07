from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import SchedulerForm, SchedulerListForm
from .models import Scheduler
from apscheduler.schedulers.background import BackgroundScheduler
from .scheduler import schedule


class SchedulerView(FormView):
    template_name = 'scheduler/schedule.html'
    form_class = SchedulerForm

    def form_valid(self, form):
        validate = URLValidator()

        if self.request.method == 'POST':
            form = SchedulerForm(self.request.POST)

            if form.is_valid():
                try:
                    validate(form.cleaned_data['url'])
                    form_obj = form.save(commit=False)
                    form_obj.user = self.request.user
                    form_obj.save()
                    scheduler = BackgroundScheduler()
                    date = str(form.cleaned_data['date'])[:19]
                    scheduler.add_job(schedule, 'date', run_date=date, args=[form.cleaned_data, form_obj.pk])
                    scheduler.start()
                    messages.success(self.request, 'Request submitted successfully')
                    return HttpResponseRedirect(reverse_lazy('scheduler:schedule'))
                except ValidationError:
                    messages.error(self.request, 'Not a valid URL')
                    return HttpResponseRedirect(reverse_lazy('scheduler:schedule'))


class SchedulerListView(TemplateView):
    template_name = 'scheduler/schedule_list.html'
    form_class = SchedulerListForm

    def get(self, request, *args, **kwargs):
        requests = Scheduler.objects.filter(user=self.request.user.id)
        if requests:
            return render(request, 'scheduler/schedule_list.html', {'requests': requests})
        return super().get(request, *args, **kwargs)
