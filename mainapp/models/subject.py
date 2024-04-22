from django.db import models
from django.utils.translation import gettext_lazy as _

from .lecturer import Lecturer
from .faculty import Faculty


class Subject(models.Model):
    faculty = models.ManyToManyField(
        Faculty,
        related_name='faculty',
        verbose_name=_("Faculties"))
    lecturers = models.ManyToManyField(
        Lecturer,
        related_name="subject",
        verbose_name=_("Lecturers"))

    title = models.CharField(max_length=100, verbose_name=_("Title"))
    short_description = models.TextField(verbose_name=_("Short Description"))
    syllabus = models.FileField(upload_to='syllabus', verbose_name=_("Syllabus"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")
