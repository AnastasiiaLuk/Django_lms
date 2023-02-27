from django.urls import path

from .views import get_courses
from .views import create_course_view
from .views import update_course
from .views import detail_course
from .views import delete_course

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course_view, name='create'),
    path('update/<int:pk>/', update_course, name='update'),
    path('detail/<int:pk>/', detail_course, name='detail'),
    path('delete/<int:pk>/', delete_course, name='delete'),

]