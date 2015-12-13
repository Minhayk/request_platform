from django import forms
from .models import Lists

class RequestForm(forms.ModelForm):

    class Meta:
        model = Lists
        fields = ('Initiator','Division','request_type_id','purchase_purpose','product_name','product_price','product_quantity','comment','status_id')
