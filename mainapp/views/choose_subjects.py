from django.shortcuts import render, redirect
from ..forms.forms import StudentSubjectForm


def choose_subjects(request):
    if request.method == 'POST':
        form = StudentSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = StudentSubjectForm()
    return render(request, 'register_subjects.html', {'form': form})
