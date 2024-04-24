from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    lecturers = models.ManyToManyField(
        to="mainapp.Lecturer",
        related_name="subjects",
        verbose_name=_("Lecturers"),
        blank=True)
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    short_description = models.TextField(verbose_name=_("Short Description"))
    syllabus = models.FileField(upload_to='syllabus', verbose_name=_("Syllabus"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")
