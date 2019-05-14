"""festival_hongik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import account.views
import festival_main.views
import flea_market.views
import honey.views
import lostfound.views
import publicity.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', festival_main.views.home, name='home'),
    path('line_up/', festival_main.views.line_up, name='line_up'),
    path('line_up_en/', festival_main.views.line_up_en, name='line_up_en'),
    path('line_up_art/', festival_main.views.line_up_art, name='line_up_art'),    
    path('beatz/', festival_main.views.beatz, name='beatz'),
    path('contact/', festival_main.views.contact, name='contact'), 

    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name = 'logout'),
    
    path('lostfound_main/',lostfound.views.lostfound_main, name='lostfound_main'),
    path('lostfound_main/lostfound_detail/<int:lostfound_id>/',lostfound.views.lostfound_detail, name='lostfound_detail'),
    path('lostfound_main/lostfound_new/',lostfound.views.lostfoundpost, name='lostfound_new'),
    
    path('flea_main/', flea_market.views.flea_main, name='flea_main'),
    path('flea_main/<int:flea_market_id>/', flea_market.views.flea_detail, name='flea_detail'),
    path('flea_main/flea_create/', flea_market.views.flea_create, name='flea_create'),
    path('flea_main/flea_new/', flea_market.views.flea_marketpost, name='flea_marketpost'),

    path('drink/', honey.views.drink, name='drink'),
    path('map/', honey.views.map, name='map'),
    path('store/', honey.views.store, name='store'),
    path('toilet/', honey.views.toilet, name='toilet'),
    
    path('publicity/', publicity.views.publicity_main, name = 'publicity_main'),
    path('publicity/publicity_detail/<int:publicity_id>/', publicity.views.publicity_detail, name = 'publicity_detail'),
    path('publicity/new', publicity.views.publicity_post, name = 'publicity_new'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
