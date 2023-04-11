from django.urls import include, re_path
from graphs_app import views


urlpatterns = [
    re_path('home', views.home, name='home'),
]