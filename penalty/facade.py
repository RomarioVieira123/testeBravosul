from core.settings import PENALTY
from loan.models import Loan
from penalty.models import Penalty
from penalty.serializers import PenaltySerializer


class PenaltyFacade:
    pass

class Database:
    def save(self, data, pk):
        loan = Loan.objects.filter(user__id=pk).first()

        penalty = Penalty.objects.create(
            delayed_days=data.get('number_days'),
            penalty_fee=data.get('penalty_fee'),
            interest_per_day=data.get('interest_per_day'),
            total_paid=data.get('total_paid'),
            paid_out=data.get('paid_out'),
            loan=loan,
        )
        return penalty