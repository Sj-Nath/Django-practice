from django.urls import include, re_path
from class_based_view import views

app_name='class_based_view'
urlpatterns = [
    re_path(r'$^', views.CBView.as_view(), name='index'),
]