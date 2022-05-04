from django.shortcuts import render
from django.http import HttpResponse
from . models import Item, ToDoList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse(f"<h1>{ls.name}</h1><br><p>{item.text}</p>")

