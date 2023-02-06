from django.urls import path

from .views import get_groups, create_group_view, update_group, detail_group

app_name = 'groups'

urlpatterns = [
    path('groups/', get_groups),
    path('groups/create/', create_group_view),
    path('groups/update/<int:pk>/', update_group),
    path('groups/detail/<int:pk>/', detail_group),
]