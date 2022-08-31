from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('read/', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('post/', views.post, name='post')
]