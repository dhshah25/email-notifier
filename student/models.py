from django.db import models

class Reg(models.Model):
  
  username = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=50)

