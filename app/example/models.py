from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
