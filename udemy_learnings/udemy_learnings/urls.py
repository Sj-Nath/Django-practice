"""
URL configuration for udemy_learnings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, re_path
from graphs_app import views

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path("^$", views.home),
    re_path(r'^graphs_app/', include('graphs_app.urls'),name='graphs_app'),
    re_path(r'^forms_practice/', include('forms_practice.urls'),name='forms_practice'),
    re_path(r'^relative_url_template/', include('relative_url_template.urls'),name='relative_url_template'),
    re_path(r'^class_based_view/', include('class_based_view.urls'),name='class_based_view'),
    
]
