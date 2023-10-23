from django.db.models import Model, CASCADE, ForeignKey, CharField, URLField, DecimalField, PositiveIntegerField
from django.contrib.auth.models import User


class UsersWebsite(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=255)
    url = URLField()

    def __str__(self):
        return self.name


class WebsiteStatistics(Model):
    website = ForeignKey(UsersWebsite, on_delete=CASCADE)
    clicks = PositiveIntegerField(default=0)
    data_transferred = DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Statistics for {self.website.name}"
