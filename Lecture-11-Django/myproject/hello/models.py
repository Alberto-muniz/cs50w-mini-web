from django.db import models

# Create your models here.
from django.db import models

class Computer(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name