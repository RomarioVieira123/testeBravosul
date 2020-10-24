from django.contrib import admin

from reservation.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reservation, ReservationAdmin)
