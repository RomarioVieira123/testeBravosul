from django.urls import path

from book.views import BookView

urlpatterns = [
    # Container commands
    path('books/', BookView.as_view()),

]