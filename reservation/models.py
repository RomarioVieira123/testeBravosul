from django.contrib.auth.models import User
from django.db import models

from book.models import Book


class Reservation(models.Model):
    user = models.ForeignKey(User, related_name='reservation', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reservation', on_delete=models.CASCADE)
    active = models.BooleanField(default=False, null=True, blank=True)
    date_reservation = models.DateField(null=True)
    date_reservation_final = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

