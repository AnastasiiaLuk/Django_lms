from django.urls import path

from .views import ListGroupVIew
from .views import CreateGroupView
from .views import UpdateGroupView
from .views import DetailGroupView
from .views import DeleteGroupView

app_name = 'groups'

urlpatterns = [
    path('', ListGroupVIew.as_view(), name='list'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailGroupView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),
]