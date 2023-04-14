from django.urls import include, re_path
from forms_practice import views


urlpatterns = [
    re_path('preference', views.preference, name='preference'),
]