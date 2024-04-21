from django.contrib import admin

from mainapp.models import Lecture
from mainapp.models import Subject
from mainapp.models import Faculty
from mainapp.models import Student

# Register your models here.


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name', 'subject']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    search_fields = ['name', 'faculty', 'subjects']
