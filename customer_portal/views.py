from msilib.schema import ListView
from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import (CreateView, FormView,)
from django.views.generic.list import ListView

from .forms import RegisterForm, OrderForm , CustomLoginForm
from .models import Product, Orders

# displaying the custom login page
class CustomLoginView(LoginView):
    template_name = 'customer_portal/login.html'  # location of the template
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')  # return the user to the task page

class RegisterPage(FormView):
    template_name = 'customer_portal/register.html'  # location of the template
    form_class = RegisterForm  # for building the custom user-registeration form
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):  # once the post request is submitted, form validation appplies
        user = form.save()  # saves the form when the form is submitted
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # to block authenticated user to register again 
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)

class HomePageView(TemplateView):
    template_name = "customer_portal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['products'] = products
        return context

# Home page
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'  # overriding
    # name of the template on where to render
    template_name = "customer_portal/product_list.html"

# Single View Product
class ProductPage(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "customer_portal/product.html"

# Ordering the Product
# basically, had my template checkout it with the product.id 
class CheckoutPage(CreateView):
    model = Orders
    template_name = 'customer_portal/checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('home')  # redirect user to the home page

    def form_valid(self, form):
        self.product_id = self.kwargs['pk']  # grab the productid passed from urls
        product = Product.objects.get(id=self.product_id)  # query the product
        product_rent = float(form.instance.days) * float(
            product.product_price)  # convert the decimal.Decimal into float
        form.instance.user = self.request.user  # assigned the user, with the current logged in user
        form.instance.product_rented = product  # assigned the queried product, to the product_rented
        form.instance.rent = product_rent  # assigned computed rent
        return super(CheckoutPage, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.product_id = self.kwargs['pk']  # grab the productid passed from urls
        product = Product.objects.get(id=self.product_id)
        context['product'] = product
        return context
