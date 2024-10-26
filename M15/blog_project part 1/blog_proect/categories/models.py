from django.db import models

# Create your models here.


class Catergory(models.Model):
    name=models.CharField(max_length=20)
    
    
    def __str__(self) -> str:
        # return super().__str__()
        return f"{self.name}"