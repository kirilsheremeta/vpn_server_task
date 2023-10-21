from django.db import models
from django.contrib.auth.models import User


class VPNStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_url = models.URLField()
    data_sent = models.BigIntegerField()
    data_received = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_url
