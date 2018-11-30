from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductCreateForm, RawCreateForm

# Create your views here.
def render_initial_data(request):

    initial_data = {
        'title':'this is awesome title',
        'descriptions':'this product is the best',
        'summary':'this is awesome summary',
        'email':'saad.azghour@gmail.com'
    }

    my_object = Product.objects.get(id=49)      # render object from Database

    # usually when editing something in backend with instance attribute
    # not initialise data with initial attr (initial_data == Dictionnary)
    form = ProductCreateForm(request.POST or None, initial=initial_data, instance=my_object)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    return render(request, "products/products_create.html", {'form':form})


def product_details_views(request):
    obj = Product.objects.get(id=49)
    # you can use this method for context or using dictionary immediately
        # context = {
        #         'object': obj
        # }

    # print(obj.price)
    return render(request, "products/products_details.html", {'object': obj})

# dynamic URL Routing
def dynamic_views(request, my_id):
    # my_object = Product.objects.get(id=my_id)
    my_object = get_object_or_404(Product, id=my_id)  # I prefer this method because easy

    # try:
    #     my_object = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    return render(request, "products/products_details.html", {'object': my_object})



def product_create_views(request):
    form = ProductCreateForm()
    if request.method == 'POST':

    #     my_new_title = request.POST.get('title')
    #         # Product.objects.create(title=my_new_title)    save data in Database
    #     print(my_new_title)
    #     print(request.POST)

        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductCreateForm()            
    return render(request, "products/products_create.html", {'form':form})


def procuct_delete_views(request, obj_id):
    my_object = get_object_or_404(Product, id=obj_id)
    if request.method == 'POST':
        # confirm delete for POST request
        my_object.delete()
        return redirect('../../')
    return render(request, "products/products_delete.html", {'object':my_object})


# def product_create_views(request):
#     my_form = RawCreateForm()
#     if request.method == 'POST':
#         my_form = RawCreateForm(request.POST or None)
#         if my_form.is_valid():           # now Data is checked with requirement Fields and good
#             # print(my_form.cleaned_data)              verification Data in the Backend
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawCreateForm()

#     return render(request, "products/products_create.html", {'form':my_form})