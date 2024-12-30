from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.hashers import check_password as verify_pass
from .models import get_user_by_email,check_password,create_user,serialize

def Login(request: HttpRequest):
    
   
    if request.method == "POST":
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        user = get_user_by_email(email)
        if not user:
            return "User not found"
        if not verify_pass(password, user["password"]):
           return "Password incorrect !"

        request.session["user"] = serialize(user)
        request.session["logged_in"] = True
        return ""

def LoginPage(request: HttpRequest):
    
    if (request.session.get("logged_in")):
       return redirect("home")
    
    error = ""
    if (request.method == "POST"):
        error = Login(request)
        if (not error or error == ""):
            return redirect("home")
    return render(request, "Login.html", {
        "error": error
    })




def Register(request:HttpRequest):
    
    
    # validate email
    email = request.POST.get("register_email")
    
    if (get_user_by_email(email)):
        return "Email already taken! "    
    
    
    
    password = request.POST.get("register_password")
    
    valid,msg = check_password(password)
    if (not valid):
        return msg
    
    
    password_conferm = request.POST.get("register_password_confirm")
    
    if (password != password_conferm):
        return "Passwords do not match! "
    
    
    # create user
    user = create_user(email, password)
    
    if (user):
        return ""
    else:
        return "There is an error !"
    


def RegisterPage(request:HttpRequest):
    
    if (request.session.get("logged_in")):
       return redirect("base")
    error = ""
    if (request.method == "POST"):
        error = Register(request)
        if (not error or error == ""):
            return redirect("Login")
    return render(request, "Register.html", {
        "error": error
    })




def LogoutPage(request:HttpRequest):
    request.session.clear()
    return redirect("Login")