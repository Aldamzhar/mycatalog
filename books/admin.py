from django.contrib import admin
from .models import Book, Review, Genre, Author

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Author)
