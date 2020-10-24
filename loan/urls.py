from django.urls import path

from loan.views import LoanView

urlpatterns = [
    # Container commands
    path('loan/client/<int:pk>/books', LoanView.as_view()),

]