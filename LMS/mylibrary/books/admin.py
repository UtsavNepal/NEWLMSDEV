from django.contrib import admin
from .models import Book
 
class BookAdmin(admin.ModelAdmin):
    list_display = ('bookid', 'isbn', 'title', 'genre', 'authorid', 'quantity','is_deleted')
    search_fields = ('title', 'authorid', 'isbn')
    list_filter = ('is_deleted','genre', 'authorid')
    ordering = ('-bookid',)
 
admin.site.register(Book, BookAdmin)
 