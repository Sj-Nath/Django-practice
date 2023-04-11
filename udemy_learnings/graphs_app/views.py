from django.shortcuts import render
from django.http import HttpResponse
from graphs_app.models import Topic,Webpage,AccessRecord
# Create your views here.


def home(request):
    webpage_list = AccessRecord.objects.order_by('date')


    home_dict={
        'graph1':'Here is your Table',
        'access_records' : webpage_list
    }
    return render(request,'graphs_app/home.html',home_dict)