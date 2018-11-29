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
from django.contrib import admin
from django.urls import path
from pages.views import home_views, contact_views, about_views, social_views
from products.views import (
    product_details_views,
    product_create_views,
    render_initial_data,
    dynamic_views
)

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', home_views, name='home'),
    path('contact/', contact_views, name='contact'),
    path('about/', about_views, name='about'),
    path('social/', social_views, name='social'),
    path('product/', product_details_views, name='details'),
    path('dynamic/<int:my_id>/', dynamic_views),
    path('create/', product_create_views),
    path('initial/', render_initial_data)
]