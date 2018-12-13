from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Student


# Create your views here.
class StudentView(View):                  # Base Class View = View
    template_name = "profiels/student_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        # my_object = Student.objects.all()
        context = {}
        if id is not None:
            # print(id)
            my_object = get_object_or_404(Student, id=id)
            context['object_detaill'] = my_object
        return render(request, self.template_name, context)


class StudentListView(View):
    template_name = "profiels/student_list.html"
    queryset = Student.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'list_student': self.get_queryset()}
        return render(request, self.template_name, context)



class FirstStudentListView(StudentListView):
    queryset = Student.objects.filter(id=2)



# class StudentListView(View):
#     template_name = "about.html"
#     def get(self, request, *args, **kwargs):
#         # my_object = Student.objects.all()
#         return render(request, self.template_name, {})

    # when handled form using post method
    # def post(request, *args, **kwargs):
    #     my_object = Student.objects.all()
    #     return render(request, "about.html", {})



def student_list_views(request, *args, **kwargs):
    # print(request.method)
    my_object = Student.objects.all()
    return render(request, "about.html", {})