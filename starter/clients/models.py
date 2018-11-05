from django.db import models
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=50)
    deleted = models.BooleanField()
    importance = models.FloatField()
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    