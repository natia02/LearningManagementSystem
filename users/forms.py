from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from mainapp.models.submitted_assignment import SubmittedAssignment
from mainapp.models.assignment import Assignment
from mainapp.models.subject import Subject


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Email',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()


class SubjectSelectionForm(forms.Form):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple)


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject', 'description', 'deadline_date', 'deadline_time']


class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = SubmittedAssignment
        fields = ['file']
