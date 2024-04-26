from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('selection/', views.subject_selection, name='subject_selection'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('view_submitted_assignments/<int:submitted_assignment_id>', views.view_submitted_assignments, name='view_submitted_assignments'),
]
