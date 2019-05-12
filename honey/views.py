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

def lost(request):
    return render(request, 'lost.html')

def drink(request):
    return render(request, 'drink.html') 

def map(request):
    return render(request, 'map.html')  

def store(request):
    return render(request, 'store.html')  

def toilet(request): 
    return render(request, 'toilet.html')   