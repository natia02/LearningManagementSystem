from django.urls import path
from mainapp.views.faculty import get_faculties, get_faculty
from mainapp.views.lecturer import get_lecturer, get_lecturers
from mainapp.views.subject import get_subject, get_subjects


urlpatterns = [
    path('', get_faculties, name='faculties'),
    path('faculty/<int:faculty_id>/', get_faculty, name='faculty'),
    path('lecturer/<int:lecturer_id>', get_lecturer, name='lecturer'),
    path('lecturers/', get_lecturers, name='lecturers'),
    path('subjects/', get_subjects, name='subjects'),
    path('subject/<int:subject_id>', get_subject, name='subject')
]
