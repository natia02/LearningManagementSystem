from django.urls import path

from .views import index
from .views import login_view

urlpatterns = [
    path('', index, name='main_page'),
]
