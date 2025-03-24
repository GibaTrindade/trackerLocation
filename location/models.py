from django.db import models

class AccessLog(models.Model):
    ip_address = models.CharField(max_length=100)
    access_time = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    isp = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ip_address} - {self.access_time}"
