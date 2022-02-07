from django.db import models
from django.urls import reverse

# Create your models here.

class productmodel(models.Model):
    pname=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=100)
    pprice=models.IntegerField()
    discount=models.IntegerField()
    pimg=models.ImageField(upload_to='product/')
    
    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
