from django.db import models

class Author(models.Model):
    name = models.CharField(default='Name')
    #books = models.ManyToManyField(Book) TODO: import book class inside method