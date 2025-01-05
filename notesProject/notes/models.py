from mongo import db 
from datetime import datetime
from bson.objectid import ObjectId
# Create your models here.

def getAllNotes(user_id):
   returnValue = []
   data = db["notes"].find({"user_id":user_id }).to_list()
   for note in data:
      returnValue.append({
         "id": str(note["_id"]),
         "title": note["title"],
         "content": note["content"],
         "createdAt": note["createdAt"],
      })
  
   return returnValue 
def createNote(title, content, user_id):
   return db["notes"].insert_one({"title": title, "content": content, "createdAt": datetime.now(), "user_id": user_id})


def getNoteById(id):
   return db["notes"].find_one({"_id": ObjectId(id)})
   
   
def updateNote(id,title, content ):
   return db["notes"].update_one({"_id": ObjectId(id)}, {"$set": {"title":title, "content": content, "createdAt": datetime.now()}})

def deleteNote(id):
   return db["notes"].delete_one({"_id": ObjectId(id)})