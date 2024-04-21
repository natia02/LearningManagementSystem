from django.db import models


# Create your models here.


class Lecture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    syllabus = models.FileField(upload_to='syllabus/')
    lecturer = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, related_name='faculty')

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    subjects=models.ManyToManyField(Subject, related_name='students', blank=True, limit_choices_to=7)
    def __str__(self):
        return self.name
