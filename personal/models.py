from django.db import models

# Create your models here.
class personal(models.Model):
   goal=models.CharField(max_length=50)
   conditions=models.CharField(max_length=100)
   pub_date=models.DateTimeField()
   def condi(self):
        return self.conditions[:50]
   def dating(self):
       return self.pub_date.strftime('%B %e %Y')
   def __str__(self):
       return self.goal


