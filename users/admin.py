from django.contrib import admin
from mainapp.models.student import Student
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    actions = ['create_student']


admin.site.register(User, CustomUserAdmin)


def create_student(modeladmin, request, queryset):
    for user in queryset:
        Student.objects.create(user=user)


create_student.short_description = "Create Student"
