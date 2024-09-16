from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={'author':'Tanzim','Age':5,'Designation':'Junior Software Engineer','lst':['python','is','my ','first','choice'],'birthday':datetime.datetime.now(),'val':10,'courses':[
        {
            'id':1,
            'name':'python',
            'fee':5000
        },
        {
            'id':2,
            'name':'django',
            'fee':10000
        },
        {
            'id':3,
            'name':'C++',
            'fee':7000
        },
        
    ]}
    
    return render(request,'first_app/home.html',d)  #django context is essentially a python dictionary
