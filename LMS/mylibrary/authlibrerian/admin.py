from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('userId', 'user_name', 'email', 'role', 'is_active', 'is_staff', 'created_date', 'updated_date')
    search_fields = ('user_name', 'email', 'role')
    list_filter = ('role', 'is_active', 'is_staff', 'created_date', 'updated_date')
    ordering = ('-created_date',)

admin.site.register(User, UserAdmin)
