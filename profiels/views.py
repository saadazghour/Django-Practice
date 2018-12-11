from django.shortcuts import render
from .models import Student
from django.views import View


# Create your views here.
class StudentListView(View):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        # my_object = Student.objects.all()
        return render(request, self.template_name, {})

    # when handled form using post method
    # def post(request, *args, **kwargs):
    #     my_object = Student.objects.all()
    #     return render(request, "about.html", {})



def student_list_views(request, *args, **kwargs):
    # print(request.method)
    my_object = Student.objects.all()
    return render(request, "about.html", {})