from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicity
from .form import Publicity_Post
from django.utils import timezone

# Create your views here.

def publicity_main(request) :
    publicity = Publicity.objects
    return render(request, 'publicity_main.html', {'publicity': publicity})

def publicity_detail(request, publicity_id) :
    publicity_detail = get_object_or_404(Publicity, pk = publicity_id)
    return render(request, 'publicity_detail.html', {'publicity_detail': publicity_detail})

def publicity_new(request) :
    return render(request, 'publicity_new.html')

def publicity_post(request):
    if request.method == 'POST': 
        form = Publicity_Post(request.POST,request.FILES)
        if form.is_valid():
            publicity = form.save(commit=False)
            publicity.pub_date = timezone.now()
            publicity.save()
            return redirect('publicity_main')

    else:
        form = Publicity_Post()
        return render(request, 'publicity_new.html', {'form' : form})
