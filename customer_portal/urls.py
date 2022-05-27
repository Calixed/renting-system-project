from django.contrib.auth.views import LogoutView
from django.urls import path

from .forms import RegisterForm
from .views import CustomLoginView, HomePage, ProductPage, RegisterPage, CheckoutPage

urlpatterns = [
    # login page
    path('login/', CustomLoginView.as_view(), name="login"),

    # logout, redirecting the user to the home page
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),

    # register page
    path('register/', RegisterPage.as_view(), name="register"),

    # home page url
    path('', HomePage.as_view(), name="home"),

    # product view url
    path("product/<int:pk>", ProductPage.as_view(), name="product"),

    # checkout order
    path("checkout/<int:product_id>", CheckoutPage.as_view(), name="checkout")
]

