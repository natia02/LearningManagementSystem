from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/main_page.html')


