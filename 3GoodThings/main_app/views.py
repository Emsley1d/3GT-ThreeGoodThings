from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

days = {
    
}

def home(request):
    return HttpResponse('<h1>3GT - 3 Good Things</h1>')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def profile(request):
    return render(request, 'profile.html')

def stats(request):
    return render(request, 'stats.html')

def days_index(request):
    return render(request, 'days/index.html', { 'days': days})

