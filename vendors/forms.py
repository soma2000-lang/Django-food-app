from django import forms
from .models import Vendor, OpeningHour
from account.validators  import allow_only_image_validators

class VendorForm(forms.Modelform)
    vendor_license=form.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model=Vendor
        fields=['vendor_name','vendor_license']
    class Meta:
        model=OpeningHour
        fields=['day', 'from_hour', 'to_hour', 'is_closed']
        