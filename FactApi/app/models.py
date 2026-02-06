from django.db import models

# Create your models here.

class Fact(models.Model):
    fact = models.TextField()

    def __str__(self):
        return self.fact