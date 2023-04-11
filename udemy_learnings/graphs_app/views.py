from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    home_dict={
        'graph1':'Here is your Graph'
    }
    return render(request,'graphs_app/home.html',home_dict)