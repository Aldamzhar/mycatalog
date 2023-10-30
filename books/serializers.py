from rest_framework import serializers
from .models import Book, Review, Genre, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

# Сериализаторы для Genre и Author аналогично
