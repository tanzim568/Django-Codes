from django.shortcuts import render,redirect
from .import forms

# Create your views here.

def add_category(request):
    if request.method == "POST":  #user post request koreche
        
        category_form=forms.CategoryForm(request.POST) # user er post request data ekhane capture kora hoeche
        if category_form.is_valid():  #post kora data valid ki na check kora hocche 
            category_form.save()     # jodi data valid then databse e save korbo
            return redirect('add_category') #sob thik thkale take add author ei url e pathiye dibo
    
    else:
        category_form=forms.CategoryForm() # jodi get request hoi then blank form pabe
    return render(request,'add_category.html',{'form':category_form})