from django.db import models

# Create your models here.
class Resume(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=100)
    degree = models.TextField(max_length=500)
    inter = models.TextField(max_length=500)
    highschool = models.TextField(max_length=500)
    about_you = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)
    # cv_img = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.name
