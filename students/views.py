from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, ListView
from django.urls import reverse, reverse_lazy

from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'

def get_queryset(self):
    students = Student.objects.all().order_by('birthday').select_related('group')
    filter_form = StudentFilterForm(data=self.request.GET, queryset=students)
    return filter_form


def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'

def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})

def delete_student(request, pk):
    st = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/delete.html', {'student': st})