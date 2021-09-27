from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    date = models.CharField(max_length=100,default=0)

