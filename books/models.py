from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    publish_date = models.DateField()
    favorited_by = models.ManyToManyField(User, related_name="favorited_books")

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    text = models.TextField()
