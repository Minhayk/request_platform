from django.db import models
from django.utils import timezone

class request_status(models.Model):
    status = models.TextField(default="Ընթացիկ")
    def __str__(self):
        return (self.status)

    def __unicode__(self):
        return (self.status)
