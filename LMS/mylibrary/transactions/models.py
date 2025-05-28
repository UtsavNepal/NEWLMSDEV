from django.db import models
from student.models import Student
from books.models import Book
from authlibrerian.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('borrow', 'Borrow'),
        ('return', 'Return'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Librarian handling the transaction
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)  # Book being borrowed/returned
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)  # Student borrowing/returning the book
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateTimeField()  # Transaction timestamp
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    def __str__(self):
        return self.title
