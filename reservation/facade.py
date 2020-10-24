from datetime import timedelta, date

from django.contrib.auth.models import User

from book.models import Book
from reservation.models import Reservation
from reservation.serializers import ReservationSerializer


class ReservationFacade:

    def create(self, data, pk):
        db = Database()
        serializer = ReservationSerializer(db.save(data, pk))

        return serializer.data


class Database:
    def save(self, data, pk):
        book = Book.objects.filter(id=pk).first()
        user = User.objects.filter(id=data['id']).first()

        reservation = Reservation.objects.create(
            user=user,
            book=book,
            date_reservation=date.today(),
            date_reservation_final=date.today() + timedelta(days=3),
            active=True
        )

        return reservation
