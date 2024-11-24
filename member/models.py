from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"




class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(blank=True, null=True)
    bio = models.CharField(blank=True, null=True, max_length=500)

    

    def __str__(self):
        return f"{self.user.username}"
    



