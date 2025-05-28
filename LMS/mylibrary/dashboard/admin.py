from django.contrib import admin
from .models import Dashboard, OverdueBorrower

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ("id", "total_student_count", "total_book_count", "total_transaction_count", "total_borrowed_books", "total_returned_books")

@admin.register(OverdueBorrower)
class OverdueBorrowerAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "borrowed_id")
