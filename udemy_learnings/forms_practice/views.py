from django.shortcuts import render
from . import forms
# Create your views here.

def preference(request):
    form=forms.GetPreference()

    if form.is_valid():
        form=forms.GetPreference(request.POST)
        print('Validated')
        print(form.cleaned_data['email'])
    return render(request,'forms_practice/forms_page.html',{'form':form})