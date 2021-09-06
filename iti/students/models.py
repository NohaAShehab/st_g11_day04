from django.db import models


# Create your models here.


class Student(models.Model):
    # attributes
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
