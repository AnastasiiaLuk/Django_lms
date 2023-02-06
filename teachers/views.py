from django.http import HttpResponseRedirect, HttpResponse
from teachers.models import Teacher
from django.db.models import Q
from django.middleware.csrf import get_token
from django.shortcuts import render
from webargs.fields import Str
from webargs.djangoparser import use_args
from teachers.forms import CreateTeacherForm, UpdateTeacherForm


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)
def get_teachers(request, args):
    teachers = Teacher.objects.all().order_by('birthday')

    if len(args) and (args.get('first_name') or args.get('last_name')):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(
        request=request,
        template_name='teachers/list.html',
        context={'title': 'List of Teachers', 'teachers': teachers}
    )


def detail_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'teachers/detail.html', {'title': 'Detail of teacher', 'teacher': teacher})


def create_teacher_view(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit"><br><br>
            <a href="/teachers/">Back to list</a>
        </form>
    '''

    return HttpResponse(html_form)


def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit"><br><br>
            <a href="/teachers/">Back to list</a>
        </form>
    '''
    return HttpResponse(html_form)