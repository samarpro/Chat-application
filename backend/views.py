from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import GroupDB,ChatDB

# Create your views here.

def home_loader(req,GroupName):
    TempQuery = GroupDB.objects.filter(Name=GroupName)
    ObjChat = None
    if TempQuery.exists():
        ObjChat = ChatDB.objects.filter(Group = TempQuery.first())
    else:
        print("Else part GroupName: ", GroupName)
        GroupDB(Name=GroupName)
    return render(req,'backend/index.html',{'GN':GroupName,'chats':ObjChat})