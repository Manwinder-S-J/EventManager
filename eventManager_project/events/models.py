from django.db import models
from django.conf import settings

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True) 
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='registered_events', blank=True)

    def __str__(self):
        return self.name
