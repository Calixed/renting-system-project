from dataclasses import fields
from django import forms
from unicodedata import name
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
# packages in helping creating user form and login form
from django.contrib.auth.forms import UserCreationForm

# importing the model Orders from the models.py
from customer_portal.models import Orders

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    # hints when the user is entered invalid email and password
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': (
            "Please enter the correct email and password"
            " Note that both fields may be case-sensitive."
        ),
    }

# Model of our User and How they will register
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label = "First name") # textfield
    last_name = forms.CharField(label = "Last Name") # textfield
    phone_number = forms.CharField(max_length=15) # textfield
    email = forms.EmailField(label = "Email") # emailfield
    address = forms.CharField(label = "Address") # textfield

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

    # overriding the saving method, setting ther username as 'email'
    # setting the data that is coming from the user-registration form to the model then to the database
    def save(self, commit= True):
        user = super(RegisterForm, self).save(commit=False)
        # "self.cleaned_data" is basically cleaning the data before settling it to the user.email attribute
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"] 
        user.username = self.cleaned_data["email"]
        user.address = self.cleaned_data["address"]
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user

# Model of the form in the Checkout page
class OrderForm(forms.ModelForm):
    # properties for the form of Renting a product
    class Meta:
        model = Orders
        fields = ['days'] # only one field. which is a textfield
    
    def save(self, commit = True): # saves the form, once the form is submitted
        return super().save(commit) 
