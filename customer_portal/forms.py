from dataclasses import fields
from django import forms
from unicodedata import name
from django.contrib.auth.models import User
# packages in helping creating user form and login form
from django.contrib.auth.forms import UserCreationForm

from customer_portal.models import Orders


# Model of our User and How they will register
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last Name")
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Address")

    # properties of this class
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "address", "phone_number")
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control '}),
            "last_name": forms.TextInput(attrs={'class': 'form-control '}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "address": forms.TextInput(attrs={'class': 'form-control'}),
            "phone_number": forms.TextInput(attrs={'class': 'form-control '}),
        }

    # overriding the saving method, setting hte username as email
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        user.address = self.cleaned_data["address"]
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['days']

    def save(self, commit=True):
        return super().save(commit)
