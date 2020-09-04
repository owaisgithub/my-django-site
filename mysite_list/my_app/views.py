import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')  #request post return a python get dict
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
