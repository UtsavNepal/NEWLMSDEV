from rest_framework import serializers
from .models import Transaction
from books.models import Book
from student.models import Student
from authlibrerian.models import User

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # This will resolve the user ID to a User instance
    bookid = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())  # This will resolve the book ID to a Book instance
    studentid = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())  # This will resolve the student ID to a Student instance
    username = serializers.CharField(source='user.user_name', read_only=True)
    book_title = serializers.CharField(source='bookid.title', read_only=True)
    student_name = serializers.CharField(source='studentid.name', read_only=True)

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'user', 'bookid', 'studentid', 'transaction_type', 'date', 'username', 'book_title', 'student_name']
