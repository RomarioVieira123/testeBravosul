from rest_framework import serializers
from book.serializers import BookSerializer
from loan.models import Loan


class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'book', 'user', 'loan_date', 'delivery_date', 'date_returned']

