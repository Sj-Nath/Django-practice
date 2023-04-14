from django import forms



class GetPreference(forms.Form):
    name=forms.CharField(min_length=2,max_length=40)
    email=forms.EmailField()
    phone=forms.CharField()
    preference=forms.CharField(min_length=2,max_length=100,widget=forms.Textarea)