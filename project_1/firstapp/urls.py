from django.urls import path

from .views import courses,about,home
# from .import views

urlpatterns = [
   
    # path('',home),
    path('courses/',courses),
    path('about/',about),
    path('',home),
    
]