from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Opinion
from .serializers import BookSerializer, OpinionSerializer

# Create your views here.
@api_view()
def books(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)

    return Response(serializer.data)


@api_view()
def book(request, title):
    book = Book.objects.get(title=title)
    serializer = BookSerializer(book)

    return Response(serializer.data)
