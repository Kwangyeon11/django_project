"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView 
from mysite.views import UserCreateView, UserCreateDoneTV 


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # shkim
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),   
    path('blog/', include('blog.urls')),  
    path('photo/', include('photo.urls')),  
    #path("polls/", include("polls.urls")),
    
    # 인증 URL 3개 추가
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name = 'register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name = 'register_done'),
        
    # class-based views
    #path('bookmark/', BookmarkLV.as_view(), name='index'),
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )