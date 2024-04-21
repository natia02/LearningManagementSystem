from django.contrib import admin

from mainapp.models import Lecturer
from mainapp.models import Subject
from mainapp.models import Faculty
from mainapp.models import Student


# Register your models here.

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname']


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

