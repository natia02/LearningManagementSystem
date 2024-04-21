from django.db import models
from django.utils.translation import gettext_lazy as _

from mainapp.models.faculty import Faculty
from mainapp.models.subject import Subject


class Student(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name=_("Faculty"))
    subjects = models.ManyToManyField(Subject, limit_choices_to=7, verbose_name=_("Subjects"))
    name = models.CharField(max_length=100, verbose_name=_("First Name"))
    surname = models.CharField(max_length=100, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
