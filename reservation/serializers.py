from rest_framework import serializers

from book.serializers import BookSerializer
from reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'book', 'date_reservation', 'date_reservation_final']