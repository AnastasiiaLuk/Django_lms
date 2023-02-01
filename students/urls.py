from django.urls import path

from .views import get_students
from .views import create_student_view

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),                       # students:list      group:list
    path('create/', create_student_view, name='create'),       # students/create/
]