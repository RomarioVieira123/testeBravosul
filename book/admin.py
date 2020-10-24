from django.contrib import admin

# Register your models here.
from book.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book,  BookAdmin)
