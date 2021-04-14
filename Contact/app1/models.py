from django.db import models

# Create your models here.
class contact_details(models.Model):
    Name = models.CharField(max_length=30)
    Number = models.IntegerField()
    Address = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
