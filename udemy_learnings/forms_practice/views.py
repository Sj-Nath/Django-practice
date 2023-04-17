from django.shortcuts import render

from forms_practice.forms import NewUser,GetPreference
# Create your views here.

def welcome(request):
    return render(request,'forms_practice/welcome.html')
def preference(request):
    form=GetPreference()
    if request.method =='POST':
        form=GetPreference(request.POST)
        if form.is_valid():
            print('Validated')
            print(form.cleaned_data['email'])
    return render(request,'forms_practice/forms_page.html',{'form':form})

def signup(request):
    signup=NewUser()
    if request.method == 'POST':
        signup = NewUser(request.POST)
        if signup.is_valid():
            signup.save(commit=True)
            return welcome(request)
        else:
            print('Error form invalid ')
    return render(request,'forms_practice/signup.html',{'signup':signup})