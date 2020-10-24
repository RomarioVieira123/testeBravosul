from django.contrib.auth.models import User
from django.db import models

from book.models import Book


class Loan(models.Model):
    book = models.OneToOneField(Book, related_name='loan', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='loan', on_delete=models.CASCADE)
    loan_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    date_returned = models.DateField(null=True, blank=True)