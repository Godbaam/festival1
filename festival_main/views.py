from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def line_up(request):
    return render(request, 'line_up.html')

def line_up_en(request):    
    return render(request, 'line_up_en.html')

def line_up_art(request):    
    return render(request, 'line_up_art.html')

def beatz(request):    
    return render(request, 'beatz.html')

def contact(request):    
    return render(request, 'contact.html')
