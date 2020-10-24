import json
from datetime import date, datetime

from django.contrib.auth.models import User
from book.models import Book
from core.settings import PENALTY
from loan.models import Loan
from loan.serializers import LoanSerializer
from penalty.serializers import PenaltySerializer, PenaltyViewSerializer
from pricing.models import Pricing


class LoanFacade:

    def create(self, data, pk):
        db = Database()
        serializer = LoanSerializer(db.save(data, pk))

        return serializer.data

    def calculate_date_difference(self, delivery_date):
        return (date.today() - delivery_date)

    def calculate_penalty_view(self, loan):
        loan_facade = LoanFacade()
        # Calcular a diferença de entre a data prevista de entrega e a data atual.
        delay = loan_facade.calculate_date_difference(loan.delivery_date)

        if delay.days <= 0:
            pricing = Pricing.objects.filter(delayed_days="Without delay").first()
            penalty = {
                'delayed_days': delay.days, #Dias em atraso
                'fine_amount': PENALTY, #Valor fixo da multa.
                'penalty_fee': (PENALTY * (pricing.penalty / 100)), #Valor da multa,
                'interest_per_day': ((PENALTY * delay.days) * (pricing.interest_per_day / 100)), #Valor juros por dia
                'total_paid': (PENALTY+ (PENALTY * (pricing.penalty / 100)) + ((PENALTY * delay.days) * (pricing.interest_per_day / 100))), #Valor fixo da multa + valor da multa + valor juros por dia.
            }

            loan_penalty = PenaltyViewSerializer(penalty)
            return loan_penalty

        elif delay.days > 0 and delay.days <= 3:
            pricing = Pricing.objects.filter(delayed_days="Up to 3 days").first()
            penalty = {
                'delayed_days': delay.days, #Dias em atraso
                'fine_amount': PENALTY, #Valor fixo da multa.
                'penalty_fee': (PENALTY * (pricing.penalty / 100)), #Valor da multa,
                'interest_per_day': ((PENALTY * delay.days) * (pricing.interest_per_day / 100)), #Valor juros por dia
                'total_paid': (PENALTY+ (PENALTY * (pricing.penalty / 100)) + ((PENALTY * delay.days) * (pricing.interest_per_day / 100))), #Valor fixo da multa + valor da multa + valor juros por dia.
            }

            loan_penalty = PenaltyViewSerializer(penalty)
            return loan_penalty


        elif delay.days > 3 and delay.days <= 5:
            pricing = Pricing.objects.filter(delayed_days="Above 3 days").first()
            penalty =  {
                'delayed_days': delay.days, #Dias em atraso
                'fine_amount': PENALTY, #Valor fixo da multa.
                'penalty_fee': (PENALTY * (pricing.penalty / 100)), #Valor da multa,
                'interest_per_day': ((PENALTY * delay.days) * (pricing.interest_per_day / 100)), #Valor juros por dia
                'total_paid': (PENALTY+ (PENALTY * (pricing.penalty / 100)) + ((PENALTY * delay.days) * (pricing.interest_per_day / 100))), #Valor fixo da multa + valor da multa + valor juros por dia.
            }

            loan_penalty = PenaltyViewSerializer(penalty)
            return loan_penalty


        elif delay.days > 5:
            pricing = Pricing.objects.filter(delayed_days="Above 5 days").first()
            penalty = {
                'delayed_days': delay.days, #Dias em atraso
                'fine_amount': PENALTY, #Valor fixo da multa.
                'penalty_fee': (PENALTY * (pricing.penalty / 100)), #Valor da multa,
                'interest_per_day': ((PENALTY * delay.days) * (pricing.interest_per_day / 100)), #Valor juros por dia
                'total_paid': (PENALTY+ (PENALTY * (pricing.penalty / 100)) + ((PENALTY * delay.days) * (pricing.interest_per_day / 100))), #Valor fixo da multa + valor da multa + valor juros por dia.
            }

            loan_penalty = PenaltyViewSerializer(penalty)
            return loan_penalty

class Database:
    def save(self, data, pk):
        book = Book.objects.filter(id=data['id']).first()
        user = User.objects.filter(id=pk).first()

        loan = Loan.objects.create(
            book=book,
            user=user,
            loan_date=data.get('loan_date'),
            delivery_date=data.get('delivery_date'),
            date_returned=data.get('date_returned'),
        )
        return loan
