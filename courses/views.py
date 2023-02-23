from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from courses.forms import CreateCourseForm, UpdateCourseForm, CourseFilterForm
from courses.models import Course



def get_courses(request):
    courses = Course.objects.all().order_by('course_name')
    filter_form = CourseFilterForm(data=request.GET, queryset=courses)
    return render(
        request=request,
        template_name='courses/list.html',
        context={'filter_form': filter_form}
    )


def detail_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/detail.html', {'course': course})


def create_course_view(request):
    if request.method == 'GET':
        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/create.html', {'form': form})


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = UpdateCourseForm(instance=course)
    elif request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/update.html', {'form': form, 'course': course})


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/delete.html', {'course': course})