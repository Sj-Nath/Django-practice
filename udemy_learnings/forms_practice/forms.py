from django import forms
from forms_practice.models import NewUsers
#Phone No. Validation custom checker
def check_phone(number):
    if (number.isdigit() ==False) | (len(number) != 10):
        raise forms.ValidationError('Please Enter A Valid Phone Number')



# Using forms
class GetPreference(forms.Form):
    name=forms.CharField(min_length=2,max_length=40)
    email=forms.EmailField()
    verify_email=forms.EmailField()
    phone=forms.CharField(validators=[check_phone])
    preference=forms.CharField(min_length=2,max_length=100,widget=forms.Textarea)

    def clean(self):
        all_cleaned_data=super().clean()
        email=all_cleaned_data['email']
        vmail=all_cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure the E-mails match')


#Using model for sign up

class NewUser(forms.ModelForm):
    class Meta():
        model=NewUsers
        fields= '__all__'