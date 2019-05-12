from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .form import Flea_marketPost
from .models import Flea_market


# Create your views here.

def flea_main(request):
    flea_markets = Flea_market.objects
    return render(request, 'flea_main.html', {'flea_markets' : flea_markets})

def flea_detail(request, flea_market_id):
    flea_detail = get_object_or_404(Flea_market, pk=flea_market_id)
    return render(request, 'flea_detail.html', {'flea_market': flea_detail})

def flea_new(request):
    return render(request, 'flea_new.html')

def flea_create(request):
    return render(request, 'flea_new.html')

def flea_marketpost(request):
    if request.method == 'POST': 

        form = Flea_marketPost(request.POST,request.FILES)
        if form.is_valid():
            flea_market = form.save(commit=False)
            flea_market.pub_date = timezone.now()
            flea_market.save()
            return redirect('home')

    else:
        form = Flea_marketPost()
        return render(request, 'flea_new.html', {'form' : form})
