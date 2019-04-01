from django.db import models

# Create your models here.
import datetime as dt

class tags(models.Model):
    name = model.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()

class Locattion(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    project_image = models.ImageField(upload_to='picture/', null=True ,blank=True)
    description = models.TextField()
    project_url=model.URLField(max_length=300)

class Profile (models.Model):
    class Meta:
        db_table = 'profile'
    
    bio = models.TextField(max_length=100, null=True, blank=True, default="bio")
    profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default=0)
    user = 

