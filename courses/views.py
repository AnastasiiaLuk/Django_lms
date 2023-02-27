from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from courses.forms import CreateCourseForm, UpdateCourseForm, CourseFilterForm
from courses.models import Course


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_queryset(self):
        courses = Course.objects.all().order_by('course_name')
        filter_form = CourseFilterForm(data=self.request.GET, queryset=courses)
        return filter_form


class CreateCourseView(CreateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class UpdateCourserView(UpdateView):
    model = Course
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class DetailCourseView(DetailView):
    model = Course
    template_name = 'courses/detail.html'


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses:list')