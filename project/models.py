from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    isbn = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        isbn = int(self.isbn)
        super().save(*args, **kwargs)


class Opinion(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="opinions")
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id}-{self.book}"
