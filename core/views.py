from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


# def view_with_param(request, value):
#     return HttpResponse(f'With param: "{value}"')
#
#
# def view_without_param(request):
#     return HttpResponse('Without param')


def index(request):
    return render(request, 'index.html')

class CustomUpdateBaseView:
    model = None
    form_class = None
    success_url = None
    template_name = None


    @classmethod
    def update_student(self, request, pk):
        student = get_object_or_404(self.model, pk=pk)

        if request.method == 'GET':
            form = self.form_class(instance=student)
        elif request.method == 'POST':
            form = self.form_class(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(self.success_url))
        return render(request, self.template_name, {'form': form})