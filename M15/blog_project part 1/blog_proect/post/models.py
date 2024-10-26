from django.db import models
from categories.models import Catergory
from author.models import Author
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Catergory)   #ekta post mulitple category r modde thakte pare abar ekta category r modde multiple post thakte pare... 
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default=None)
    
    
    def __str__(self):
        return f"{self.title}"