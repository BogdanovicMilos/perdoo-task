from django.urls import path

from .views import SchedulerView, SchedulerListView

app_name = 'scheduler'

urlpatterns = [
    path('create/', SchedulerView.as_view(), name='schedule'),
    path('list/', SchedulerListView.as_view(), name='schedule-list'),
]