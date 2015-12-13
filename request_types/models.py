from django.db import models
from django.utils import timezone

class request_types(models.Model):
    category = models.CharField(max_length=75)
    threshold = models.IntegerField(default=100000)

    def __str__(self):
        return (self.category)

    def __unicode__(self):
        return (self.category)