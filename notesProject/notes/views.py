from django.shortcuts import render,redirect,HttpResponse
from .models import getAllNotes,createNote,getNoteById,updateNote,deleteNote

def home(request: HttpResponse):
    if (not request.session.get("user")):
        return redirect("Login")
    
    notes = getAllNotes(request.session.get("user_id"))
    
    # check search
    search_query:str|None = request.GET.get("search_query")
    if (search_query):
        notes = [i for i in notes if search_query.lower() in i["title"].lower() or search_query.lower() in i["content"].lower() ]
    
    if (len(notes) <= 0):
        notes = None
    return render(request, "home.html",{"user": request.session.get("user"), "notes": notes, "search_query": search_query or ""})




def create(request):
    if (not request.session.get("user")):
        return redirect("Login")
    
    # post
    
    if (request.method == "POST"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        note = createNote(title, content, request.session.get("user_id"))
        if (note):
            return redirect("home")
        else:
            return redirect("home", {"messages": [{"type": "danger", "message": "There is an error !"}] })
        # return error
    
    return render(request, "create/create_edit.html", {"user": request.session.get("user")})

def edit(request, id):
    if (not request.session.get("user")):
        return redirect("Login")
    
    # post
    
    if (request.method == "POST"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        # update
        note = updateNote(id,title, content)
        if (note):
            return redirect("home")
        else:
            return redirect("home", {"messages": [{"type": "danger", "message": "There is an error !"}] })
    
    note = getNoteById(id)

    return render(request, "create/create_edit.html", {"user": request.session.get("user"), "note": {
        "id": id, "title": note["title"], "content": note["content"],"createdAt": note["createdAt"]
    }})
    
    
def delete(request, id):
    deleteNote(id)
    return redirect("home" )