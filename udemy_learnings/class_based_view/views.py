from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
# Create your views here.

class CBView(TemplateView):

    template_name='class_based_view/index.html'
