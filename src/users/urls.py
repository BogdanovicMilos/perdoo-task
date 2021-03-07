from django.urls import path

from .views import SignUpView, LogInView, LogOutView

app_name = 'users'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
]