# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls), projuect admin ektai thakbe
    path('home/',home),
]