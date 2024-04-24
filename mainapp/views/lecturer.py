from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from mainapp.models import Lecturer


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by('name')
    paginator = Paginator(lecturers, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'mainapp/lecturer_list.html', {'lecturers': page_obj})


def get_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, pk=lecturer_id)
    subjects = lecturer.subjects.all()
    faculties = set()
    for subject in subjects:
        faculties.update(subject.faculty.all())
    return render(request, 'mainapp/lecturer_detail.html',
                  {'lecturer': lecturer, 'faculties': faculties, 'subjects': subjects})
