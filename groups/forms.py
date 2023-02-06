from django import forms
from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'start_date',
            'description'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'start_date',
            'description'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }