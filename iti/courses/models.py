from django.db import models
from depts.models import Department


# Create your models here.

class Course(models.Model):
    # create
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name
