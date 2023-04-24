from django.shortcuts import render


app_name= 'relative_url_template'

def index(request):
    return render(request,'relative_url_template/index.html')

def other(request):
    return render(request,'relative_url_template/other.html')

def relative(request):
    return render(request,'relative_url_template/relative.html')