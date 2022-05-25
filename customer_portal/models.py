from unicodedata import name
from django.db import models
from django import forms
# packages in helping creating user form and login form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Model of our User and How they will register
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last Name")
    email = forms.EmailField(label = "Email")
    address = forms.CharField(label = "Address")
    # properties of this class
    class Meta:
        model = User
        fields = ("first_name","last_name" ,"email" ,"address")

    # overriding the saving method, setting hte username as email
    def save(self, commit= True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        user.address = self.cleaned_data["address"]
        if commit:
            user.save()
        return user

