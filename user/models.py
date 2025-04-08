from django.db import models


class Account(models.Model):
    full_name = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.full_name}"
    

