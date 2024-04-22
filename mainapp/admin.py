from django.contrib import admin

from .models.lecturer import Lecturer
from .models.student import Student
from .models.faculty import Faculty
from .models.subject import Subject

# Register your models here.


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'faculty']
    search_fields = ['name', 'surname', 'faculty']
    list_filter = ['name', 'surname', 'faculty']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description']
    search_fields = ['title']
    list_filter = ['title']

