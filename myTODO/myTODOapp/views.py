from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>This is the home page</h1>")

def about(response):
    return HttpResponse("<h1>This is the about page</h1>")

