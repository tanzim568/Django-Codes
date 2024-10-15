from django.shortcuts import render
from .forms import contactForm , StudentData ,PasswordValidationProject

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html')


def djangoForm(request):
    if request.method=='POST':
        form=contactForm(request.POST, request.FILES)     #to get files from post method add request.FILES
        if form .is_valid():
            # File=form.cleaned_data['file']
            # with open('./first_app/upload/' + File.name, 'wb+') as destination:
            #     for chunk in File.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
        return render (request,'./first_app/django_form.html',{'form':form})

    else:
        form=contactForm()
    return render(request,'./first_app/django_form.html',{'form':form})


# def PasswordValidationProject(request):
#     if request.method =='POST':
#         form=PasswordValidationProject(request.POST)
#         if form .is_valid():
#             print(form.cleaned_data)
#         return render(request,'./first_app/Password_validation.html/',{'form':form})
#     else:
#         form=PasswordValidationProject()
#     return render(request,'./first_app/Password_validation.html/',{'form':form})

def studentform(request):
    if request.method=='POST':
        form=StudentData(request.POST, request.FILES)
        if form .is_valid():
            print(form.cleaned_data)
        return render(request,'./first_app/student_form.html/',{'form':form})
    else:
        form=StudentData()
    return render(request,'./first_app/student_form.html/',{'form':form})

def PasswordValidation(request):
    if request.method=='POST':
        form=PasswordValidationProject(request.POST)
        if form .is_valid():
            print(form.cleaned_data)
        # return render(request,'./first_app/student_form.html/',{'form':form})
    else:
        form=PasswordValidationProject()
    return render(request,'./first_app/student_form.html/',{'form':form})

# def PasswordValidationProject(request):
#     if request.method=='POST':
#         form=PasswordValidationProject(request.POST)
#         if form .is_valid():
#             print(form.cleaned_data)
#         return render(request,'./first_app/student_form.html/',{'form':form})
#     else:
#         form=PasswordValidationProject()
#     return render(request,'./first_app/student_form.html/',{'form':form})


def about(request):
    if request.method =='POST':
        print(request.POST)
        name=request.POST.get('username')
        email=request.POST.get('useremail')
        select=request.POST.get("select")
        return render(request,'./first_app/about.html',{'name':name,'email':email,'select':select})
    else:
        return render(request,'./first_app/about.html')


def form(request):
    # print(request.POST)

    return render(request,'./first_app/form.html')


# first e webpage e jabe then oi page er url borabor urls.py te asbe then views.py te oi function e asbe then page theke kono request thakle print kora jbe kono value thkle oitai oi page er html file theke niye views.py te ene dekha jabe final data veiws theke render hoye ekta template dekha jabe oi page e