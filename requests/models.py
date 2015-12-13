from django.db import models
from django.utils import timezone
from divisions.models import divisions
from request_types.models import request_types
from request_status.models import request_status

class Lists(models.Model):
    Initiator = models.ForeignKey('auth.User')
    Division = models.ForeignKey('divisions.divisions')
    request_type_id = models.ForeignKey('request_types.request_types')
    purchase_purpose = models.CharField(max_length=150)
    product_name = models.CharField(max_length=75)
    product_price = models.FloatField(default=1)
    product_quantity = models.FloatField(default=1)
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    approved_date_head = models.DateTimeField(
            blank=True, null=True)
    approved_date_admin = models.DateTimeField(
            blank=True, null=True)
    approved_date_fin = models.DateTimeField(
            blank=True, null=True)
    approved_date_CEO_DCEO = models.DateTimeField(
            blank=True, null=True)
    status_id = models.ForeignKey(request_status,related_name="request_status")


    def publish(self):
        self.approved_date_CEO_DCEO = timezone.now()
        self.save()

    def __str__(self):
        return self.product_name