from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm
from mainapp.models.student import Student


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main_page')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_page'))


@login_required
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
        subjects = student.subjects.all()
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('faculties'))
    return render(request, 'users/dashboard.html', {'student': student, 'subjects': subjects})


@login_required
def subject_selection(request):
    try:
        student = Student.objects.get(user=request.user)
        faculty = student.faculty
    except ObjectDoesNotExist:
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
