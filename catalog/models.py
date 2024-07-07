from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flowers/')
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='flowers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
