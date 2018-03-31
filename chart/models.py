from django.db import models

class Chart(models.Model):
    name = models.TextField()
    data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
