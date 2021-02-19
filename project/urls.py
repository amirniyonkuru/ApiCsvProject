from django.urls import path
from . import views

urlpatterns = [
    path("book/", views.books, name="books"),
    path("book/<str:title>", views.book, name="book"),
]