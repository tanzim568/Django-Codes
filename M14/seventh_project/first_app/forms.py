from django import forms
from .import models
# from first_app.models import StudentModel


class StudentFrom(forms.ModelForm):
    class Meta:
        model= models.StudentModel
        # fields= ['name','roll']
        fields='__all__'
        # exclude=['roll']
        labels={
            'name':'Student Name',
            'father_name':'Dad',
        }
        widgets= {
            'name': forms.TextInput(attrs={'class': ''}),
            # 'roll':forms.IntegerField()
        }
        help_texts={
            'name':"Write Your Full Name"
        }
        error_messages={
            'name':{'required':'Your name is required'}
        }
    