from django import forms
from ..models.student import Student


class StudentSubjectForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['subjects']

    def clean_subjects(self):
        subjects = self.cleaned_data['subjects']
        if len(subjects) > 7:
            raise forms.ValidationError("You can choose up to seven subjects.")
        return subjects
