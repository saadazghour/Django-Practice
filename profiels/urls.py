"""Training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    student_list_views,
    StudentListView,
    FirstStudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    StudentView
)

app_name = 'profiels'

urlpatterns = [
    path('', StudentView.as_view(template_name="contact.html")),
    path('student_list/', StudentListView.as_view(), name="student_list"),
    path('first_student/', FirstStudentListView.as_view(), name="first_student"),
    path('<int:id>', StudentView.as_view(), name="list_detail"),
    path('create/', StudentCreateView.as_view(), name="student_create"),
    path('<int:id>/update/', StudentUpdateView.as_view(), name="student_update"),
    path('<int:id>/delete/', StudentDeleteView.as_view(), name="student_delete")
]