from django.db import models
from depts.models import Department

# Create your models here.


class Student(models.Model):
    # any added to the table through the model --> not null
    # attributes
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    # male or female
    gender = models.CharField(
        max_length=2,
        choices=[
            ("m", "Male"),
            ("f", "Female")
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ## Alter table students add column dept --> reference department model,
    # on delete --> null

    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept_students")

    def __str__(self):
        return self.name
