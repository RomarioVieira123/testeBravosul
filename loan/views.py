
from rest_framework.response import Response
from rest_framework.views import APIView
from loan.facade import LoanFacade
from loan.models import Loan
from loan.serializers import LoanSerializer


class LoanView(APIView):

    def get(self, request, pk):
        #Buscar livros emprestados que não foram devolvidos pelo usuário e gerar suas respectivas multas (* apenas visualização), caso exista atraso.
        loan = Loan.objects.filter(user__id=pk).filter(date_returned=None).first()
        if loan is None:
            return Response({"sucess": True, "loan": None})

        loan_facade = LoanFacade()
        serializer = LoanSerializer(loan)
        #Gerar a visualização com a multa calculada caso exista.
        loan_penalty = loan_facade.calculate_penalty_view(loan)

        return Response({'loan': serializer.data, 'penalty': loan_penalty.data})


    def post(self, request, pk):
        return Response({"Request not implemented!"})


    def delete(self, request, pk):
        return Response({"Request not implemented!"})
