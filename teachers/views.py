from django.urls import reverse_lazy
from teachers.forms import CreateTeacherForm, UpdateTeacherForm, TeacherFilterForm
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        teachers = Teacher.objects.all().order_by('birthday')
        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teachers)
        return filter_form


class CreateTeacherView(CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')