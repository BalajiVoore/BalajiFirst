from django.db import models

# Create your models here.

class job(models.Model):
    imageNew= models.ImageField(upload_to='images')
    summaryNew= models.CharField(max_length=200)



