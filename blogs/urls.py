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
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)


# app_name = "blogs"    # still working without using app_name attribute

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('<int:my_id>', ArticleDetailView.as_view(), name="article_detail"),  # or using <int:pk> (By default id=pk)
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id_update>/update/', ArticleUpdateView.as_view(), name="article_update")
]