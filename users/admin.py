from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mainapp.models.student import Student


def create_student(modeladmin, request, queryset):
    for user in queryset:
        Student.objects.create(user=user)


create_student.short_description = "Create Student"
