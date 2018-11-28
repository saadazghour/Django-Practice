from django.shortcuts import render
from .models import Product
from .forms import ProductCreateForm, RawCreateForm

# Create your views here.
def product_details_views(request):
    obj = Product.objects.get(id=10)
    # you can use this method for context or using dictionary immediately
        # context = {
        #         'object': obj
        # }

    # print(obj.price)
    return render(request, "products/products_details.html", {'object': obj})


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


# def product_create_views(request):
#     my_form = RawCreateForm()
#     if request.method == 'POST':
#         my_form = RawCreateForm(request.POST or None)
#         if my_form.is_valid():           # now Data is checked with requirement Fields and good
#             # print(my_form.cleaned_data)              verification Data in the Backend
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawCreateForm()

#     return render(request, "products/products_create.html", {'form':my_form})