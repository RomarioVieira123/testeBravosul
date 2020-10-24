from book.models import Book
from book.serializers import BookSerializer
from loan.models import Loan


class BookFacade:

    def create(self, data):
        db = Database()
        serializer = BookSerializer(db.save(data))

        return serializer.data

    def delete(self, pk):
        book = Book.objects.filter(id=pk).filter(status='A').first()
        if book is not None:
            book.delete()

        return None

    def create_book_penalty(self, books):
        full_books = []
        for book in books:
            loan = Loan.objects.filter(book__id=book.id).filter(date_returned=None).first()
            if loan is None:
                serializer = BookSerializer(book)
                body = {
                    'id': serializer.data['id'],
                    'title': serializer.data['title'],
                    'publishing_company': serializer.data['publishing_company'],
                    'edition': serializer.data['edition'],
                    'year_publication': serializer.data['year_publication'],
                    'status': 'available'
                }

                full_books.append(body)
            else:
                serializer = BookSerializer(book)
                body = {
                    'id': serializer.data['id'],
                    'title': serializer.data['title'],
                    'publishing_company': serializer.data['publishing_company'],
                    'edition': serializer.data['edition'],
                    'year_publication': serializer.data['year_publication'],
                    'status': 'borrowed'
                }

                full_books.append(body)

        return full_books


class Database:
    def save(self, data):
        book = Book.objects.create(
            title=data.get('title'),
            publishing_company=data.get('publishing_company'),
            edition=data.get('edition'),
            year_publication=data.get('year_publication'),
            status=data.get('status'),
        )
        return book