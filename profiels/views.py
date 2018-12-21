from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Student
from .forms import StudentCreateForm


# Create your views here.
class StudentObjectMixin(object):
    model = Student
    url_lookup = 'id'

    def get_object(self):
        id_ = self.kwargs.get(self.url_lookup)
        my_object = None
        if id_ is not None:
            my_object = get_object_or_404(self.model, id=id_)
        return my_object



class StudentView(StudentObjectMixin, View):                  # Base Class View = View
    template_name = "profiels/student_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        # my_object = Student.objects.all()

        context = {
            "object_detaill": self.get_object()
        }

        # if id is not None:
        #     # print(id)
        #     my_object = get_object_or_404(Student, id=id)
        #     context['object_detaill'] = my_object
   
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


class StudentCreateView(View):
    template_name = "profiels/student_create.html"
    form = StudentCreateForm()

    # initial_data = {
    #     'first_name':'SAzghour',
    #     'age':88
    # }

    # retrieve_student_data = Student.objects.get(id=1)

    # GET Methode
    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return render(request, self.template_name, context)


    # POST Methode
    def post(self, request, *args, **kwargs):
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # form = StudentCreateForm()
            return redirect('/')
        context = {'form': form}
        return render(request, self.template_name, context)



class StudentUpdateView(StudentObjectMixin, View):
    template_name = "profiels/student_update.html"

    # def get_object(self):
    #     id_ = self.kwargs.get("id_update")
    #     my_object = None
    #     if id_ is not None:
    #         my_object = get_object_or_404(Student, id=id_)
    #     return my_object


    def get(self, request, id=None, *args, **kwargs):
        # GET Method
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = StudentCreateForm(instance=obj)
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)


    def post(self, request, id=None, *args, **kwargs):
        # POST Method
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = StudentCreateForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('/profiels/student_list/')
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)



class StudentDeleteView(StudentObjectMixin, View):
    template_name = "profiels/student_delete.html"

    # def get_object(self):
    #     id_ = self.kwargs.get('id_delete')
    #     my_obj = None
    #     if id is not None:
    #         my_obj = get_object_or_404(Student, id=id_)
    #     return my_obj


    def get(self, request, id=None, *args, **kwargs):
        # GET Method
        obj = self.get_object()
        context = {}
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
 

    def post(self, request, id=None, *args, **kwargs ):
        # POST Method
        obj = self.get_object()
        context = {}
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/profiels/student_list/')
        return(request, self.template_name, context)



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