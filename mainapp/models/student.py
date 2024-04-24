from django.db import models
from django.utils.translation import gettext_lazy as _

from .faculty import Faculty
from .subject import Subject

from django.contrib.auth import get_user_model


class Student(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'))
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        verbose_name=_("Faculty"))
    subjects = models.ManyToManyField(
        Subject,
        related_name="subjects",
        verbose_name=_("Subjects"),
        blank=True)
    name = models.CharField(max_length=100, verbose_name=_("First Name"))
    surname = models.CharField(max_length=100, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
