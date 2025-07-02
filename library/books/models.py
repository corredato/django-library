from django.db import models
from authors.models import Author

#TODO: https://isbndb.com/isbndb-api-documentation-v2

class Book(models.Model):
    title = models.CharField(max_length=200, default='Title')
    title_long = models.CharField(max_length=200, default='Long title')
    isbn = models.CharField(max_length=200, default='ISBN')
    isbn_13 = models.CharField(max_length=200, default='ISBN 13')
    dewey_decimal = models.CharField(max_length=200, default='Dewey decimal')  # TODO: dict inside list? [{}]
    #binding = models.CharField(max_length=200)
    #publisher = models.CharField(max_length=200, default='Publisher') # TODO: ''.join() strings
    #date_published = models.DateField(null=True) # TODO: maybe many2many like authors field
    edition = models.CharField(max_length=200, default='Edition')
    pages = models.CharField(max_length=200, default='Pages')
    dimensions = models.CharField(max_length=200, default='Dimensions')
    dimensions_structured = models.CharField(max_length=200, default='Dimensions structured')  # TODO
    overview = models.TextField(default='Overview')
    excerpt = models.TextField(default='Excerpt')
    msrp = models.IntegerField(default=0)
    synopsis = models.CharField(max_length=200, default='Synopsis')
    #subjects = models.CharField(max_length=200, default='Subjects')  # TODO: ''.join() strings
    reviews = models.CharField(max_length=200, default='Reviews')  # TODO: ''.join() review strings
    authors = models.ManyToManyField(Author) #TODO: for author in self ''.join() authors names
