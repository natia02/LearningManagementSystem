from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def main_page_view(request):
    return render(request, 'mainapp/main_page.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            # Return an 'invalid login' error message.
            context = {'invalid_credentials': True}
            return render(request, 'mainapp/login.html', context)
    else:
        return render(request, 'mainapp/login.html')
