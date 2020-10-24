from django.db import models

class Pricing(models.Model):
    penalty = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    interest_per_day = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    delayed_days = models.CharField(max_length=50, default='')

