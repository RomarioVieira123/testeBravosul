from rest_framework import serializers

from loan.serializers import LoanSerializer
from penalty.models import Penalty


class PenaltySerializer(serializers.ModelSerializer):
    loan = LoanSerializer(read_only=True)

    class Meta:
        model = Penalty
        fields = ['id', 'loan', 'delayed_days', 'fine_amount', 'penalty_fee', 'interest_per_day', 'total_paid']


class PenaltyViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Penalty
        fields = ['delayed_days', 'fine_amount', 'penalty_fee', 'interest_per_day', 'total_paid']