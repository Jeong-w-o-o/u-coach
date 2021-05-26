from django.shortcuts import render, redirect
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')