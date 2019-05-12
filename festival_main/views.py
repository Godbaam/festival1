from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def line_up(request):
    return render(request, 'line_up.html')
