from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_view, name='main_page'),
    path('login/', views.login_view, name='login'),
]
