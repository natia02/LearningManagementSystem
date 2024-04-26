from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from .forms import LoginUserForm, AssignmentForm, AssignmentSubmissionForm
from mainapp.models.student import Student
from mainapp.models.subject import Subject
from mainapp.models.assignment import Assignment
from mainapp.models.submitted_assignment import SubmittedAssignment
from .forms import SubjectSelectionForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/login.html'
    extra_context = {'title': 'Login'}

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:dashboard')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('faculties'))


@login_required
def dashboard(request):
    user = request.user

    if hasattr(user, 'student'):
        student = user.student
        subjects = student.subjects.all()
        assignments = student.assignments.all()
        return render(request, 'users/dashboard.html', {'student': student,
                                                        'subjects': subjects,
                                                        'assignments': assignments})

    elif hasattr(user, 'lecturer'):
        lecturer = user.lecturer
        assignments = Assignment.objects.filter(lecturer=lecturer)
        submitted_assignments = SubmittedAssignment.objects.filter(lecturer=lecturer)
        return render(request, 'users/dashboard.html', {'lecturer': lecturer,
                                                        'assignments': assignments,
                                                        'submitted_assignments': submitted_assignments})
    else:
        return HttpResponseRedirect(reverse('faculties'))


@login_required
def subject_selection(request):
    user = request.user
    if hasattr(user, 'student'):
        student = user.student
        faculty = student.faculty
    else:
        return HttpResponseRedirect(reverse('faculties'))

    if request.method == 'POST':
        selected_subject_ids = request.POST.getlist('subjects')
        selected_subjects = Subject.objects.filter(id__in=selected_subject_ids, faculty=faculty)
        if len(selected_subjects) > 7:
            error_message = "You can select a maximum of 7 subjects."
            return render(request, 'users/subject_selection.html', {'error_message': error_message})

        student.subjects.clear()
        student.subjects.add(*selected_subjects)
        return HttpResponseRedirect(reverse('users:dashboard'))

    else:
        subjects = faculty.subjects.all()
        return render(request, 'users/subject_selection.html', {'subjects': subjects})


@login_required
def add_assignment(request):
    user = request.user

    if hasattr(user, 'lecturer'):
        if request.method == 'GET':
            form = AssignmentForm()
            return render(request, 'users/add_assignment.html', {'form': form})
        if request.method == 'POST':
            form = AssignmentForm(request.POST)
            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.lecturer = request.user.lecturer
                assignment.save()
                return redirect('users:dashboard')
    else:
        return HttpResponseRedirect(reverse('faculties'))


@login_required
def submit_assignment(request, assignment_id):
    user = request.user

    if hasattr(user, 'student'):
        assignment = Assignment.objects.get(id=assignment_id)
        student = user.student
        lecturer = assignment.lecturer
        if request.method == 'POST':
            form = AssignmentSubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                submission = form.save(commit=False)
                submission.assignment = assignment
                submission.student = student
                submission.lecturer = lecturer
                submission.save()

                student.assignments.remove(assignment)
                return redirect('users:dashboard')
            else:
                print(form.errors)
        else:
            form = AssignmentSubmissionForm()
        return render(request, 'users/submit_assignment.html', {'form': form, 'assignment': assignment})
    else:
        return HttpResponseRedirect(reverse('faculties'))


@login_required
def view_submitted_assignments(request, submitted_assignment_id):
    user = request.user

    if hasattr(user, 'lecturer'):
        assignment = SubmittedAssignment.objects.get(id=submitted_assignment_id)
        return render(request, 'users/submitted_assignment_detail.html', {'assignment': assignment})
    else:
        return HttpResponseRedirect(reverse('faculties'))
