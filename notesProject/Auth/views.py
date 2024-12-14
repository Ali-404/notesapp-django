from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import get_user_by_email,check_password,create_user
# Create your views here.


def Login(request: HttpRequest):
    pass 


def LoginPage(request: HttpRequest):
    if (request.method == "POST"):
        Login(request)
        
    return render(request, "Login.html")




def Register(request:HttpRequest):
    error = ""
    
    
    # validate email
    email = request.POST.get("register_email")
    
    if (get_user_by_email(email)):
        error = "Email already taken! "
        return error    
    
    
    
    password = request.POST.get("register_password")
    
    valid,msg = check_password(password)
    if (not valid):
        error = msg
        return error
    
    
    password_conferm = request.POST.get("register_password_confirm")
    
    if (password != password_conferm):
        error  = "Passwords do not match! "
        return error
    
    
    # create user
    user = create_user(email, password)
    
    if (user):
        error = ""
    else:
        error = "There is an error !"
    
    return error


def RegisterPage(request:HttpRequest):
    
    
    error = ""
    if (request.method == "POST"):
        error = Register(request)
        if (not error or error == ""):
            return redirect("Login")
    return render(request, "Register.html", {
        "error": error
    })



