from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=75)
    task_description = models.TextField(null=True)
    is_completed = models.BooleanField(default=False)