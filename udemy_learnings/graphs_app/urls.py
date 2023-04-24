from django.urls import include, re_path
from graphs_app import views

app_name='graphs_app'
urlpatterns = [
    re_path('home', views.home, name='home'),
]