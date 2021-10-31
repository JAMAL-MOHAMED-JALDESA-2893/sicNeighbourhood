from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=200)
    hood_location = models.CharField(max_length=200)
    hood_description = models.TextField(max_length=500, blank=True)
    hood_photo = CloudinaryField('photo', default='photo')
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='admin')


    def __str__(self):
        return self.hood_name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()    