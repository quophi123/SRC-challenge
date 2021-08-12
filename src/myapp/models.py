from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField()
    
    
    def __str__(self):
        return self.name
    
