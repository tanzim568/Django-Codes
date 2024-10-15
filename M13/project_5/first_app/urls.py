
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('about/', views.about,name='aboutpage'),
    path('form/', views.form,name='submit_form'),
    path('django_form/', views.djangoForm,name='django_form'),
    path('student_form/', views.PasswordValidation,name='student_form'),
    

    
]
