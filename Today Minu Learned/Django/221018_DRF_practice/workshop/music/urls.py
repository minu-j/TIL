"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('artists/<int:artist_pk>/music/', views.music_create),
    path('music/', views.music_list),
    path('music/<int:music_pk>/', views.music_detail),
]
