from django import forms
from django_filters import FilterSet

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'city',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()


    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        new_value = ''
        symbols = ['+', '-', '(', ')']
        for i in value:
            if i.isnumeric() or i in symbols:
                new_value += i
        return new_value