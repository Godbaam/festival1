from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from .models import Lostfound
from .form import LostfoundPost
from django.utils import timezone
from django.core.paginator import Paginator


def lostfound_main(request):
    lostfounds=Lostfound.objects.order_by('-pub_date')
    lostfound_list=Lostfound.objects.all().order_by('-pub_date')
    paginator=Paginator(lostfound_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'lostfound_main.html',{'lostfounds':lostfounds, 'posts':posts})

def lostfound_detail(request,lostfound_id):
    lostfound_detail=get_object_or_404(Lostfound,pk=lostfound_id)
   
    return render(request,'lostfound_detail.html',{'lostfound_detail':lostfound_detail})

def lostfound_new(request):
    return render(request, 'lostfound_new.html')

def lostfoundpost(request):
    if request.method=='POST':
        form=LostfoundPost(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('lostfound_main') #글쓰고 나면 홈이아니라 lostfound에메인에가야할거같아서 
    else:

        form=LostfoundPost()
        return render(request, 'lostfound_new.html',{'form':form})