from django.urls import path
from reservation.views import ReservationView

urlpatterns = [
    # Container commands
    path('books/<int:pk>/reserve', ReservationView.as_view()),
]
