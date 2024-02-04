from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = models.Manager()
    
    def getUsername(self):
        return str(self.pk) + ": " + self.username
    
    def getPassword(self):
        return str(self.pk) + ": " + self.password