from django.db import models


# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.dept_name
