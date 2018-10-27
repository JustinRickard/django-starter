from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    deleted = models.BooleanField()
    importance = models.FloatField()

    def __str__(self):
        return self.name
    