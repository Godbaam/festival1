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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', festival_main.views.home, name='home'),
    path('line_up/', festival_main.views.line_up, name='line_up'),

    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name = 'logout'),
    
    path('flea_main/', flea_market.views.flea_main, name='flea_main'),
    path('flea_main/<int:flea_market_id>/', flea_market.views.flea_detail, name='flea_detail'),
    path('flea_main/flea_create/', flea_market.views.flea_create, name='flea_create'),
    path('flea_main/flea_new/', flea_market.views.flea_marketpost, name='flea_marketpost'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
