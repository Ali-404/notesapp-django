from django.shortcuts import render

# Create your views here.


def LoginPage(request):
    return render(request, "Login.html")



def RegisterPage(request):
    return render(request, "Register.html")