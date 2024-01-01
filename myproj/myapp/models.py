from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.BigIntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Add(models.Model):
    cname = models.CharField(max_length=30)
    ccolor = models.CharField(max_length=30)
    cprice = models.IntegerField()

    def __str__(self):
        return self.cname