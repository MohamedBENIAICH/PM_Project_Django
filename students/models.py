from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField(null=True, blank=True)
    is_present = models.BooleanField(default=False)
