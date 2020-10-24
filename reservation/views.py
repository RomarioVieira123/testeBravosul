from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from reservation.facade import ReservationFacade
from reservation.models import Reservation
from reservation.serializers import ReservationSerializer


class ReservationView(APIView):

    def get(self, request):
        return Response({"Request not implemented!"})


    def post(self, request, pk):
        reservation = Reservation.objects.filter(book__id=pk).filter(active=True).first()
        if reservation is not None:
            return Response({'sucess': True, 'reservation': 'Book already has reservation!'})

        reservation_facade = ReservationFacade()
        reservation = reservation_facade.create(request.data, pk)

        return Response({'sucess': True, 'reservation': reservation})

    def delete(self, request):
        return Response({"Request not implemented!"})
