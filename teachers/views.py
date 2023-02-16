from django.http import HttpResponseRedirect, HttpResponse
from teachers.models import Teacher
from django.db.models import Q
# from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from webargs.fields import Str
from webargs.djangoparser import use_args
from teachers.forms import CreateTeacherForm, UpdateTeacherForm, TeacherFilterForm
from django.urls import reverse



def get_teachers(request):
    teachers = Teacher.objects.all().order_by('birthday')
    filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)
    return render(
        request=request,
        template_name='teachers/list.html',
        context={'filter_form': filter_form}
    )


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'teacher': teacher})


def create_teacher_view(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/create.html', {'form': form})


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/update.html', {'form': form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/delete.html', {'teacher': teacher})