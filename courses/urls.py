from django.urls import path

from .views import ListCourseView
from .views import CreateCourseView
from .views import UpdateCourserView
from .views import DetailCourseView
from .views import DeleteCourseView

app_name = 'courses'

urlpatterns = [
    path('', ListCourseView.as_view(), name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateCourserView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),

]