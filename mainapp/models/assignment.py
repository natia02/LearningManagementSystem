from django.db import models
from django.utils.translation import gettext_lazy as _

from mainapp.models import Student


class Assignment(models.Model):
    lecturer = models.ForeignKey(to='Lecturer', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE, null=True)
    description = models.TextField(_('Description'))
    deadline_date = models.DateField(_('Deadline date'))
    deadline_time = models.TimeField(_('Deadline time'), null=True)

    def __str__(self):
        return f"{self.subject} - {self.lecturer} - {self.deadline_date} - {self.deadline_time}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        students = Student.objects.filter(lecturers=self.lecturer, subjects=self.subject)
        for student in students:
            student.assignments.add(self)

    class Meta:
        verbose_name = _('Assignment')
        verbose_name_plural = _('Assignments')
