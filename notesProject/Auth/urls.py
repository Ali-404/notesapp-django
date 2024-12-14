from django.urls import path
from .views import LoginPage,RegisterPage
urlpatterns = [
    path("login/", LoginPage, name="Login"),
    path("register/", RegisterPage, name="Register")
]