from django.db import models

from Author.models import Author
 
class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    authorid = models.ForeignKey(Author, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_deleted = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title