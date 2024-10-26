from django import forms
from django.core import validators


# widgets == field to html input

class contactForm(forms.Form):
    name=forms.CharField(label="Full Name :",help_text="Enter your full name",required=False,widget=forms.Textarea(attrs ={'id':'text_area','class':'class1 class2','placeholder':'Enter your name'}))
    # file=forms.FileField()
    email=forms.EmailField(label="User Email") 
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput)
    check=forms.BooleanField()
    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    Appointment=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    choices=[('S','Small'),('M','Medium'),('L','Large')]
    Size=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    meal=[('P','Pepperoni'),('D','Dominoz'),('B','Blusters')]
    Pizza=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
    
    # target is to validate the form data 
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <10:
    #         raise forms.ValidationError("Enter a valid name within 10 characters")
    #     else:
    #         return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if  '.com' not in valemail:
    #         raise forms.ValidationError("Not valid email")
    #     return valemail 
    
    
    # we can put it together
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data['name']
        valemail=self.cleaned_data['email']

        if len(valname)<10 :
            raise forms.ValidationError("Enter at least 10 characters")
        if '.com' not in valemail:
            raise forms.ValidationError("Email must contain .com")
        
def check(val):
    if len(val)<10:
        raise forms.ValidationError("enter at least 10 character")
      
        
class StudentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(11,message='Enter a name maximum 10 character'),validators.MinLengthValidator(10,message="Enter a name at least 10 character")])
    email=forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid Email')])
    text=forms.CharField(widget=forms.TextInput,validators=[check])
    age=forms.IntegerField(widget=forms.NumberInput,validators=[validators.MaxValueValidator(60,message="Enter a age within 60"),validators.MinValueValidator(32,message='Enter a value above 32')])
    # file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])
    
    # file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])
    
class PasswordValidationProject(forms.Form):
    # name=forms.CharField(widget=forms.TextInput)
    # password=forms.PasswordInput()  #othoba forms.CharField(widget=forms.PasswordInput) searched but this is not the right way according google below one is
    # confirm_password=forms.PasswordInput()
    # name=forms.CharField(widget=forms.TextInput)
    # password=forms.CharField(widget=forms.PasswordInput)
    # confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data=super().clean()
        valpass= self.cleaned_data['password']
        valcon= self.cleaned_data['confirm_password']
         
        if valpass != valcon:
            raise forms.ValidationError("Password doesn't match")
        