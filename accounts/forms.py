from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import Profile

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        fields = [
            'first_name',
            'last_name'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'birthday',
            'city'
        ]

        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}