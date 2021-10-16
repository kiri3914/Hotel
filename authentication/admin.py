from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'image', 'email')
    readonly_fields = ('image',)
