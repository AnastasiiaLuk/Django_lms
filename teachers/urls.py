from django.urls import path

from .views import get_teachers, create_teacher_view, update_teacher, detail_teacher

app_name = 'teachers'

urlpatterns = [
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher_view),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/detail/<int:pk>/', detail_teacher)
]