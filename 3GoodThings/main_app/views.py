from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>3GT - 3 Good Things</h1>')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')
