from django.urls import path

from .views import AccountRegisterView
from .views import AccountLoginview
from .views import AccountLogoutView



app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginview.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
]