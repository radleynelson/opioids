from django.contrib.auth.models import AbstractUser
from django.db import models

 
# Create your models here.
class User(AbstractUser):
   def returnName(self):
       return self.first_name + ' ' + self.last_name; 


