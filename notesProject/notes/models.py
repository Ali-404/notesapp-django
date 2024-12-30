from mongo import db 
# Create your models here.

def getAllNotes():
   return db["notes"].find()