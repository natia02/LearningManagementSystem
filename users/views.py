from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
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
        return reverse_lazy('users:dashboard')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def student_dashboard(request):
    try:
        student = request.user.student
    except ObjectDoesNotExist:
        student = None
    return render(request, 'users/dashboard.html', {'student': student})
