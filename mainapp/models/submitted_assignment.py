from django.db import models
from django.utils.translation import gettext_lazy as _


class SubmittedAssignment(models.Model):
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    assignment = models.ForeignKey(to='Assignment', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=f'assignments/%Y%m%d/{submission_date}/{student}')

    def __str__(self):
        return f'{self.student.name} submitted {self.assignment.description}'
