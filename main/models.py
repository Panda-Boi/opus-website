from django.db import models
from django.contrib.auth.models import User

class Org(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "data")
    name = models.CharField(max_length = 64)
    info = models.CharField(max_length = 128)
    website = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"Username : {self.user}, Name : {self.name}, Info : {self.info}"

