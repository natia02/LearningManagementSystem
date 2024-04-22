from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm
from .forms import RegisterUserForm


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


def register_user(request):
    form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
