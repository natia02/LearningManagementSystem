from django.db import models
from django.utils.translation import gettext_lazy as _

from mainapp.models.subject import Subject


class Faculty(models.Model):
    subject = models.ManyToManyField(Subject, related_name='faculty', verbose_name=_("Subjects"))
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Faculty")
        verbose_name_plural = _("Faculties")