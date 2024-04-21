from django.db import models
from django.utils.translation import gettext_lazy as _

from mainapp.models.lecturer import Lecturer


class Subject(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, verbose_name=_("Lecturer"))
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    short_description = models.TextField(verbose_name=_("Short Description"))
    syllabus = models.FileField(upload_to='syllabus', verbose_name=_("Syllabus"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")
