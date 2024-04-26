from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name=_('First Name'))
    surname = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    submitted_assignments = models.ManyToManyField(to='SubmittedAssignment',
                                                   blank=True,
                                                   related_name='submitted_assignments',
                                                   verbose_name=_('Submitted Assignments'))

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')