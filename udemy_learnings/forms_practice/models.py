from django.db import models

# Create your models here.


#for sign-up page

class NewUsers(models.Model):

    name=models.CharField(max_length=50)
    roll_No=models.CharField(max_length=30)
    contact_No=models.CharField(max_length=20)
    email_Id=models.EmailField(unique=True)
    