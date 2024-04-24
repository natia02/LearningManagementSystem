from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('selection/', views.subject_selection, name='subject_selection')
]
