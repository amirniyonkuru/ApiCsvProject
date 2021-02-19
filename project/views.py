from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Opinion
from .serializers import BookSerializer, OpinionSerializer

# Create your views here.


@api_view(["GET", "POST"])
def book(request):
    if request.method == "GET":
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        title = request.data.get("title")
        book = Book.objects.get(title=title)
        serializer = BookSerializer(book)

        return Response(serializer.data)
    else:
        pass
