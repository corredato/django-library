from django.db import models
from books.models import Book


class Publisher(models.Model):
    name = models.CharField(default='Name')
    books = models.ManyToManyField(Book)
