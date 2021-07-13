from django.db import models
from django.contrib.auth.models import User

class Org(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "data")
    name = models.CharField(max_length = 64)
    info = models.TextField()
    website = models.CharField(max_length = 64)
    metadata = models.CharField(max_length = 128)
    logo = models.ImageField(default='logos/default.png', upload_to='logos')
    
    def __str__(self):
        return f"Username : {self.user}, Name : {self.name}, Info : {self.info}, MetaData : {self.metadata}"

