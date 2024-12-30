from django.shortcuts import render,redirect
from .models import getAllNotes 

def home(request):
    if (not request.session.get("user")):
        return redirect("Login")
    
    notes = getAllNotes()
    return render(request, "home.html",{"user": request.session.get("user"), "notes": notes})