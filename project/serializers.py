from rest_framework import serializers
from .models import Book, Opinion


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ("id", "rating", "description")


class BookSerializer(serializers.ModelSerializer):
    opinions = OpinionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "isbn", "opinions"]
