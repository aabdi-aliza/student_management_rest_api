from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "roll_number", "course", "owner")
    search_fields = ("name", "email", "roll_number")
    list_filter = ("course",)
