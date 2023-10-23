from django.forms import ModelForm
from .models import UsersWebsite, WebsiteStatistics


class UserWebsiteForm(ModelForm):
    class Meta:
        model = UsersWebsite
        fields = ['name', 'url']


class WebsiteStatisticsForm(ModelForm):
    class Meta:
        model = WebsiteStatistics
        fields = ['clicks', 'data_transferred']