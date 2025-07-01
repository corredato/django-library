from django.db import models
#from ..books.models import Book


class Subject(models.Model):
    name = models.CharField(default='Name')
    #books = models.ManyToManyField(Book)