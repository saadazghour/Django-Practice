from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_views(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse('<h1>Hello Python & Django</h1>')
    
    context = {
        'title':'my best title',
        'text': 'this is awesome text',
        'number': 123456,
        'my_list':[123, 333, 444, 577, 58, "SAzghour"],
        'html_text':'<h2>Hello Django</h2>'
    }
    return render(request, "home.html", context)


def contact_views(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_views(request, *args, **kwargs):
    return render(request, "about.html", {})


def social_views(request, *args, **kwargs):
    return render(request, "social.html", {})