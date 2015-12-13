from django.db import models
from django.utils import timezone

class divisions(models.Model):
    Branch_name = models.CharField(max_length=75)
    AS_code = models.CharField(max_length=3)

    def __str__(self):
        return (self.Branch_name)

    def __unicode__(self):
        return (self.Branch_name)