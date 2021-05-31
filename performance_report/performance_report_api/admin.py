from django.contrib import admin
from .models import PerformanceReport
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(PerformanceReport)

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    readonly_fields = ('id',)
admin.site.register(User, CustomUserAdmin)