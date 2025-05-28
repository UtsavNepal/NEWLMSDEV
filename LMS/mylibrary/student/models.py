from django.db import models

class Student(models.Model):
    studentid = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=255)  # Student name
    email = models.EmailField(unique=True)  # Unique Email
    faculty = models.CharField(max_length=100)  # Faculty Name
    contact_no = models.CharField(max_length=15, unique=True)  # Contact Number
    is_deleted = models.BooleanField(default=False)  # Soft Delete

    def __str__(self):
        return self.name
