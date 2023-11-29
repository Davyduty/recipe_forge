from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Item(models.Model):
    name = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    description = models.TextField()
    color = models.CharField(max_length=30,default="white")

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
