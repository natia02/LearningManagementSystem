from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from mainapp.models import Faculty


def get_faculties(request):
    faculties = Faculty.objects.all().order_by('name')
    paginator = Paginator(faculties, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'mainapp/main_page.html', {'faculties': page_obj})


def get_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    subjects = faculty.subject.all()
    lecturers = faculty.lecturers.all()
    return render(request, 'mainapp/faculty_detail.html',
                  {'faculty': faculty, 'subjects': subjects, 'lecturers': lecturers})
