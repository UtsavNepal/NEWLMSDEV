from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorid', 'name', 'bio', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('is_deleted',)
    ordering = ('-authorid',)

admin.site.register(Author, AuthorAdmin)
