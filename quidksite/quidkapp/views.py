from curses.ascii import HT
from django.shortcuts import render

from django.http import HttpResponse
 
# Create your views here.
def home (request):
    return render(request, 'base/home.html')

def sub (request):
    return render(request, 'base/linkemb.html')
