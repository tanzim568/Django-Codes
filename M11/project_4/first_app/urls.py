# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('home/', views.home),
    path('index/',views.index,name='home'),
    # path('about/<int:id>/',views.about,name='about'),
    path('about/',views.about,name='about'),
]
