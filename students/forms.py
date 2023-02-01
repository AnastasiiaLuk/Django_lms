from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name_1(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()