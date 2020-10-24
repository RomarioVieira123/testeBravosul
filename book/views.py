from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from book.facade import BookFacade
from book.models import Book
from book.serializers import BookSerializer
from loan.models import Loan


class BookView(APIView):

    def get(self, request):
        books = Book.objects.all()
        if books is None:
            return Response({'sucess': True, 'book': None})

        book_facade = BookFacade()
        book = book_facade.create_book_penalty(books)

        return Response({'sucess': True, 'book': book})

    def post(self, request):
        return Response({"Request not implemented!"})

    def delete(self, request):
        return Response({"Request not implemented!"})




