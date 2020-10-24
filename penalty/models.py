from django.db import models

from loan.models import Loan


class Penalty(models.Model):
    loan = models.OneToOneField(Loan, related_name='penalty', on_delete=models.CASCADE)
    delayed_days = models.IntegerField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    penalty_fee = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    interest_per_day = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_paid = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
