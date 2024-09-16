from django.contrib import admin
from django.urls import path,include
from .views import about,  contact

urlpatterns = [
    path('about',about),
    path('contact/',contact),
    # path('navigation/',include("navigation.urls")),
]
