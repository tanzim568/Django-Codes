from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def home(request):
    if request.method == 'POST':
        form= forms.StudentFrom(request.POST)
        if form .is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            # return render(request,'.first_app/home.html/')
            return redirect ("homepage")
    else:
        form=forms.StudentFrom()
        return render(request,'./first_app/home.html',{'data':form})