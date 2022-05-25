from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy 
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView   
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


# from models
from customer_portal.models import RegisterForm

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

class CustomLoginView(LoginView):
    template_name = 'customer_portal/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True #redirected authenticated user
    
    def get_success_url(self):
        return reverse_lazy('home') # return the user to the task page


class RegisterPage(FormView):
    template_name = 'customer_portal/register.html'
    form_class = RegisterForm # for building custom use registeration form
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form): # once the post request is submitted, form validation appplies 
        user = form.save() # saves the form when the form is submitted
        if user is not None: # checking if the form is valid
            login(self.request, user)
        return super(RegisterPage,   self).form_valid(form)

    # to block authenticated user to register again 
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)

# Home page
class HomePage(View):
    def get(self, request):
        return HttpResponse('Hello World')


