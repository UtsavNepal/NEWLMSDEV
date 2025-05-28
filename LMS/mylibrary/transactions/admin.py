from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'get_username', 'get_book_title', 'get_student_name', 'transaction_type', 'date', 'is_deleted')
    search_fields = ('student__name', 'book__title', 'user__user_name')
    list_filter = ('transaction_type', 'date')
    ordering = ('-transaction_id',)

    # Method to get username (Librarian)
    def get_username(self, obj):
        return obj.user.user_name  # Assuming 'user_name' is the field in the User model

    # Method to get book title
    def get_book_title(self, obj):
        return obj.bookid.title  # Assuming 'title' is the field in the Book model

    # Method to get student name
    def get_student_name(self, obj):
        return obj.studentid.name  # Assuming 'name' is the field in the Student model

    get_username.admin_order_field = 'user__user_name'  # Allow ordering by username
    get_book_title.admin_order_field = 'book__title'  # Allow ordering by book title
    get_student_name.admin_order_field = 'student__name'  # Allow ordering by student name

admin.site.register(Transaction, TransactionAdmin)
