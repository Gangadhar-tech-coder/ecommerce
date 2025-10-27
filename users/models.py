from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(null=True)
    bio=models.CharField(max_length=500, null=True)
    phone_number=models.CharField(max_length=15, null=True)
    def __str__(self):
        return f'{self.user.username}\'s Profile'
# Create your models here.
class Address(models.Model):
    user=models.OneToOneField(Profile, on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=10)
