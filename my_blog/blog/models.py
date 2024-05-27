from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=500)
    money = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title