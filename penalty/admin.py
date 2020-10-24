from django.contrib import admin

from penalty.models import Penalty


class PenaltyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Penalty, PenaltyAdmin)

