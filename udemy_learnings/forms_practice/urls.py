from django.urls import include, re_path
from forms_practice import views


urlpatterns = [
    re_path('preference', views.preference, name='preference'),
    re_path('signup', views.signup, name='signup'),
    re_path('welcome', views.welcome, name='welcome'),
    
    
]