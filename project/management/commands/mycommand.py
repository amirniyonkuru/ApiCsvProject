from django.core.management.base import BaseCommand
from project.models import Book, Opinion
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        # i am opening 2 csv files at the same time
        with open("books.csv", "r") as fbook, open("opinions.csv", "r") as fopinion:
            books = csv.reader(fbook)
            opinions = csv.reader(fopinion)

            # l ooping through books and saving them
            for i, book in enumerate(books):
                if i == 0:
                    pass
                else:
                    book = "".join(book)
                    book = book.replace(";", ",")
                    book = book.split(",")

                    try:
                        obj_book = Book.objects.create(
                            title=book[1], author=book[2], genre=book[3], isbn=book[0]
                        )

                        obj_book.save()
                    except:
                        print("Book already exists")

            # looping through reviews and save each according to the corresponding book
            for i, opinion in enumerate(opinions):
                if i == 0:
                    pass
                else:
                    opinion = "".join(opinion)
                    opinion = opinion.replace(";", ",")
                    opinion = opinion.split(",")
                    isbn = opinion[0]
                    book = Book.objects.get(isbn=int(isbn))
                    print(book)
                    obj_opinion = Opinion(
                        book=book, rating=opinion[1], description=opinion[2]
                    )
                    obj_opinion.save()
