from django.db import models

class Chart(models.Model):
    name = models.TextField()
    data = models.TextField()
# Create your models here.
