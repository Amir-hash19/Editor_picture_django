from django.db import models
from user.models import Account



class ImageCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)


    def __str__(self):
        return f"{self.name}"




class UserImage(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, unique=True)
    original = models.ImageField(upload_to='images/original/')
    edited = models.ImageField(upload_to="images/edited/", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user.username} - {self.id}"

