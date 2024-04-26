from django.db import models
from django.utils.translation import gettext_lazy as _
from mainapp.models.lecturer import Lecturer


class SubmittedAssignment(models.Model):
    student = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    assignment = models.ForeignKey(to='Assignment', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=f'assignments/')

    def __str__(self):
        return f'{self.student.name} submitted {self.assignment.description}'
