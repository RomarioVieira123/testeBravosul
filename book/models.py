from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, default='')
    publishing_company = models.CharField(max_length=50, default='')
    edition = models.CharField(max_length=50, default='')
    year_publication = models.CharField(max_length=4, default='')
    created_at = models.DateTimeField(auto_now_add=True)
