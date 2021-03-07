from django.db import models
from django.contrib.auth.models import User


class Scheduler(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')
