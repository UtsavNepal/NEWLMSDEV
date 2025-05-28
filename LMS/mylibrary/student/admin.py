from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentid', 'name', 'email', 'faculty', 'contact_no', 'is_deleted')
    search_fields = ('name', 'email', 'faculty')
    list_filter = ('is_deleted', 'faculty')
    ordering = ('-studentid',)

admin.site.register(Student, StudentAdmin)
