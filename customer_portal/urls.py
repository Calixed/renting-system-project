from django.contrib.auth.views import LogoutView
from django.urls import path

from .forms import RegisterForm
from .views import CustomLoginView, HomePage, ProductPage, RegisterPage, CheckoutPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),

    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),

    path('register/', RegisterPage.as_view(), name="register"),

    # home page url
    path('', HomePage.as_view(), name="home"),

    # product view url
    path("product/<int:pk>", ProductPage.as_view(), name="product"),

    # checkout order
    path("checkout/<int:pk>", CheckoutPage.as_view(), name="checkout")
]

