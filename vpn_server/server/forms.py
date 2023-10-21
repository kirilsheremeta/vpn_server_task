from django.forms import CharField, DateField, ModelChoiceField, ModelForm, ModelMultipleChoiceField, Select, \
    SelectMultiple, TextInput, URLField, IntegerField
from sqlalchemy import ForeignKey


class VPNStatForm(ModelForm):
    user = ForeignKey()
    site_url = URLField()
    data_sent = IntegerField()
    data_received = IntegerField()
