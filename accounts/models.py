from django.db import models

class Account(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=50)

class Notice(models.Model):
  notice=models.CharField(max_length=100)