from django.contrib import admin

from loan.models import Loan


class LoanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Loan, LoanAdmin)

